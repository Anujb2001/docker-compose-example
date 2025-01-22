from flask import Flask
from app.routes.students import student_bp

def create_app():
    app = Flask(__name__)
    
    # Configuration can be loaded here
    app.config.from_object('config')
    
    app.register_blueprint(student_bp)

    return app

app = create_app()