import sqlite3

connect = sqlite3.connect("school.db")
cursor = connect.cursor()

cursor.execute('''
       CREATE TABLE IF NOT EXISTS students(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(50)
    )       
''')

cursor.execute('''
       CREATE TABLE IF NOT EXISTS grades(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           subject TEXT,
           scores INTEGER,
           student_id INTEGER,
           FOREIGN KEY (student_id) REFERENCES students(id)
    )     
''')
connect.commit()

def create_student(name):
    cursor.execute('INSERT INTO students(name) VALUES(?)', (name,))
    connect.commit()
    print(f"Ученик добавлен {name}!")

def create_grades(student_id, subject_name, scores):
    cursor.execute('INSERT INTO grades(student_id, subject, scores) VALUES(?, ?, ?)',
                   (student_id, subject_name, scores))
    connect.commit()
    print(f"Оценка выставлена {scores}!")

# create_student("Lynette")
# create_student("Gabriel")
# create_student("Bree")
# create_student("Susan")
# create_grades(1, "Math", 5)
# create_grades(2, "Biology", 3)
# create_grades(3, "Literature", 5)
# create_grades(4, "Physics", 2)


def get_students_grades():
    cursor.execute('''
         SELECT students.name, grades.subject, grades.scores
         FROM students LEFT JOIN grades ON students.id = grades.student_id
     ''')
    students = cursor.fetchall()
    for i in students:
        print(f"NAME: {i[0]} SUBJECT: {i[1]}, SCORES: {i[2]}")

# get_students_grades()

def get_max_grade():
    cursor.execute('''
    SELECT MAX(scores) FROM grades
    ''')
    grades = cursor.fetchone()
    print(grades)

# get_max_grade()

def get_average_grade():
    cursor.execute('''
    SELECT AVG(scores) FROM grades    
    ''')
    grades =  cursor.fetchone()
    print(grades)

# get_average_grade()

def get_min_grade():
    cursor.execute('''
    SELECT MIN(scores) FROM grades    
    ''')
    grades =  cursor.fetchone()
    print(grades)

# get_min_grade()

def get_student_records():
    cursor.execute('''
    SELECT student_id, COUNT(*) 
    FROM grades
    GROUP BY student_id    
    ''')
    students = cursor.fetchall()
    print(students)
# get_student_records()

def get_literature_student():
    cursor.execute('''
    SELECT name 
    FROM students
    WHERE id IN (
        SELECT student_id FROM grades
        WHERE subject = 'Literature'
    )
    ''')

    students = cursor.fetchall()
    print(students)
get_literature_student()

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT
            students.name,
            grades.subject,
            grades.scores
        FROM students
        LEFT JOIN grades ON students.id = grades.student_id    
    ''')
    connect.commit()
create_my_view()


def get_my_view():
    cursor.execute('SELECT * FROM my_view')
    students = cursor.fetchall()
    print(students)
get_my_view()