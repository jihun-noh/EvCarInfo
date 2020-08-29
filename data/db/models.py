from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True)
    manufacturer = Column(String)
    model = Column(String)
    trim = Column(String)
    mileage = Column(String)
    year = Column(String)

class OldCar(Base):
    __tablename__ = 'old_car'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    trim = Column(String)
    year = Column(String)
    km = Column(String)
    location = Column(String)

class Subsidy(Base):
    __tablename__ = 'subsidy'

    id = Column(Integer, primary_key=True)
    trim = Column(String)
    subsidy_gov = Column(String)
    subsidy_local = Column(String)

class RegStatus(Base):
    __tablename__ = 'reg_status'

    id = Column(Integer, primary_key=True)
    year_month = Column(String)
    base = Column(String)
    base_value = Column(String)
    total = Column(String)

# class ChargingStation(Base):
#     __tablename__ = 'charging_station'

def create_tables(engine):
    Base.metadata.create_all(engine)
