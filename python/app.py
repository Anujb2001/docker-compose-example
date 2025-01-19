from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
    print("DB connected")
    return connection

# Routes
@app.route('/')
def index():
    return "Welcome to the School API!"

# Create a single student
@app.route('/create_student', methods=['POST'])
def create_student():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO students (FirstName, Surname) VALUES (%s, %s)"
    cursor.execute(query, (data['FirstName'], data['Surname']))
    connection.commit()
    student_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return jsonify({"message": "Student created successfully!", "StudentID": student_id}), 201

# Create multiple students
@app.route('/create_students', methods=['POST'])
def create_students():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO students (FirstName, Surname) VALUES (%s, %s)"
    values = [(student['FirstName'], student['Surname']) for student in data]
    cursor.executemany(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Students created successfully!"}), 201

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(students), 200

# Get a specific student by ID
@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM students WHERE StudentID = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()
    if not student:
        return jsonify({"message": "Student not found."}), 404

    return jsonify(student), 200

# Update a single student
@app.route('/update_student', methods=['PUT'])
def update_student():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE students SET FirstName = %s, Surname = %s WHERE StudentID = %s"
    cursor.execute(query, (data['FirstName'], data['Surname'], data['StudentID']))
    connection.commit()
    cursor.close()
    connection.close()
    if cursor.rowcount == 0:
        return jsonify({"message": "Student not found."}), 404

    return jsonify({"message": "Student updated successfully!"}), 200

# Update multiple students
@app.route('/update_students', methods=['PUT'])
def update_students():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE students SET FirstName = %s, Surname = %s WHERE StudentID = %s"
    for student in data:
        cursor.execute(query, (student['FirstName'], student['Surname'], student['StudentID']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Students updated successfully!"}), 200

# Delete a single student
@app.route('/delete_student', methods=['DELETE'])
def delete_student():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM students WHERE StudentID = %s"
    cursor.execute(query, (data['StudentID'],))
    connection.commit()
    cursor.close()
    connection.close()
    if cursor.rowcount == 0:
        return jsonify({"message": "Student not found."}), 404

    return jsonify({"message": "Student deleted successfully!"}), 200

# Delete multiple students
@app.route('/delete_students', methods=['DELETE'])
def delete_students():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM students WHERE StudentID IN (%s)"
    student_ids = ', '.join(map(str, data['StudentIDs']))
    cursor.execute(query % student_ids)
    connection.commit()
    cursor.close()
    connection.close()
    if cursor.rowcount == 0:
        return jsonify({"message": "No students found to delete."}), 404

    return jsonify({"message": "Students deleted successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)