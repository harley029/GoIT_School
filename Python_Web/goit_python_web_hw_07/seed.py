from abc import ABC, abstractmethod
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


class DataGeneratorInterface(ABC):
    @abstractmethod
    def generate_data(self):
        pass

class DataExporterInterface(ABC):
    @abstractmethod
    def write_data_to_db(self, *data_generators):
        pass

class FakerGenerator:
    def __init__(self, locale="uk-UA"):
        self.fake = faker.Faker(locale)

    def get_fake(self):
        return self.fake

class GroupDataGenerator(DataGeneratorInterface):
    def __init__(self, grp_num, fake):
        self.grp_num = grp_num
        self.fake = fake
    def generate_data(self):
        for _ in range(self.grp_num):
            group = Group(name=self.fake.postcode())
            yield group

class TeacherDataGenerator(DataGeneratorInterface):
    def __init__(self, teach_num, fake):
        self.teach_num = teach_num
        self.fake = fake

    def generate_data(self):
        for _ in range(self.teach_num):
            teacher = Teacher(fullname=self.fake.full_name())
            yield teacher

class SubjectDataGenerator(DataGeneratorInterface):
    def __init__(self, subj_num, teach_num, fake):
        self.subj_num = subj_num
        self.teach_num = teach_num
        self.fake = fake

    def generate_data(self):
        for _ in range(self.subj_num):
            subject = Subject(
                name=self.fake.job(), teacher_id=randint(1, self.teach_num)
            )
            yield subject

class StudentDataGenerator(DataGeneratorInterface):
    def __init__(self, stud_num, gr_num, fake):
        self.stud_num = stud_num
        self.gr_num = gr_num
        self.fake = fake

    def generate_data(self):
        for _ in range(self.stud_num):
            student = Student(
                fullname=self.fake.full_name(), group_id=randint(1, self.gr_num)
            )
            yield student

class GradeDataGenerator(DataGeneratorInterface):
    def __init__(self, mark_num, st_num, subj_num):
        self.mark_num = mark_num
        self.st_num = st_num
        self.subj_num = subj_num
        self.fake = faker.Faker("uk-UA")

    def generate_data(self):
        for student in range(1, self.st_num + 1):
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
                        grade_date=grades_date,
                    )
                    yield mark


class DataExporter(DataExporterInterface):

    def __init__(self, db_filename: str, db_session):
        self.db_filename = db_filename
        self.db_session = db_session

    def write_data_to_db(self, *data_generators):
        with self.db_session as conn:
            for data_generator in data_generators:
                for data in data_generator.generate_data():
                    conn.add(data)
            conn.commit()


def fill_in_db(db_filename, db_session):

    faker_generator = FakerGenerator()
    db_faker = faker_generator.get_fake()

    group_generator = GroupDataGenerator(GROUPS_NUMBER, db_faker)
    teacher_generator = TeacherDataGenerator(TEACHERS_NUMBER, db_faker)
    subject_generator = SubjectDataGenerator(SUBJECTS_NUMBER, TEACHERS_NUMBER, db_faker)
    student_generator = StudentDataGenerator(STUDENTS_NUMBER, GROUPS_NUMBER, db_faker)
    grade_generator = GradeDataGenerator(MARKS_NUMBER, STUDENTS_NUMBER, SUBJECTS_NUMBER)

    exporter = DataExporter(db_filename, db_session)
    exporter.write_data_to_db(
        group_generator,
        teacher_generator,
        subject_generator,
        student_generator,
        grade_generator,
    )


if __name__ == "__main__":
    fill_in_db(db_filename=DB_NAME, db_session=session)
