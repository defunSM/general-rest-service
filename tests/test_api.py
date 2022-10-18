""" Tests for api.py"""

# pylint: disable=[missing-function-docstring]

from mysecrets import TEST_USER
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

async def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_token():
    response = client.get("/", params=TEST_USER)
    assert response.json()['token_type'] == 'bearer'

def test_read_text_summary():
    params = {'text': 'a'}
    response = client.get('/countleaf/v1/summary', params=params)
    assert response.status_code == 200

def test_sentiment_analysis():
    payload = TEST_USER
    response = client.get('/countleaf/v1/sentiment')
    assert response.status_code == 200
    

    