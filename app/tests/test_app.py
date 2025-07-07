from main import app

def test_root():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enterprise CI/CD" in response.data 