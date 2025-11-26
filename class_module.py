from typing import Optional, List
from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship


class Soldiers:
    def __init__(self,
    personal_number,
    first_name,
    last_name,
    gender,
    city_of_residence,
    distance_from_base,
    status):
        self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city_of_residence = city_of_residence
        self.distance_from_base = distance_from_base
        self.status = status


class SoldiersT(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    personal_number: int
    first_name: str
    last_name: str
    gender: str
    city_of_residence: str
    distance_from_base: int
    status: str


class HousesT(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    rooms: int
    beds: int


def add_soldier(personal_number: int,
    first_name: str,
    last_name: str,
    gender: str,
    city_of_residence: str,
    distance_from_base: int,
    status: str) -> None:
    soldier = Soldiers(personal_number=personal_number, first_name=first_name, last_name=last_name, gender=gender, city_of_residence=city_of_residence, distance_from_base=distance_from_base, status=status)
    with Session(engine) as session:
        session.add(soldier)
        session.commit()
        session.refresh(soldier)
        print(f"Added soldier with id ={soldier.id}")