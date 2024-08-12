from flask import render_template, url_for, Blueprint, request
from webse import application, db, bcrypt
sbm_course_students_apps= Blueprint('sbm_course_students_apps', __name__)

@sbm_course_students_apps.route('/sustainable_business_models_course/students_apps')
def sbm_course_students_apps_home():
    return render_template('sbm_course/sbm_students_apps/sbm_students_apps_home.html', title='Sustainable Business Models Course, Students Apps')
  
  
