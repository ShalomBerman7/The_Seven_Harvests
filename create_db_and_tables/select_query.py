
# def get_course_by_id(course_id):
#     with Session(engine) as s:
#         statement = select(Courses).where(Courses.id == course_id)
#         results = s.exec(statement)
#         return results.all()
#
#
# def get_students_by_course(course_id) -> list[Courses]:
#     with Session(engine) as session:
#         statement = select(Students).where(Students.courseId == course_id)
#         results = session.exec(statement)
#         return results.all()
#
#
# def get_students_with_courses():
#     with Session(engine) as session:
#         statement = select(Students, Courses).join(Courses)
#         results = session.exec(statement)
#         for student, course in results:
#             print(f"{student.id}: {student.name}, {student.city}, Course: {course.name} ({course.hours} hours)")
#
#
# def update_course_status(course_id: int, new_status: bool):
#     with Session(engine) as session:
#         statement = select(Courses).where(Courses.id == course_id)
#         course = session.exec(statement).first()
#
#         if not course:
#             print("Course not found!")
#             return
#
#         course.is_active = new_status
#         session.add(course)
#         session.commit()
#         session.refresh(course)
#
#         print(f"Course ID {course.id} status updated to {course.is_active}")
#
#
# def get_id():
#     n = int(input('answer id: '))
#     return n
#
