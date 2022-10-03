from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_text():
    test_string = """
    Physics is the natural science that studies matter,[a] its fundamental the constituents, its motion and behavior through space and time, and the related entities of energy and force. Physics is one of the most fundamental scientific disciplines, with its main goal being to understand how the universe behaves. A scientist who specializes in the field of physics is called a physicist.
    """
    response = client.get("/countleaf/summary/?text=" + test_string)
    assert response.status_code == 200
    assert response.json() == {"words":61,"letters":316,"sentences":3,"letters_per_word":5.180327868852459,"words_per_sentence":20.333333333333332,"most_frequent_word":"the"}