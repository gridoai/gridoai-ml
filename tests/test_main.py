import requests
import uuid


def test_write_neardocs_and_delete() -> None:
    uid = uuid.uuid4()
    r1 = requests.post(
        "http://127.0.0.1:8000/write", json={"uid": str(uid), "text": "cat"}
    )
    assert r1.status_code == 200
    r2 = requests.get("http://127.0.0.1:8000/neardocs?text=dog")
    assert r2.status_code == 200
    r3 = requests.get(f"http://127.0.0.1:8000/delete?uid={uid}")
    assert r3.status_code == 200
