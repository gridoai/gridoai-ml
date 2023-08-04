import requests
import uuid

HOST = "http://127.0.0.1:8000"


def test_embeddding() -> None:
    r = requests.post(
        f"{HOST}/embed",
        json={
            "texts": ["cats are better than people"],
            "instruction": "query",
            "model": "multilingual-e5-base",
        },
    )
    assert r.status_code == 200
