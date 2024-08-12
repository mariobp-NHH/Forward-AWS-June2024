from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD
from flask_login import login_user, current_user, logout_user, login_required

es_course_students_apps= Blueprint('es_course_students_apps', __name__)

@es_course_students_apps.route('/economías_del_español_curso/es_students_apps')
def es_students_apps_home(): 
    return render_template('es_course/students_apps/es_students_apps_home.html', title='Students Apps Home')

@es_course_students_apps.route('/economías_del_español_curso/es_students_apps/2024')
def es_students_apps_home_2024(): 
    return render_template('es_course/students_apps/es_students_apps_home_2024.html', title='Students Apps Home 2024')

@es_course_students_apps.route('/economías_del_español_curso/es_students_apps/2023')
def es_students_apps_home_2023(): 
    return render_template('es_course/students_apps/es_students_apps_home_2023.html', title='Students Apps Home 2023')
