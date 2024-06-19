import pytest
from src.app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Sentiment Analysis" in rv.data

def test_post(client):
    rv = client.post('/', data=dict(text='good'))
    assert rv.status_code == 200
    assert b"prediction" in rv.data
