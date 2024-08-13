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

@es_course_chapters.route('/economías_del_español_curso/capítulo3/box_sizing')
@login_required
def es_course_chapters_ch3_box_sizing():  
    return render_template('es_course/chapters/ch3_box_sizing.html', title='Economías del Español Curso, ch3, box-sizing')

@es_course_chapters.route('/economías_del_español_curso/capítulo3/block_inline')
@login_required
def es_course_chapters_ch3_block_inline():  
    return render_template('es_course/chapters/ch3_block_inline.html', title='Economías del Español Curso, ch3, block-inline')

@es_course_chapters.route('/economías_del_español_curso/capítulo3/display')
@login_required
def es_course_chapters_ch3_display():  
    return render_template('es_course/chapters/ch3_display.html', title='Economías del Español Curso, ch3, display')

@es_course_chapters.route('/economías_del_español_curso/capítulo3/css_flex_container')
@login_required
def es_course_chapters_ch3_css_flex_container():  
    return render_template('es_course/chapters/ch3_css_flex_container.html', title='Economías del Español Curso, ch3, css_flex_container')

@es_course_chapters.route('/economías_del_español_curso/capítulo3/css_flex_items')
@login_required
def es_course_chapters_ch3_css_flex_items():  
    return render_template('es_course/chapters/ch3_css_flex_items.html', title='Economías del Español Curso, ch3, css_flex_items')

@es_course_chapters.route('/economías_del_español_curso/capítulo3/media_query')
@login_required
def es_course_chapters_ch3_media_query():  
    return render_template('es_course/chapters/ch3_media_query.html', title='Economías del Español Curso, ch3, media_query')

@es_course_chapters.route('/economías_del_español_curso/capítulo3/week1')
@login_required
def es_course_chapters_ch3_week1():  
    return render_template('es_course/chapters/ch3_week1.html', title='Economías del Español Curso, ch3, week1')

@es_course_chapters.route('/economías_del_español_curso/capítulo3/week2')
@login_required
def es_course_chapters_ch3_week2():  
    return render_template('es_course/chapters/ch3_week2.html', title='Economías del Español Curso, ch3, week2')

#Chapter 4
@es_course_chapters.route('/economías_del_español_curso/capítulo4', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch4(): 
    return render_template('es_course/chapters/ch4.html', title='Economías del Español Curso, ch4') 

@es_course_chapters.route('/economías_del_español_curso/capítulo4/home1')
@login_required
def es_course_chapters_ch4_home1():  
    return render_template('es_course/chapters/ch4_home1.html', title='Economías del Español Curso, ch4, home1') 

@es_course_chapters.route('/economías_del_español_curso/capítulo4/methodology1')
@login_required
def es_course_chapters_ch4_methodology1():  
    return render_template('es_course/chapters/ch4_methodology1.html', title='Economías del Español Curso, ch4, methodology1') 

@es_course_chapters.route('/economías_del_español_curso/capítulo4/carbon_app1')
@login_required
def es_course_chapters_ch4_carbon_app1():  
    return render_template('es_course/chapters/ch4_carbon_app1.html', title='Economías del Español Curso, ch4, carbon_app1')  

@es_course_chapters.route('/economías_del_español_curso/capítulo4/home2')
@login_required
def es_course_chapters_ch4_home2():  
    return render_template('es_course/chapters/ch4_home2.html', title='Economías del Español Curso, ch4, home2') 

@es_course_chapters.route('/economías_del_español_curso/capítulo4/methodology2')
@login_required
def es_course_chapters_ch4_methodology2():  
    return render_template('es_course/chapters/ch4_methodology2.html', title='Economías del Español Curso, ch4, methodology2') 

@es_course_chapters.route('/economías_del_español_curso/capítulo4/carbon_app2')
@login_required
def es_course_chapters_ch4_carbon_app2():  
    return render_template('es_course/chapters/ch4_carbon_app2.html', title='Economías del Español Curso, ch4, carbon_app2')  

#Chapter 5
@es_course_chapters.route('/economías_del_español_curso/capítulo5', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch5(): 
    return render_template('es_course/chapters/ch5.html', title='Economías del Español Curso, ch5')   

@es_course_chapters.route('/economías_del_español_curso/capítulo5/home')
@login_required
def es_course_chapters_ch5_home():  
    return render_template('es_course/chapters/ch5_home.html', title='Economías del Español Curso, ch5, home') 

@es_course_chapters.route('/economías_del_español_curso/capítulo5/methodology')
@login_required
def es_course_chapters_ch5_methodology():  
    return render_template('es_course/chapters/ch5_methodology.html', title='Economías del Español Curso, ch5, methodology') 

@es_course_chapters.route('/economías_del_español_curso/capítulo5/carbon_app')
@login_required
def es_course_chapters_ch5_carbon_app():  
    return render_template('es_course/chapters/ch5_carbon_app.html', title='Economías del Español Curso, ch5, carbon_app') 

#Chapter 6
@es_course_chapters.route('/economías_del_español_curso/capítulo6', methods=['GET', 'POST'])
@login_required
def es_course_chapters_ch6(): 
    return render_template('es_course/chapters/ch6.html', title='Economías del Español Curso, ch6') 

