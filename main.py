from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HousePredictionInput(BaseModel):
    number_of_rooms: int
    location: str
    land_size_sqft: float
    garage: int

@app.post("/predict")
def predict_price(item: HousePredictionInput):
    estimated_price = (item.land_size_sqft * 200) + (item.number_of_rooms * 150000) + \
    (item.garage * 500000)
    return {"predicted_price": estimated_price}
