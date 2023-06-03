import requests
import uuid

HOST = "http://127.0.0.1:8000"


def test_write_neardocs_and_delete() -> None:
    uid = uuid.uuid4()
    r1 = requests.post(f"{HOST}/write", json={"uid": str(uid), "text": "cat"})
    assert r1.status_code == 200
    r2 = requests.get(f"{HOST}/neardocs?text=dog")
    assert r2.status_code == 200
    r3 = requests.get(f"{HOST}/delete?uid={uid}")
    assert r3.status_code == 200
