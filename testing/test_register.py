from main import *

def test_register_successfully(client):
    response = client.post('/register', json={'username': 'newUser', 'password': 'newPassword'})
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_existing_registry(client):
    response = client.post('/register', json={'username': 'correctName', 'password': 'newPassword'})
    assert response.status_code == 400
    assert b'Username already exists. Please choose another username.' in response.data