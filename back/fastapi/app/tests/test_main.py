from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

prefix='/profiles'

def test_get_all_profile():
    request = client.get(prefix + '/')
    assert request.status_code == 200
    assert request.json() == []

def test_profil_id_not_found():
    request = client.get(prefix + '/1')
    assert request.status_code == 404

def test_creat_profil():
    request = client.post("prefix + '/'" , jason ={"name" : "profil 1")
    