from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_standard_house():
       payload = {
               "land_size_sqft":100,
               "number_of_rooms":1,
               "garage":2,
               "location":"colombo"
             }

       response = client.post("/predict",json=payload)
       assert response.status_code == 200

       assert response.json()["predicted_price"] ==1170000.0

def test_predict_mansion():
    # Scenario 2: A big house
    payload = {
        "land_size_sqft": 200,
        "number_of_rooms": 10,
        "garage": 0,
        "location": "Kandy"
    }
    
    # Math: (200 * 200) + (10 * 150000) + (0 * 500000)
    #      = 40,000 + 1,500,000 + 0 = 1,540,000
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["predicted_price"] == 1540000.0

