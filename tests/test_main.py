import requests
import uuid


def test_write(server: None) -> None:
    r = requests.post(
        "http://127.0.0.1:8000/write", json={"uid": str(uuid.uuid4()), "text": "cat"}
    )
    assert r.status_code == 200
