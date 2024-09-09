from random import randint
import sqlite3

import faker


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
            yield (self.fake.postcode(),)

    def generate_teachers_data(self):
        for _ in range(self.teach_num):
            yield (self.fake.full_name(),)

    def generate_subjects_data(self):
        for _ in range(self.subj_num):
            yield (self.fake.job(), randint(1, self.teach_num))

    def generate_students_data(self):
        for _ in range(self.stud_num):
            yield (self.fake.full_name(), randint(1, self.grp_num))

    def generate_grades_data(self):
        for student in range(1, self.stud_num + 1):
            for subject in range(1, self.subj_num + 1):
                for _ in range(self.mark_num):
                    grade_date = f"2024-{randint(1,12):02d}-{randint(10, 28):02d}"
                    grade = randint(6, 12)
                    yield (student, subject, grade, grade_date)


class DataExporter:
    @staticmethod
    def write_data_to_db(data_generators_sql_statements):
        with sqlite3.connect("college.db") as con:
            cur = con.cursor()
            for data_generator, sql_statement in data_generators_sql_statements:
                cur.executemany(sql_statement, data_generator)
            con.commit()


if __name__ == "__main__":
    GROUPS_NUMBER = 3
    TEACHERS_NUMBER = 3
    SUBJECTS_NUMBER = 3
    STUDENTS_NUMBER = 6
    MARKS_NUMBER = 5

    generator = DataGenerator(
        GROUPS_NUMBER, TEACHERS_NUMBER, SUBJECTS_NUMBER, STUDENTS_NUMBER, MARKS_NUMBER
    )

    groups_data_generator = generator.generate_groups_data()
    teachers_data_generator = generator.generate_teachers_data()
    subjects_data_generator = generator.generate_subjects_data()
    students_data_generator = generator.generate_students_data()
    grades_data_generator = generator.generate_grades_data()

    data_generators_sql_statements = [
        (groups_data_generator, "INSERT INTO groups (title) VALUES (?)"),
        (teachers_data_generator, "INSERT INTO teachers (name) VALUES (?)"),
        (subjects_data_generator, "INSERT INTO subjects (title, teacher_id) VALUES (?, ?)"),
        (students_data_generator, "INSERT INTO students (name, group_id) VALUES (?, ?)"),
        (grades_data_generator, "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)")
    ]

    DataExporter.write_data_to_db(data_generators_sql_statements)
