
from enum import Enum
from fastapi import FastAPI

# Define an Enum for the car models
class CarModel(str, Enum):
    toyota = "toyota"
    honda = "honda"
    tesla = "tesla"

# Create an instance of FastAPI
app = FastAPI()

# Create a route that uses the Enum for path parameters
@app.get("/cars/{car_model}")
async def get_car(car_model: CarModel):
    # Return a message based on the car model
    if car_model is CarModel.toyota:
        return {"car_model": car_model, "message": "Reliable and efficient!"}
    elif car_model is CarModel.honda:
        return {"car_model": car_model, "message": "Great value for money!"}
    elif car_model is CarModel.tesla:
        return {"car_model": car_model, "message": "Electric and futuristic!"}
    return {"car_model": car_model, "message": "Unknown car model"}

