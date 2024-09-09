"""This script fills in the genereted (faked) data into the database"""

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

    def _generate_groups_data(self):
        for _ in range(self.grp_num):
            yield (self.fake.postcode(),)

    def _generate_teachers_data(self):
        for _ in range(self.teach_num):
            yield (self.fake.full_name(),)

    def _generate_subjects_data(self):
        for _ in range(self.subj_num):
            yield (self.fake.job(), randint(1, self.teach_num))

    def _generate_students_data(self):
        for _ in range(self.stud_num):
            yield (self.fake.full_name(), randint(1, self.grp_num))

    def _generate_grades_data(self):
        for student in range(1, self.stud_num + 1):
            for subject in range(1, self.subj_num + 1):
                for _ in range(self.mark_num):
                    grade_date = f"2024-{randint(1,12):02d}-{randint(10, 28):02d}"
                    grade = randint(6, 12)
                    yield (student, subject, grade, grade_date)

    def export_groups_data(self):
        """Експортує дані про групи до бази даних."""
        groups_data_generator = self._generate_groups_data()
        DataExporter.write_groups_data_to_db(groups_data_generator)

    def export_teachers_data(self):
        """Експортує дані про викладачів до бази даних."""
        teachers_data_generator = self._generate_teachers_data()
        DataExporter.write_teachers_data_to_db(teachers_data_generator)

    def export_subjects_data(self):
        """Експортує дані про предмети до бази даних."""
        subjects_data_generator = self._generate_subjects_data()
        DataExporter.write_subjects_data_to_db(subjects_data_generator)

    def export_students_data(self):
        """Експортує дані про студентів до бази даних."""
        students_data_generator = self._generate_students_data()
        DataExporter.write_students_data_to_db(students_data_generator)

    def export_grades_data(self):
        """Експортує дані про оцінки до бази даних."""
        grades_data_generator = self._generate_grades_data()
        DataExporter.write_grades_data_to_db(grades_data_generator)


class DataExporter:

    @staticmethod
    def write_data_to_db(data_generator, sql_statement):
        """Записує дані в базу даних за допомогою зазначеного SQL-запиту."""
        with sqlite3.connect("college.db") as con:
            cur = con.cursor()
            cur.executemany(sql_statement, data_generator)
            con.commit()

    @staticmethod
    def write_groups_data_to_db(groups_data):
        """Записує дані про групи у базу даних."""
        sql_statement = "INSERT INTO groups (title) VALUES (?)"
        DataExporter.write_data_to_db(groups_data, sql_statement)

    @staticmethod
    def write_teachers_data_to_db(teachers_data):
        """Записує дані про викладачів у базу даних."""
        sql_statement = "INSERT INTO teachers (name) VALUES (?)"
        DataExporter.write_data_to_db(teachers_data, sql_statement)

    @staticmethod
    def write_subjects_data_to_db(subjects_data):
        """Записує дані про предмети у базу даних."""
        sql_statement = "INSERT INTO subjects (title, teacher_id) VALUES (?, ?)"
        DataExporter.write_data_to_db(subjects_data, sql_statement)

    @staticmethod
    def write_students_data_to_db(students_data):
        """Записує дані про студентів у базу даних."""
        sql_statement = "INSERT INTO students (name, group_id) VALUES (?, ?)"
        DataExporter.write_data_to_db(students_data, sql_statement)

    @staticmethod
    def write_grades_data_to_db(grades_data):
        """Записує дані про оцінки у базу даних."""
        sql_statement = "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)"
        DataExporter.write_data_to_db(grades_data, sql_statement)


if __name__ == "__main__":

    gr = DataGenetator(
        GROUPS_NUMBER, TEACHERS_NUMBER, SUBJECTS_NUMBER, STUDENTS_NUMBER, MARKS_NUMBER
    )
    gr.export_groups_data()
    gr.export_teachers_data()
    gr.export_subjects_data()
    gr.export_students_data()
    gr.export_grades_data()