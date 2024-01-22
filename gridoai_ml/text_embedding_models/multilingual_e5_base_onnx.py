from gridoai_ml.text_embedding_models.abs_model import AbsTextEmbeddingModel
import typing as t
from transformers import PreTrainedTokenizerFast
import onnxruntime as ort
from gridoai_ml.utils import check_and_download_hf_files
import json

import numpy as np


def average_pool(
    last_hidden_state: np.ndarray, attention_mask: np.ndarray
) -> np.ndarray:
    # Apply attention mask
    attention_mask_expanded = np.expand_dims(attention_mask, -1)
    last_hidden_masked = np.where(attention_mask_expanded, last_hidden_state, 0)

    # Sum over the sequence dimension and divide by the sum of the attention mask
    sum_hidden = last_hidden_masked.sum(axis=1)
    mask_sum = attention_mask.sum(axis=1, keepdims=True)

    # Avoid division by zero
    mask_sum = np.where(mask_sum == 0, 1, mask_sum)

    # Average pooling
    average_pooled = sum_hidden / mask_sum

    return average_pooled


class OnnxRuntimeTextEmbeddingModel(AbsTextEmbeddingModel):
    def __init__(self) -> None:
        repo_id = "intfloat/multilingual-e5-base"
        files = [
            "onnx/model.onnx",
            "onnx/tokenizer.json",
            "onnx/tokenizer_config.json",
            "onnx/special_tokens_map.json",
        ]
        destination_dir = "./onnx/multilingual-e5-base/"
        check_and_download_hf_files(repo_id, files, destination_dir)

        with open(destination_dir + "special_tokens_map.json", "r") as f:
            special_tokens_map = json.load(f)
        for key, value in special_tokens_map.items():
            if isinstance(value, dict):
                special_tokens_map[key] = value["content"]

        self.tokenizer = PreTrainedTokenizerFast(
            tokenizer_file=destination_dir + "tokenizer.json",
            tokenizer_config=destination_dir + "tokenizer_config.json",
        )
        self.tokenizer.add_special_tokens(special_tokens_map)
        so = ort.SessionOptions()
        so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        self.ort_sess = ort.InferenceSession(
            destination_dir + "model.onnx",
            sess_options=so,
            providers=["CPUExecutionProvider", "CUDAExecutionProvider"],
        )

    @property
    def dim(self) -> int:
        return 768

    def calc(
        self, texts: t.List[str], instruction: t.Optional[str] = None
    ) -> t.List[t.List[float]]:
        print(f"Calculating embeddings for {len(texts)} texts in onnx")
        if instruction:
            texts = [f"{instruction}: {text}" for text in texts]
        results = []
        for text in texts:
            batch_dict = self.tokenizer(
                [text],
                max_length=512,
                padding=True,
                truncation=True,
                return_tensors="np",
            )
            last_hidden_state = self.ort_sess.run(
                None,
                {
                    "input_ids": batch_dict["input_ids"],
                    "attention_mask": batch_dict["attention_mask"],
                },
            )[0]
            embeddings = average_pool(last_hidden_state, batch_dict["attention_mask"])

            results.append(embeddings[0].tolist())
        return results
