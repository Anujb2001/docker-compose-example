import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port="3306", database='db')
    print("DB connected")
    return connection

class StudentModel:
    def create_student(self, first_name, surname):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO students (FirstName, Surname) VALUES (%s, %s)"
        cursor.execute(query, (first_name, surname))
        connection.commit()
        student_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return student_id

    def add_marks(self, student_id, marks):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO marks (StudentID, Mark) VALUES (%s, %s)"
        for mark in marks:
            cursor.execute(query, (student_id, mark))
        connection.commit()
        cursor.close()
        connection.close()

    def add_student_marks(self, student_id, marks):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO marks (StudentID, Subject, Mark) VALUES (%s, %s, %s)"
        for mark in marks:
            cursor.execute(query, (student_id, mark['subject'], mark['Marks']))
        connection.commit()
        cursor.close()
        connection.close()