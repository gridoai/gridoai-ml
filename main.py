from context_handler.model import word2vec
import os

def main() -> None:
    use_mocked_model = os.environ.get("USE_MOCKED_MODEL", "FALSE") == "TRUE"
    print(f"Using mocked model: {use_mocked_model}")
    model = word2vec.load_model(use_mocked_model)
    vec = model["cat"]
    print(vec)

main()