from flask import render_template,redirect, url_for
from app.models import Department
# from app.departments import  departments_blueprint

# @departments_blueprint.route('/')
def department_index():
    departments = Department.get_all_departments()
    return render_template('departments/index.html',departments=departments )



def department_show(id):
    department = Department.query.get_or_404(id)
    return render_template('departments/show.html', department=department)


def department_delete(id):
    department = Department.query.get_or_404(id)
    res =department.delete_object()
    if res :
        return redirect(url_for("departments_all"))