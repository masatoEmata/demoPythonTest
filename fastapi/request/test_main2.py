from fastapi.testclient import TestClient
from .main2 import app

client = TestClient(app)

'''
GET METHOD
'''
def test_read_item():
    response = client.get('/items/foo', headers={'X-Token': 'coneofsilence'})
    assert response.status_code == 200
    assert response.json() == {
        'id': 'foo',
        'title': 'Foo',
        'description': 'xxxxxxxxxxx',
    }

def test_read_item_bad_token():
    response = client.get('/items/foo', headers={'X-Token': 'hailhydra'})
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid X-token header'}
    
def test_read_inexistent_item():
    response = client.get('/items/baz', headers={'X-Token': 'coneofsilence'})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not found'}

'''
POST METHOD
'''
def test_create_item():
    response = client.post(
        '/items/',
        headers={'X-Token': 'coneofsilence'},
        json={'id': 'foobar', 'title': 'Foobar', 'description': 'The Foo Barters'},
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 'foobar',
        'title': 'Foobar',
        'description': 'The Foo Barters',
    }

def test_create_item_bad_token():
    response = client.post(
        '/items/',
        headers={'X-Token': 'hailhydra'},
        json={'id': 'bazz', 'title': 'bazz', 'description': 'Drop the bazz'}
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid X-token header'}

def test_create_existing_item():
    response = client.post(
        '/items/',
        headers={'X-Token': 'coneofsilence'},
        json={
            'id': 'foo',
            'title': 'Foo',
            'description': 'xxxxxxxxxxx'
        }
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Item already exists'}
