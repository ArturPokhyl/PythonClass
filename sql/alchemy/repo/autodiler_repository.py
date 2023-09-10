from sql.alchemy.models.models import AutodilerModel
from sql.alchemy.session import session


class AutodilerRepository:
    def __init__(self):
        self.__session = session
        self.__model = AutodilerModel

    def get_all(self):
        car = self.__session.query(self.__model).all()
        return car

    def get_by_id(self, id: int) -> AutodilerModel:
        diler: AutodilerModel | None = self.__session.get(self.__model, {"id": id})
        return diler

    def create_new(self, autodiler_model: AutodilerModel) -> bool:
        try:
            self.__session.add(autodiler_model)
            return True
        except:
            return False

    def delete(self, id: int) -> bool:
        try:
            address = self.get_by_id(id)
            self.__session.delete(address)
            return True
        except:
            return False

    def update(self, autodiler_model: AutodilerModel):
        self.__session.query(self.__model).filter(
            self.__model.id == autodiler_model.id
        ).update(
            {
                self.__model.company_name: autodiler_model.company_name,
                self.__model.city: autodiler_model.city,
                self.__model.diler_id: autodiler_model.diler_id,
            }
        )
