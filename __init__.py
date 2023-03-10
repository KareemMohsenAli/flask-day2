from flask import  Flask
from flask_migrate import Migrate
from  app.models import  db
from app.config import  projectConfig as AppConfig  
from app.models import Student,Department
def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name] 
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config 
    app.config['SECRET_KEY'] = current_config.SECRET_KEY
    app.config.from_object(current_config)
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    
    from app.students.views import students_index, student_info, student_delete
    from app.students.errors import page_not_found
    
    app.register_error_handler(404, page_not_found) 
    app.add_url_rule('/students', view_func=students_index)
    app.add_url_rule('/students/<id>', view_func=student_info)
    app.add_url_rule('/students/<id>/delete', view_func=student_delete)
    return  app


