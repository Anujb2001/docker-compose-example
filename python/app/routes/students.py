from flask import Blueprint, request, jsonify
from app.models.db_model import get_db_connection

student_bp = Blueprint('student', __name__)

@student_bp.route('/')
def index():
    return "Welcome to the School API!"

from flask import Blueprint, request, jsonify
from app.models.db_model import StudentModel
from app.controllers.student_controller import StudentController

student_bp = Blueprint('student', __name__)
student_model = StudentModel()
student_controller = StudentController(student_model)

@student_bp.route('/')
def index():
    return "Welcome to the School API!"

@student_bp.route('/create_student', methods=['POST'])
def create_student():
    data = request.get_json()
    response = student_controller.create_student(data)
    return jsonify(response[0]), response[1]

@student_bp.route('/students', methods=['GET'])
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(students), 200

@student_bp.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM students WHERE StudentID = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(student), 200

@student_bp.route('/add_marks', methods=['POST'])
def add_marks():
    data = request.get_json()
    response = student_controller.add_marks(data)
    return jsonify(response[0]), response[1]

@student_bp.route('/add_student_with_marks', methods=['POST'])
def add_student_with_marks():
    data = request.get_json()
    response = student_controller.add_student_with_marks(data)
    return jsonify(response[0]), response[1]

# Update a single student
@student_bp.route('/update_student', methods=['PUT'])
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
@student_bp.route('/update_students', methods=['PUT'])
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
@student_bp.route('/delete_student', methods=['DELETE'])
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
@student_bp.route('/delete_students', methods=['DELETE'])
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
