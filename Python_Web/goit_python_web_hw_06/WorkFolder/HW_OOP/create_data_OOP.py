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

    def generate_groups_data(self): # +
        group_names = [self.fake.postcode() for _ in range(self.grp_num)]
        groups = []
        for group_name in group_names:
            groups.append((group_name,))
        return groups

    def generate_teachers_data(self): # +
        teacher_names = [self.fake.full_name() for _ in range(self.teach_num)]
        t_names = []
        for teacher_name in teacher_names:
            t_names.append((teacher_name,))
        return t_names

    def generate_subjects_data(self): # +
        subject_names = [self.fake.job() for _ in range(self.subj_num)]
        s_titles = []
        for subject_name in subject_names:
            s_titles.append((subject_name, randint(1, self.teach_num),))
        return s_titles

    def generate_students_data(self): # +
        students_names = [self.fake.full_name() for _ in range(self.stud_num)]
        s_names = []
        for student_name in students_names:
            s_names.append((student_name, randint(1, self.grp_num),))
        return s_names

    def generate_grades_data(self): # +
        grades = []
        for student in range(1, self.stud_num + 1):
            for subject in range(1, self.stud_num + 1):
                for _ in range(1, self.mark_num + 1):
                    grade_date = f"2024-{randint(1,12):02d}-{randint(10, 28):02d}"
                    grade = randint(1, 12)
                    grades.append((student, subject, grade, grade_date))
        return grades

class DataExporter:
    pass
def generate_data(
    groups_number, teachers_number, subjects_number, students_number, makrs_number
):
    fake = faker.Faker("uk-UA")
    group_names = [fake.postcode() for _ in range(groups_number)]
    teacher_names = [fake.full_name() for _ in range(teachers_number)]
    subject_names = [fake.job() for _ in range(subjects_number)]
    students_names = [fake.full_name() for _ in range(students_number)]
    grades = []
    for student in range(1, students_number + 1):
        for subject in range(1, subjects_number + 1):
            for _ in range(1, makrs_number + 1):
                grade_date = f"2024-{randint(1,12):02d}-{randint(10, 28):02d}"
                grade = randint(1, 12)
                grades.append((student, subject, grade, grade_date))
    return group_names, teacher_names, subject_names, students_names, grades


def prepare_data(group_names, teacher_names, subject_names, student_names):
    groups = []
    for group_name in group_names:
        groups.append((group_name,))
    t_names = []
    for teacher_name in teacher_names:
        t_names.append((teacher_name,))
    s_titles = []
    for subject_name in subject_names:
        s_titles.append(
            (
                subject_name,
                randint(1, TEACHERS_NUMBER),
            )
        )
    s_names = []
    for student_name in student_names:
        s_names.append(
            (
                student_name,
                randint(1, GROUPS_NUMBER),
            )
        )
    return groups, t_names, s_titles, s_names


def insert_data(group_names, teachers_names, subjects_names, students_names, grades):
    with sqlite3.connect("college.db") as con:
        cur = con.cursor()
        sql = """INSERT INTO groups (title) VALUES (?)"""
        cur.executemany(sql, group_names)

        sql = """INSERT INTO teachers (name) VALUES (?)"""
        cur.executemany(sql, teachers_names)

        sql = """INSERT INTO subjects (title, teacher_id) VALUES (?,?)"""
        cur.executemany(sql, subjects_names)

        sql = """INSERT INTO students (name, group_id) VALUES (?,?)"""
        cur.executemany(sql, students_names)

        sql = """INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?,?,?,?)"""
        cur.executemany(sql, grades)
        con.commit()
        cur.close()


if __name__ == "__main__":
    # # згенерувати данні для бази данних
    # group_names, teacher_names, subject_names, student_names, grades = [
    #     *generate_data(
    #         GROUPS_NUMBER,
    #         TEACHERS_NUMBER,
    #         SUBJECTS_NUMBER,
    #         STUDENTS_NUMBER,
    #         MARKS_NUMBER,
    #     )
    # ]
    # # підготовка данних до імпорту до бази даних
    # group_names1, teacher_names1, subject_names1, student_names1 = [
    #     *prepare_data(group_names, teacher_names, subject_names, student_names)
    # ]
    # # шьзщке данних до бази даних
    # insert_data(group_names1, teacher_names1, subject_names1, student_names1, grades)
    gr=DataGenetator(GROUPS_NUMBER, TEACHERS_NUMBER, SUBJECTS_NUMBER, STUDENTS_NUMBER, MARKS_NUMBER)
    print(gr.generate_groups_data())
    print(gr.generate_teachers_data())
    print(gr.generate_subjects_data())
    print(gr.generate_students_data())
    print(gr.generate_grades_data())
