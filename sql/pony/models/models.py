from pony.orm import Database, PrimaryKey, Required, Set

db = Database()
db.bind(provider='postgres', user='postgres', password='11223344', host='127.0.0.1', database='car')


class Car(db.Entity):
    _table_ = "car"
    car_id = PrimaryKey(int, auto=True)
    brand = Required(str, 30)
    model = Required(str, 30)
    mileage = Required(int)
    diler = Required(int)
    diler_id = Required("Autodiler", column="diler_id")
    autodiler = Set("Autodiler")


class Autodiler(db.Entity):
    _table_ = "autodiler"
    id = PrimaryKey(int, auto=True)
    company_name = Required(str, 50)
    city = Required(str, 50)
    diler_id = Set(Car)


db.generate_mapping()
