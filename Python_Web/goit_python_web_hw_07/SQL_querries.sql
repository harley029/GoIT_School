-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT s.fullname AS StudentName, ROUND(AVG(g.grade),2) AS AverageGrade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
GROUP BY s.id
ORDER BY AverageGrade DESC
LIMIT 5;

-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.fullname AS StudentName, AVG(g.grade) AS AverageGrade, subj.name AS SubjectTitle
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS subj ON g.subjects_id = subj.id
WHERE g.subjects_id = 1 -- Замість знаку питання вкажіть ідентифікатор певного предмета
GROUP BY s.id
ORDER BY AverageGrade DESC
LIMIT 1;

-- Знайти середній бал у групах з певного предмета.
SELECT groups.name AS GoupTitle, subjects.name AS SubjectTitle, ROUND(AVG(grades.grade),2) AS average_grade
FROM groups
JOIN students ON students.group_id = groups.id
JOIN grades ON grades.student_id = students.id
JOIN subjects ON subjects.id = grades.subjects_id
WHERE subjects.id = 3
GROUP BY groups.name, subjects.name;

-- Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT ROUND(AVG(grades.grade),2) AS average_grade
FROM grades;

-- Знайти які курси читає певний викладач.
SELECT t.fullname AS TeacherName, s.name AS SubjectTitle
FROM teachers as t
JOIN subjects AS s ON s.teacher_id = t.id 
WHERE t.id = 1;

-- Знайти список студентів у певній групі.
SELECT students.fullname, groups.name 
FROM students
JOIN groups ON students.group_id = groups.id 
WHERE students.group_id = 2;

-- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT students.fullname, grades.grade, subjects.name, groups.name 
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subjects_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE subjects.id = 1 AND groups.id = 2;

-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT teachers.fullname, ROUND(AVG(grades.grade), 2) AS average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subjects_id
GROUP BY teachers.fullname;

-- Знайти список курсів, які відвідує студент.
SELECT DISTINCT subjects.name, students.fullname 
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subjects_id = subjects.id
WHERE students.id = 6;

-- Список курсів, які певному студенту читає певний викладач.
SELECT DISTINCT subjects.name AS Subject_title, students.fullname AS Student_name, teachers.fullname AS Teacher_name 
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subjects_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 1 AND teachers.id = 1;
  
-- Середній бал, який певний викладач ставить певному студентові.
SELECT teachers.fullname AS teacher_name, students.fullname AS student_name, ROUND(AVG(grades.grade),2) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subjects_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 3
GROUP BY teachers.fullname;
