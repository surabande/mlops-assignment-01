from fastapi.testclient import TestClient
from api.main import app

# Create a TestClient instance to simulate API requests
client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_endpoint():
    # Sample healthy patient data
    sample_payload = {
        "age": 55, "sex": 1, "cp": 0, "trestbps": 140, 
        "chol": 250, "fbs": 0, "restecg": 0, "thalach": 120, 
        "exang": 1, "oldpeak": 1.5, "slope": 1, "ca": 0, "thal": 2
    }
    
    response = client.post("/predict", json=sample_payload)
    
    # Assert the request was successful
    assert response.status_code == 200
    
    # Assert the response contains the required keys
    json_response = response.json()
    assert "prediction" in json_response
    assert "confidence_scores" in json_response