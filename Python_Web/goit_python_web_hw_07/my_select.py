''' Alchemy SQL queriies '''
from time import sleep

from sqlalchemy import func, desc
from tabulate import tabulate

from config.db_session import session
from config.db_models import Student, Group, Grade, Teacher, Subject


def print_results(title, headers, rows):
    """
    Друкує заголовок, результати та дані у вигляді таблиці
    """
    print("\n", title)
    sleep(1)
    print(tabulate(rows, headers=headers, tablefmt="presto"))


def select_01():
    """
    SELECT
    s.fullname,
    ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = (
        session.query(
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label("average_grade")
        )
        .select_from(Student)
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("average_grade"))
        .limit(5)
        .all()
    )
    title="1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів."
    # Перетворення списку результатів на список кортежів для tabulate
    rows = [(*row,) for row in result]
    headers = ["Student fullname", "Average grade"]
    print_results(title, headers, rows)

def select_02(subject_id):
    """
    SELECT s.fullname AS StudentName, AVG(g.grade) AS AverageGrade, subj.name AS SubjectTitle
    FROM students AS s
    JOIN grades AS g ON s.id = g.student_id
    JOIN subjects AS subj ON g.subjects_id = subj.id
    WHERE g.subjects_id = 1 -- Замість знаку питання вкажіть ідентифікатор певного предмета
    GROUP BY s.id
    ORDER BY AverageGrade DESC
    LIMIT 1;
    """
    result = (
        session.query(
            Student.fullname.label("StudentName"),
            func.avg(Grade.grade).label("Average_grade"),
            Subject.name.label("SubjectTitle")
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .filter(Grade.subjects_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("Average_grade"))
        .limit(1)
        .first()
    )
    title="2. Знайти студента із найвищим середнім балом з певного предмета."
    rows = [[result.StudentName, result.Average_grade, result.SubjectTitle]]
    headers = ["StudentName", "AverageGrade", "SubjectTitle"]
    print_results(title, headers, rows)

def select_03(subject_id):
    """
    SELECT groups.name AS GoupTitle, subjects.name AS SubjectTitle, 
           ROUND(AVG(grades.grade),2) AS Average_grade
    FROM groups
    JOIN students ON students.group_id = groups.id
    JOIN grades ON grades.student_id = students.id
    JOIN subjects ON subjects.id = grades.subjects_id
    WHERE subjects.id = 3
    GROUP BY groups.name, subjects.name;
    """
    result = (
        session.query(
            Group.name.label("GroupTitle"),
            Subject.name.label("SubjectTitle"),
            func.round(func.avg(Grade.grade), 2).label("Average_grade")
        )
        .select_from(Group)
        .join(Student)
        .join(Grade)
        .join(Subject)
        .filter(Grade.subjects_id == subject_id)
        .group_by(Group.name, Subject.name)
        .all()
    )
    title="3. Знайти середній бал у групах з певного предмета."
    rows = [(*row,) for row in result]
    headers = ["Group Title", "Subject Title", "Average grade"]
    print_results(title, headers, rows)

def select_04():
    """
    SELECT ROUND(AVG(grades.grade),2) AS Average_grade
    FROM grades;
    """
    result = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("Average_grade")
        )
        .select_from(Grade)
        .scalar()
    )
    title="4. Знайти середній бал на потоці (по всій таблиці оцінок)."
    rows = [[result]]
    headers = ["Average grade"]
    print_results(title, headers, rows)

def select_05(teacher_id):
    """
    SELECT t.fullname AS TeacherName, s.name AS SubjectTitle
    FROM teachers as t
    JOIN subjects AS s ON s.teacher_id = t.id 
    WHERE t.id = 1;
    """
    result = (
        session.query(
            Teacher.fullname.label("TeacherName"),
            Subject.name.label("SubjectTitle")
        )
        .select_from(Teacher)
        .join(Subject)
        .filter(Teacher.id == teacher_id)
        .first()
    )
    title="5. Знайти які курси читає певний викладач."
    rows = [result]
    headers = ["Teacher Name", "Subject Title"]
    print_results(title, headers, rows)

def select_06(group_id):
    """
    SELECT students.fullname, groups.name 
    FROM students
    JOIN groups ON students.group_id = groups.id 
    WHERE students.group_id = 2;
    """
    result = (
        session.query(
            Student.fullname,
            Group.name
        )
        .select_from(Student)
        .join(Group)
        .filter(Student.group_id == group_id)
        .all()
    )
    title="6. Знайти список студентів у певній групі."
    rows = [(*row,) for row in result]
    headers = ["Student fullname", "Group name"]
    print_results(title, headers, rows)

def select_07(subject_id, group_id):
    """
    SELECT students.fullname, grades.grade, subjects.name, groups.name 
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subjects_id = subjects.id
    JOIN groups ON students.group_id = groups.id
    WHERE subjects.id = 1 AND groups.id = 2;
    """
    result = (
        session.query(
            Student.fullname,
            Grade.grade,
            Subject.name,
            Group.name
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .join(Group)
        .filter(Subject.id == subject_id, Group.id == group_id)
        .all()
    )
    title="7. Знайти оцінки студентів у окремій групі з певного предмета."
    rows = [(*row,) for row in result]
    headers = ["Student fullname", "Grade", "Subject name", "Group name"]
    print_results(title, headers, rows)

def select_08():
    """
    SELECT teachers.fullname, ROUND(AVG(grades.grade), 2) AS Average_grade
    FROM teachers
    JOIN subjects ON teachers.id = subjects.teacher_id
    JOIN grades ON subjects.id = grades.subjects_id
    GROUP BY teachers.fullname;
    """
    result = (
        session.query(
            Teacher.fullname,
            func.round(func.avg(Grade.grade), 2).label("Average_grade")
        )
        .select_from(Teacher)
        .join(Subject)
        .join(Grade)
        .group_by(Teacher.fullname)
        .all()
    )
    title="8. Знайти середній бал, який ставить певний викладач зі своїх предметів."
    rows = [(*row,) for row in result]
    headers = ["Teacher fullname", "Average grade"]
    print_results(title, headers, rows)

def select_09(student_id):
    """
    SELECT DISTINCT subjects.name, students.fullname
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subjects_id = subjects.id
    WHERE students.id = 6;
    """
    result = (
        session.query(Subject.name, Student.fullname)
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .filter(Student.id == student_id)
        .group_by(Subject.name, Student.fullname)
        .all()
    )
    title="9. Знайти список курсів, які відвідує студент."
    rows = [(*row,) for row in result]
    headers = ["Subject name", "Student name"]
    print_results(title, headers, rows)


def select_10(student_id, teacher_id):
    """
    SELECT DISTINCT subjects.name AS Subject_title, students.fullname AS Student_name, 
           teachers.fullname AS Teacher_name
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subjects_id = subjects.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE students.id = 1 AND teachers.id = 1;
    """
    result = (
        session.query(
            Subject.name.label("Subject_title"),
            Student.fullname.label("Student_name"),
            Teacher.fullname.label("Teacher_name"),
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .join(Teacher)
        .filter(Student.id == student_id, Teacher.id == teacher_id)
        .group_by(Subject.name, Student.fullname, Teacher.fullname)
        .first()
    )
    title="10. Список курсів, які певному студенту читає певний викладач."
    rows = [result]
    headers = ["Subject title", "Student name", "Teacher name"]
    print_results(title, headers, rows)


def select_11(student_id):
    """
    SELECT teachers.fullname AS Teacher_name, students.fullname AS Student_name, 
           ROUND(AVG(grades.grade),2) AS Average_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subjects_id = subjects.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE students.id = 3
    GROUP BY teachers.fullname;
    """
    result = (
        session.query(
            Teacher.fullname.label("Teacher_name"),
            Student.fullname.label("Student_name"),
            func.round(func.avg(Grade.grade), 2).label("Average_grade")
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .join(Teacher)
        .filter(Student.id == student_id)
        .group_by(Teacher.fullname)
        .all()
    )
    title="11. Середній бал, який певний викладач ставить певному студентові."
    headers = ["Teacher Name", "Student Name", "Average Grade"]
    # rows = [(row.Teacher_name, row.Student_name, row.Average_grade) for row in result]
    # варіант, коли стовпчики вказуються прямо, як в запиті
    rows = [(*row,) for row in result]
    print_results(title, headers, rows)

if __name__ == "__main__":

    select_01()
    select_02(subject_id=1)
    select_03(subject_id=3)
    select_04()
    select_05(teacher_id=1)
    select_06(group_id=2)
    select_07(subject_id=1, group_id=2)
    select_08()
    select_09(student_id=6)
    select_10(student_id=1, teacher_id=1)
    select_11(student_id=3)
