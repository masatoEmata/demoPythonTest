from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get('/')
async def read_main():
    return {'msg': 'hello fastapi'}

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'hello fastapi.'}

client = TestClient(app)

