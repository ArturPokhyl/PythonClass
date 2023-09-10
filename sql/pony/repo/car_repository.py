from pony.orm import db_session, select

from sql.pony.models.models import Car


class CarRepository:
    def __init__(self, db):
        self.db = db
        self.model = Car

    @db_session
    def get_all(self):
        return list(select(c for c in self.model)[:])

    @db_session
    def get_by_id(self, car_id: int):
        return self.model.get(lambda c: c.car_id == car_id)

    @db_session
    def create_new(self, car_model: Car):
        try:
            self.db.insert(car_model)
            return True
        except Exception as e:
            print(e)
            return False

    @db_session
    def delete(self, car_id: int):
        car = self.model.get(lambda c: c.car_id == car_id)
        if car:
            car.delete()
            return True
        return False

    @db_session
    def update(self, car_model: Car):
        car = self.model.get(lambda c: c.car_id == car_model.car_id)
        if car:
            car.set(
                brand=car_model.brand,
                model=car_model.model,
                mileage=car_model.mileage,
                diler=car_model.diler,
            )
