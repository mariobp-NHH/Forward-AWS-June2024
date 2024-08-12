import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt, DBVAR
from webse.models import  ModulsGD
from flask_login import login_user, current_user, logout_user, login_required


gd_course_statistics = Blueprint('gd_course_statistics', __name__)

##################################
####   Block 11. Statistics   ####
##################################

@gd_course_statistics.route('/green_digitalization_course/statistics', methods=['GET', 'POST'])
@login_required
def statistics():
    return render_template('gd_course/statistics/statistics.html')

@gd_course_statistics.route('/green_digitalization_course/statistics/ch1', methods=['GET', 'POST'])
@login_required
def statistics_ch1():
    entries = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.title_mo=='ch1'). \
        filter(ModulsGD.title_ch=='Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).all()

    incorrect = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==0). \
        filter(ModulsGD.title_mo=='ch1'). \
        filter(ModulsGD.title_ch=='Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==1). \
        filter(ModulsGD.title_mo=='ch1'). \
        filter(ModulsGD.title_ch=='Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch1'). \
        filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch1'). \
        filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch1'). \
        filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch1'). \
        filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch1'). \
        filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch1'). \
        filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    return render_template('gd_course/statistics/statistics_ch1.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3)


@gd_course_statistics.route('/green_digitalization_course/statistics/ch2', methods=['GET', 'POST'])
@login_required
def statistics_ch2():
    entries = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.title_mo=='ch2'). \
        filter(ModulsGD.title_ch=='Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).all()

    incorrect = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==0). \
        filter(ModulsGD.title_mo=='ch2'). \
        filter(ModulsGD.title_ch=='Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==1). \
        filter(ModulsGD.title_mo=='ch2'). \
        filter(ModulsGD.title_ch=='Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q4 = ModulsGD.query.filter(ModulsGD.question_num == 4). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q4 = ModulsGD.query.filter(ModulsGD.question_num == 4). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()    

    incorrect_q5 = ModulsGD.query.filter(ModulsGD.question_num == 5). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q5 = ModulsGD.query.filter(ModulsGD.question_num == 5). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()    

    incorrect_q6 = ModulsGD.query.filter(ModulsGD.question_num == 6). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q6 = ModulsGD.query.filter(ModulsGD.question_num == 6). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch2'). \
        filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()      

    return render_template('gd_course/statistics/statistics_ch2.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6)


@gd_course_statistics.route('/green_digitalization_course/statistics/ch3', methods=['GET', 'POST'])
@login_required
def statistics_ch3():
    entries = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.title_mo=='ch3'). \
        filter(ModulsGD.title_ch=='Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).all()

    incorrect = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==0). \
        filter(ModulsGD.title_mo=='ch3'). \
        filter(ModulsGD.title_ch=='Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==1). \
        filter(ModulsGD.title_mo=='ch3'). \
        filter(ModulsGD.title_ch=='Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q4 = ModulsGD.query.filter(ModulsGD.question_num == 4). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q4 = ModulsGD.query.filter(ModulsGD.question_num == 4). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()    

    incorrect_q5 = ModulsGD.query.filter(ModulsGD.question_num == 5). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q5 = ModulsGD.query.filter(ModulsGD.question_num == 5). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()    

    incorrect_q6 = ModulsGD.query.filter(ModulsGD.question_num == 6). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q6 = ModulsGD.query.filter(ModulsGD.question_num == 6). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count() 

    incorrect_q7 = ModulsGD.query.filter(ModulsGD.question_num == 7). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q7 = ModulsGD.query.filter(ModulsGD.question_num == 7). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count() 

    incorrect_q8 = ModulsGD.query.filter(ModulsGD.question_num == 8). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q8 = ModulsGD.query.filter(ModulsGD.question_num == 8). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count() 

    incorrect_q9 = ModulsGD.query.filter(ModulsGD.question_num == 9). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q9 = ModulsGD.query.filter(ModulsGD.question_num == 9). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count() 

    incorrect_q10 = ModulsGD.query.filter(ModulsGD.question_num == 10). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q10 = ModulsGD.query.filter(ModulsGD.question_num == 10). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'ch3'). \
        filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()     

    return render_template('gd_course/statistics/statistics_ch3.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7,
                           correct_q8=correct_q8, incorrect_q8=incorrect_q8, 
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9,
                           correct_q10=correct_q10, incorrect_q10=incorrect_q10)

