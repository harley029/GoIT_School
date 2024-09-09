from random import randint
import sqlite3

import faker

GROUPS_NUMBER = 3
TEACHERS_NUMBER = 3
SUBJECTS_NUMBER = 3
STUDENTS_NUMBER = 6
MARKS_NUMBER = 5


class DataGenetator:
    def __init__(self, grp_num, teach_num, subj_num, stud_num, mark_num):
        self.grp_num = grp_num
        self.teach_num = teach_num
        self.subj_num = subj_num
        self.stud_num = stud_num
        self.mark_num = mark_num
        self.fake = faker.Faker("uk-UA")

    def _generate_data(self, generator, *args):
        for _ in range(generator):
            yield args

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

    def export_data(self, generator, sql_statement):
        with sqlite3.connect("college.db") as con:
            cur = con.cursor()
            cur.executemany(sql_statement, generator)
            con.commit()

    def export_groups_data(self):
        groups_data_generator = self.generate_groups_data()
        sql_statement = "INSERT INTO groups (title) VALUES (?)"
        self.export_data(groups_data_generator, sql_statement)

    def export_teachers_data(self):
        teachers_data_generator = self.generate_teachers_data()
        sql_statement = "INSERT INTO teachers (name) VALUES (?)"
        self.export_data(teachers_data_generator, sql_statement)

    def export_subjects_data(self):
        subjects_data_generator = self.generate_subjects_data()
        sql_statement = "INSERT INTO subjects (title, teacher_id) VALUES (?, ?)"
        self.export_data(subjects_data_generator, sql_statement)

    def export_students_data(self):
        students_data_generator = self.generate_students_data()
        sql_statement = "INSERT INTO students (name, group_id) VALUES (?, ?)"
        self.export_data(students_data_generator, sql_statement)

    def export_grades_data(self):
        grades_data_generator = self.generate_grades_data()
        sql_statement = "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)"
        self.export_data(grades_data_generator, sql_statement)

if __name__ == "__main__":
    gr = DataGenetator(
        GROUPS_NUMBER, TEACHERS_NUMBER, SUBJECTS_NUMBER, STUDENTS_NUMBER, MARKS_NUMBER
    )
    gr.export_groups_data()
    gr.export_teachers_data()
    gr.export_subjects_data()
    gr.export_students_data()
    gr.export_grades_data()