# Flask MVC Application

This is a Flask MVC application designed to manage student records. The application follows the Model-View-Controller (MVC) design pattern, separating concerns for better organization and maintainability.

## Project Structure

```
flask-mvc-app
├── app
│   ├── __init__.py          # Initializes the Flask application and sets up routes
│   ├── controllers           # Contains request handling logic
│   │   ├── __init__.py      # Initializes the controllers package
│   │   └── student_controller.py  # Handles student-related requests
│   ├── models                # Contains data models and database interactions
│   │   ├── __init__.py      # Initializes the models package
│   │   └── student_model.py  # Manages student database operations
│   ├── views                 # Contains response rendering logic
│   │   ├── __init__.py      # Initializes the views package
│   │   └── student_view.py   # Renders responses for student-related requests
├── config.py                 # Configuration settings for the application
├── run.py                    # Entry point for running the Flask application
└── README.md                 # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd flask-mvc-app
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python run.py
```

The application will start on `http://localhost:5000`.

## API Endpoints

- `POST /create_student`: Create a new student record.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

{ Firstname : "Amit", Surname: "Kumar", 
Marks : [ {subject: "Maths", Marks: 90 }, 
          { subject: "English", Marks: 70 }, 
          { subject: "Science", Marks: 88 } 
          ] 
}