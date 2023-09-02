from sql.models.models import CarModel
from sql.session import session


class CarRepository:
    def __init__(self):
        self.__session = session
        self.__model = CarModel

    def get_all(self):
        car = self.__session.query(self.__model).all()
        return car

    def get_by_id(self, car_id: int) -> CarModel:
        car: CarModel | None = self.__session.get(self.__model, {"car_id": car_id})
        return car

    def create_new(self, car_model: CarModel) -> bool:
        try:
            self.__session.add(car_model)
            return True
        except:
            return False

    def delete(self, car_id: int) -> bool:
        try:
            address = self.get_by_id(car_id)
            self.__session.delete(address)
            return True
        except:
            return False

    def update(self, car_model: CarModel):
        self.__session.query(self.__model).filter(
            self.__model.id == car_model.car_id
        ).update(
            {
                CarModel.brand: car_model.brand,
                CarModel.model: car_model.model,
                CarModel.mileage: car_model.mileage,
                CarModel.diler: car_model.diler,
            }
        )
