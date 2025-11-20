from typing import Union

from fastapi import FastAPI

from app.controllers.car_controller import CarController
from app.database import create_db_and_tables, test_connection
from app.models.car import Car

app = FastAPI()

@app.on_event("startup")
def on_startup():
    test_connection()
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id, 
        "q": q
    }

@app.get("/cars")
def read_cars():
    return CarController.get_all_cars()


@app.post("/cars")
def create_car(car: Car):
    return CarController.create_car(car)
