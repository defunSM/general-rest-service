""" Tests for api.py"""

# pylint: disable=[missing-function-docstring]

from mysecrets import TEST_USER
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def user_authentication_headers():
        # Get bearer token
    response = client.post('/token',
                         data=TEST_USER)
    response = response.json()
    auth_token = response['access_token']
    
    authorization = f"Bearer {auth_token}"
    headers = {"Authorization": authorization}
    
    return headers

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_token():
    response = client.post("/token",
                            data=TEST_USER,
                            )
    print(response.content)
    assert response.status_code == 200

def test_read_text_summary():
    params = {'text': 'a'}
    response = client.get('/countleaf/v1/summary', params=params)
    assert response.status_code == 200

def test_sentiment_analysis():
    data = {'text': 'I got the keys to the car.'}
    
    
    response = client.get('/countleaf/v1/sentiment', 
                          params=data, 
                          headers=user_authentication_headers())
    
    assert response.status_code == 200
    

    