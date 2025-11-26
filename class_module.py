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

    def add_soldier(self):
        pass
