'''This script presents some querries to SQLite databas'''
import sqlite3
from time import sleep


def execute_query(sql_query: str) -> list:
    '''Execution of a query'''
    with sqlite3.connect("college.db") as con:
        cur = con.cursor()
        cur.execute(sql_query)
        return cur.fetchall()

def query(title:str, sql_query: str):
    '''The function calls for a query and returns a result of it'''
    print('\n', title)
    sleep(2)
    return execute_query(sql_query)

if __name__ == '__main__':

    TITLE = 'Знайти 5 студентів із найбільшим середнім балом з усіх предметів.'
    SQL = """
    SELECT s.name AS StudentName, ROUND(AVG(g.grade),2) AS AverageGrade
    FROM students AS s
    JOIN grades AS g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY AverageGrade DESC
    LIMIT 5;
    """
    print(query(TITLE, SQL))


    TITLE = "Знайти студента із найвищим середнім балом з певного предмета."
    SQL = """
    SELECT s.name AS StudentName, AVG(g.grade) AS AverageGrade, subj.title AS SubjectTitle
    FROM students AS s
    JOIN grades AS g ON s.id = g.student_id
    JOIN subjects AS subj ON g.subject_id = subj.id
    WHERE g.subject_id = 1 -- Замість знаку питання вкажіть ідентифікатор певного предмета
    GROUP BY s.id
    ORDER BY AverageGrade DESC
    LIMIT 1;
    """
    print(query(TITLE, SQL))


    TITLE = "Знайти середній бал у групах з певного предмета."
    SQL = """
    SELECT groups.title AS GoupTitle, subjects.title AS SubjectTitle, ROUND(AVG(grades.grade),2) AS average_grade
    FROM groups
    JOIN students ON students.group_id = groups.id
    JOIN grades ON grades.student_id = students.id
    JOIN subjects ON subjects.id = grades.subject_id
    WHERE subjects.id = 3
    GROUP BY groups.title, subjects.title;
    """
    print(query(TITLE, SQL))


    TITLE = "Знайти середній бал на потоці (по всій таблиці оцінок)."
    SQL = """
    SELECT ROUND(AVG(grades.grade),2) AS average_grade
    FROM grades;
    """
    print(query(TITLE, SQL))

    TITLE = "Знайти які курси читає певний викладач."
    SQL = """
    SELECT t.name AS TeacherName, s.title AS SubjectTitle
    FROM teachers as t
    JOIN subjects AS s ON s.teacher_id = t.id 
    WHERE t.id = 1;
    """
    print(query(TITLE, SQL))


    TITLE = "Знайти список студентів у певній групі."
    SQL = """
    SELECT students.name, groups.title 
    FROM students
    JOIN groups ON students.group_id = groups.id 
    WHERE students.group_id = 2;
    """
    print(query(TITLE, SQL))


    TITLE = "Знайти оцінки студентів у окремій групі з певного предмета."
    SQL = """
    SELECT students.name, grades.grade, subjects.title, groups.title 
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    JOIN groups ON students.group_id = groups.id
    WHERE subjects.id = 1 AND groups.id = 2;
    """
    print(query(TITLE, SQL))


    TITLE = "Знайти середній бал, який ставить певний викладач зі своїх предметів."
    SQL = """
    SELECT teachers.name, ROUND(AVG(grades.grade), 2) AS average_grade
    FROM teachers
    JOIN subjects ON teachers.id = subjects.teacher_id
    JOIN grades ON subjects.id = grades.subject_id
    GROUP BY teachers.name;
    """
    print(query(TITLE, SQL))


    TITLE = "Знайти список курсів, які відвідує студент."
    SQL = """
    SELECT DISTINCT subjects.title, students.name 
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE students.id = 6;
    """
    print(query(TITLE, SQL))


    TITLE = "Список курсів, які певному студенту читає певний викладач."
    SQL = """
    SELECT DISTINCT subjects.title AS Subject_title, students.name AS Student_name, teachers.name AS Teacher_name 
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE students.id = 1 AND teachers.id = 1;
    """
    print(query(TITLE, SQL))


    TITLE = "Середній бал, який певний викладач ставить певному студентові."
    SQL = """
    SELECT teachers.name AS teacher_name, students.name AS student_name, ROUND(AVG(grades.grade),2) AS average_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE students.id = 3
    GROUP BY teachers.name;
    """
    print(query(TITLE, SQL))