import pytest
from multiprocessing import Process
import os
import uvicorn
from context_handler.app import app
import time


def run_server():
    uvicorn.run(app)


@pytest.fixture
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start()
    time.sleep(5)
    yield None
    proc.kill()
