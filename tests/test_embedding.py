import requests
import uuid

HOST = "http://127.0.0.1:8000"


def test_embeddding() -> None:
    r = requests.get(f"{HOST}/embed?text=cats%20are%20better")
    assert r.status_code == 200
