class StudentController:
    def __init__(self, model):
        self.model = model

    def create_student(self, data):
        student_id = self.model.create_student(data['FirstName'], data['Surname'])
        return {"message": "Student created successfully!", "StudentID": student_id}, 201

    def add_marks(self, data):
        student_id = self.model.create_student(data['FirstName'], data['Surname'])
        self.model.add_marks(student_id, data['marks'])
        return {"message": "Marks added successfully!", "StudentID": student_id}, 201

    def add_student_with_marks(self, data):
        student_id = self.model.create_student(data['FirstName'], data['Surname'])
        self.model.add_student_marks(student_id, data['Marks'])
        return {"message": "Student and marks added successfully!", "StudentID": student_id}, 201