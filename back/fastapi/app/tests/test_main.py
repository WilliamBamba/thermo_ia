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
    request = client.post(prefix + '/' , json ={"name" : "profil 1"})
    assert request.status_code == 200

def test_profil_id_found():
    request = client.get(prefix + '/1')
    assert request.status_code == 200
    assert request.json() == {"id": 1, "name": 'profil 1',"option_id": None, "time_table": None ,"url_agenda": None}

def test_update_profil():
    request = client.put(prefix + '/1', json ={"name" : "new Profil 1"})
    assert request.status_code == 200
    assert request.json() == {"id": 1, "name": 'new Profil 1',"option_id": None, "time_table": None ,"url_agenda": None}

def test_delete_profil():
    request = client.delete(prefix + '/1')
    assert request.status_code == 200
    request = client.get(prefix + '/1')
    assert request.status_code == 404