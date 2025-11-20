from sqlmodel import Session, select
from app.database import engine
from ..models.car import Car

class CarController:
    @staticmethod
    def get_all_cars():
        with Session(engine) as session:
            return session.exec(select(Car)).all()

    @staticmethod
    def create_car(car: Car):
        with Session(engine) as session:
            session.add(car)
            session.commit()
            session.refresh(car)
            return car