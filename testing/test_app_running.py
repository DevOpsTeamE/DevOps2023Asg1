from main import *

def test_starting_app(client):
    response = client.get('/')
    assert response.status_code == 200
