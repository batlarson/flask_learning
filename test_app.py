import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_listar_activos(client):
    response = client.get("/activos")
    assert response.status_code == 200

def test_crear_activo(client):
    response = client.post("/activos", json={"ticker": "MAIN", "nombre": "Main Street Capital"})
    assert response.status_code == 201