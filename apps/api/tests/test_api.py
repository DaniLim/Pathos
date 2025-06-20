from fastapi.testclient import TestClient
from apps.api.main import app

client = TestClient(app)

def test_create_and_list_posts():
    # ensure feed empty
    resp = client.get('/posts')
    assert resp.status_code == 200
    initial_count = len(resp.json())

    # create post
    resp = client.post('/posts', json={'text': 'hello'})
    assert resp.status_code == 200
    data = resp.json()
    assert data['text'] == 'hello'
    assert 'id' in data

    # list posts again
    resp = client.get('/posts')
    assert resp.status_code == 200
    assert len(resp.json()) == initial_count + 1
