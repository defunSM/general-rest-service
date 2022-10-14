from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    
def test_read_text_summary():
    response = client.get('/countleaf/v1/summary')
    assert response.status_code == 200
    
def test_sentiment_analysis():
    response = client.get('/countleaf/v1/sentiment')
    assert response.status_code == 200