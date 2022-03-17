# test the fastapi demo testclient

from fastapi.testclient import TestClient

# Import app from fastapi-demo.py
from fastapi-demo import app


#instantiate the test client with app
client = TestClient(app)

# write tests using same syntax as with the request module
def test_get_path():
    r = client.get("/items/42")
    assert r.status_code == 200
    assert r.json() == {"fetch": " Fetched 1 of 42"}
    
    
def test_get_path_query():
    r = cient.get("/items/42?count=5")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 5 of 42"}
    
    
def test_get_malformed():
    r = client.get("/items")
    assert r.status_code != 200
