import typing as t
import os
from huggingface_hub import hf_hub_download


def _raise(message: str) -> t.NoReturn:
    raise Exception(message)
    
def check_and_download_hf_files(repo_id, files, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)
    for file in files:
        file_path = os.path.join(destination_dir, os.path.basename(file))
        if not os.path.isfile(file_path):
            hf_hub_download(
                repo_id=repo_id,
                filename=file,
                cache_dir=destination_dir,
                force_filename=os.path.basename(file)
            )