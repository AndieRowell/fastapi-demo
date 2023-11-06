from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import pytest
import httpx

# importing the sys module
import sys

# inserting the mod.py directoy at
# position 1 in sys.path
sys.path.insert(1, '/workspaces/fastapi-demo') #find our path in the terminal should show it after root..

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_item():
    response = client.get("/items/3")
    assert response.status_code == 200
    assert response.json() == {"item_id": 3}
