from random import randint
import datetime

import faker

from config.db_session import session
from config.db_models import Student, Group, Grade, Teacher, Subject

DB_NAME = "college.db"

GROUPS_NUMBER = 3
TEACHERS_NUMBER = 5
SUBJECTS_NUMBER = 5
STUDENTS_NUMBER = 18
MARKS_NUMBER = 10

class DataGenerator:
    def __init__(self, grp_num, teach_num, subj_num, stud_num, mark_num):
        self.grp_num = grp_num
        self.teach_num = teach_num
        self.subj_num = subj_num
        self.stud_num = stud_num
        self.mark_num = mark_num
        self.fake = faker.Faker("uk-UA")

    def generate_groups_data(self):
        for _ in range(self.grp_num):
            group = Group(name=self.fake.postcode())
            yield group

    def generate_teachers_data(self):
        for _ in range(self.teach_num):
            teacher = Teacher(fullname=self.fake.full_name())
            yield teacher

    def generate_subjects_data(self):
        for _ in range(self.subj_num):
            subject = Subject(
                name=self.fake.job(), teacher_id=randint(1, self.teach_num)
            )
            yield subject

    def generate_students_data(self):
        for _ in range(self.stud_num):
            student = Student(
                fullname=self.fake.full_name(), group_id=randint(1, self.grp_num)
            )
            yield student

    def generate_grades_data(self):
        for student in range(1, self.stud_num + 1):
            for subject in range(1, self.subj_num + 1):
                for _ in range(self.mark_num):
                    grades_date = f"2024-{randint(1,12):02d}-{randint(10, 28):02d}"
                    grades_date = datetime.datetime.strptime(
                        grades_date, "%Y-%m-%d"
                    ).date()
                    grades = randint(6, 12)
                    mark = Grade(
                        student_id=student,
                        subjects_id=subject,
                        grade=grades,
                        grade_date=grades_date
                    )
                    yield mark


class DataExporter:
    def __init__(self, db_filename: str):
        self.db_filename = db_filename

    def write_data_to_db(self, *data_generators):
        with session as conn:
            for data_generator in data_generators:
                for data in data_generator:
                    conn.add(data)
            conn.commit()

def fill_in_db():
    # Генератор для создания данниых в базу
    generator = DataGenerator(
        GROUPS_NUMBER, TEACHERS_NUMBER, SUBJECTS_NUMBER, STUDENTS_NUMBER, MARKS_NUMBER
    )

    # Инициализацыя генераторов для создания данниых в базу
    groups_data_generator = generator.generate_groups_data()
    teachers_data_generator = generator.generate_teachers_data()
    subjects_data_generator = generator.generate_subjects_data()
    students_data_generator = generator.generate_students_data()
    grades_data_generator = generator.generate_grades_data()

    # Запись данниых в базу
    exporter = DataExporter(DB_NAME)
    exporter.write_data_to_db(
        groups_data_generator,
        teachers_data_generator,
        subjects_data_generator,
        students_data_generator,
        grades_data_generator,
    )


if __name__ == "__main__":
    fill_in_db()