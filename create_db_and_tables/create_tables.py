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



# if __name__ == '__main__':
#     create_db_and_tables()

    # add_course("SQL Basics", 20, True)
    # add_student('yosef', 527418787, 'tel aviv', 2)

    # active = get_status_soldier()
    # print('\nstatus soldier:')
    # for c in active:
    #     print(f"{c.personal_number}: {c.first_name} {c.last_name} active = {c.status}")

    # print('\nget course by id:')
    # course = get_course_by_id(get_id())
    # for i in course:
    #     print(f"{i.id}: {i.name} ({i.hours} hours) active = {i.is_active}")
    #
    # print('\nget students by course:')
    # student = get_students_by_course(get_id())
    # for s in student:
    #     print(f'{s.id}: {s.name}, {s.phone}, {s.city}, {s.courseId}')
    #
    # print("\nstudents with courses:")
    # get_students_with_courses()

    # update_course_status(get_id(), True)

    # with Session(engine) as session:
    #     session.delete(session.get(Students, 3))
    #     session.commit()
