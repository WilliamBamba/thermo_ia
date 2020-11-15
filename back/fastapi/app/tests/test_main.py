from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_all_profile():
    request = client.get('/profiles/')
    assert request.status_code == 200
    assert 1 == 1