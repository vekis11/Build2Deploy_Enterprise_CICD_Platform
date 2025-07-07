import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

def test_root():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enterprise CI/CD" in response.data 
