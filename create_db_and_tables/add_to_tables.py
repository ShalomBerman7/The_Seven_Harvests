from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship
from create_db_and_tables.create_tables import SoldiersT, HousesT, engine


def add_soldier(personal_number: int, first_name: str, last_name: str, gender: str, city_of_residence: str, distance_from_base: int, status: str) -> None:
    soldier = SoldiersT(personal_number=personal_number, first_name=first_name, last_name=last_name, gender=gender, city_of_residence=city_of_residence, distance_from_base=distance_from_base, status=status)
    with Session(engine) as session:
        session.add(soldier)
        session.commit()
        session.refresh(soldier)
        print(f"Added soldier with id ={soldier.personal_number}")


def add_houses(name: str, room: int, bed: str):
    house = HousesT(name=name, room=room, bed=bed)
    with Session(engine) as s:
        s.add(house)
        s.commit()
        s.refresh(house)
        print(f"Added house with id ={house.id}")


def get_status_soldier() -> list[SoldiersT]:
    with Session(engine) as session:
        statement = select(SoldiersT).where(SoldiersT.status == True)
        results = session.exec(statement)
        return results.all()