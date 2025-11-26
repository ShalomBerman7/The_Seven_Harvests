from typing import Optional, List
from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship


class SoldiersT(SQLModel, table=True):
    personal_number: int = Field(primary_key=True)
    first_name: str
    last_name: str
    gender: str
    city_of_residence: str
    distance_from_base: int
    status: bool = True


class HousesT(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    rooms: int
    beds: int


engine = create_engine("sqlite:///data/soldiers.db")  # , echo=True


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


