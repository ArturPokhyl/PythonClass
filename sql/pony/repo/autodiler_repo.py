from pony.orm import db_session, select

from sql.pony.models.models import Autodiler


class AutodilerRepository:
    def __init__(self, db):
        self.db = db
        self.model = Autodiler

    @db_session
    def get_all(self):
        return list(select(a for a in self.model)[:])

    @db_session
    def get_by_id(self, id: int):
        return self.model.get(lambda a: a.id == id)

    @db_session
    def create_new(self, autodiler_model: Autodiler):
        try:
            self.db.insert(autodiler_model)
            return True
        except Exception as e:
            print(e)
            return False

    @db_session
    def delete(self, id: int):
        diler = self.model.get(lambda a: a.id == id)
        if diler:
            diler.delete()
            return True
        return False

    @db_session
    def update(self, autodiler_model: Autodiler):
        diler = self.model.get(lambda a: a.id == autodiler_model.id)
        if diler:
            diler.set(
                company_name=autodiler_model.company_name,
                city=autodiler_model.city,
                diler_id=autodiler_model.diler_id,
            )
