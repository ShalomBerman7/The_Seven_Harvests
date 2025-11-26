from typing import Optional, List
from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship


class Soldiers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    personal_number: int
    first_name: str
    last_name: str
    gender: str
    city_of_residence: str
    distance_from_base: int
    status: str


class Houses(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    rooms: int
    beds: int