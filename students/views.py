#1
from app.models import Student,db
#2
from flask import  render_template, redirect, url_for, request


from app.models import Student,db
from flask import  render_template, redirect, url_for, request
def students_index():
    students = Student.get_all_students()
    return render_template('students/index.html', students=students)


def student_info(id):
    student = Student.query.get_or_404(id)
    return render_template('students/show.html', student=student)


def student_delete(id):
    student = Student.query.get_or_404(id)
    res =student.delete_object()
    if res :
        return redirect(url_for("students_index"))

def validateInputs(requestdict: dict):
    errors = {}
    if not requestdict["name"]:
        errors["name"] = 'name required'

    ## check email exists before
    student = Student.query.filter_by(email=requestdict['email']).first()
    if student:
        errors["email"] = 'Email already exists'

    return errors
