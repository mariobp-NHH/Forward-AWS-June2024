from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

gd_course_students_apps= Blueprint('gd_course_students_apps', __name__)

@gd_course_students_apps.route('/green_digitalization_course/gd_students_apps')
def gd_students_apps_home(): 
    return render_template('gd_course/students_apps/gd_students_apps_home.html', title='Students Apps Home')

@gd_course_students_apps.route('/green_digitalization_course/gd_students_apps/2024')
def gd_students_apps_home_2024(): 
    return render_template('gd_course/students_apps/gd_students_apps_home_2024.html', title='Students Apps Home 2024')

@gd_course_students_apps.route('/green_digitalization_course/gd_students_apps/2023')
def gd_students_apps_home_2023(): 
    return render_template('gd_course/students_apps/gd_students_apps_home_2023.html', title='Students Apps Home 2023')



