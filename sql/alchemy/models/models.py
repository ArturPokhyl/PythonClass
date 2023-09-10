from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class CarModel(Base):
    __tablename__ = "car"
    car_id = Column(INTEGER, primary_key=True)
    brand = Column(VARCHAR(30))
    model = Column(VARCHAR(30))
    mileage = Column(INTEGER)
    diler = Column(INTEGER)
    diler_id = relationship("AutodilerModel", back_populates="car")

    def __repr__(self):
        return (
            f"Id: {self.car_id}, brand: {self.brand}, model: {self.model}, mileage - {self.mileage}, diler - {self.diler},"
            f"diler_id - {self.diler_id}"
        )


class AutodilerModel(Base):
    __tablename__ = "autodiler"
    id = Column(INTEGER, primary_key=True)
    company_name = Column(VARCHAR(50))
    city = Column(VARCHAR(50))
    diler_id = Column(ForeignKey("car.diler"))
    car = relationship("CarModel", back_populates="diler_id")

    def __repr__(self):
        return (
            f"Id: {self.id}, company_name: {self.company_name}, city: {self.city}, diler_id: {self.diler_id}"
            f"car: {self.car}"
        )
