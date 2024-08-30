from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

es_course_chapters= Blueprint('es_course_chapters', __name__)

#Chapter 1
@es_course_chapters.route('/economías_del_español_curso/capítulo1', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch1(): 
    return render_template('es_course/chapters/ch1.html', title='Economías del Español Curso, ch1')

#Chapter 2
@es_course_chapters.route('/economías_del_español_curso/capítulo2', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch2():       
    return render_template('es_course/chapters/ch2.html', title='Economías del Español Curso, ch2')

#Chapter 3
@es_course_chapters.route('/economías_del_español_curso/capítulo3', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch3():     
    return render_template('es_course/chapters/ch3.html', title='Economías del Español Curso, ch3')

#Chapter 4
@es_course_chapters.route('/economías_del_español_curso/capítulo4', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch4(): 
    return render_template('es_course/chapters/ch4.html', title='Economías del Español Curso, ch4') 


#Chapter 5
@es_course_chapters.route('/economías_del_español_curso/capítulo5', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch5(): 
    return render_template('es_course/chapters/ch5.html', title='Economías del Español Curso, ch5')   


#Chapter 6
@es_course_chapters.route('/economías_del_español_curso/capítulo6', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch6(): 
    return render_template('es_course/chapters/ch6.html', title='Economías del Español Curso, ch6') 

#Light Day Conference
@es_course_chapters.route('/economías_del_español_curso/light_day_conference', methods=['GET', 'POST'])
@login_required
def es_course_chapters_light_day_conference(): 
    return render_template('es_course/chapters/light_day.html', title='Economías del Español Curso, conference') 

