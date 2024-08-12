import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt, DBVAR
from webse.models import  Moduls
from flask_login import login_user, current_user, logout_user, login_required


se_course_statistics = Blueprint('se_course_statistics', __name__)

##################################
####   Block 11. Statistics   ####
##################################

@se_course_statistics.route('/sustainable_energy_web/statistics', methods=['GET', 'POST'])
@login_required
def statistics_main():
    return render_template('se_course/statistics/statistics.html')

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch1', methods=['GET', 'POST'])
@login_required
def statistics_se_ch1():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Chapter 1. Frame'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Chapter 1. Frame'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Chapter 1. Frame'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()
    
    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch1.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1 =correct_q1, incorrect_q1=incorrect_q1, correct_q2 =correct_q2, incorrect_q2=incorrect_q2)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch2', methods=['GET', 'POST'])
@login_required
def statistics_se_ch2():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()
    
    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    
    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()


    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch2.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1, correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3, correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5, correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7, correct_q8=correct_q8, incorrect_q8=incorrect_q8)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch3', methods=['GET', 'POST'])
@login_required
def statistics_se_ch3():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch3.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1, correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3, correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5, correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7, correct_q8=correct_q8, incorrect_q8=incorrect_q8,
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch4', methods=['GET', 'POST'])
@login_required
def statistics_se_ch4():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch4.html', entries=entries, correct=correct, incorrect=incorrect,
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

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch5', methods=['GET', 'POST'])
@login_required
def statistics_se_ch5():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch5.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7,
                           correct_q8=correct_q8, incorrect_q8=incorrect_q8,
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9,
                           correct_q10=correct_q10, incorrect_q10=incorrect_q10,
                           correct_q11=correct_q11, incorrect_q11=incorrect_q11,
                           correct_q12=correct_q12, incorrect_q12=incorrect_q12)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch6', methods=['GET', 'POST'])
@login_required
def statistics_se_ch6():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch6.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7,
                           correct_q8=correct_q8, incorrect_q8=incorrect_q8,
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9,
                           correct_q10=correct_q10, incorrect_q10=incorrect_q10,
                           correct_q11=correct_q11, incorrect_q11=incorrect_q11,
                           correct_q12=correct_q12, incorrect_q12=incorrect_q12)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch7', methods=['GET', 'POST'])
@login_required
def statistics_se_ch7():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch7.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7,
                           correct_q8=correct_q8, incorrect_q8=incorrect_q8,
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9,
                           correct_q10=correct_q10, incorrect_q10=incorrect_q10,
                           correct_q11=correct_q11, incorrect_q11=incorrect_q11,
                           correct_q12=correct_q12, incorrect_q12=incorrect_q12)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch8', methods=['GET', 'POST'])
@login_required
def statistics_se_ch8():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8.  Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch8.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7,
                           correct_q8=correct_q8, incorrect_q8=incorrect_q8,
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9,
                           correct_q10=correct_q10, incorrect_q10=incorrect_q10,
                           correct_q11=correct_q11, incorrect_q11=incorrect_q11,
                           correct_q12=correct_q12, incorrect_q12=incorrect_q12)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch9', methods=['GET', 'POST'])
@login_required
def statistics_se_ch9():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'ch9.  Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch9.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7,
                           correct_q8=correct_q8, incorrect_q8=incorrect_q8,
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9,
                           correct_q10=correct_q10, incorrect_q10=incorrect_q10,
                           correct_q11=correct_q11, incorrect_q11=incorrect_q11,
                           correct_q12=correct_q12, incorrect_q12=incorrect_q12)

@se_course_statistics.route('/sustainable_energy_web/statistics/se_ch10', methods=['GET', 'POST'])
@login_required
def statistics_se_ch10():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'ch10.  Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q11 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q12 = Moduls.query.filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('Your answer has been submitted!', 'success')
    return render_template('se_course/statistics/statistics_se_ch10.html', entries=entries, correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           correct_q7=correct_q7, incorrect_q7=incorrect_q7,
                           correct_q8=correct_q8, incorrect_q8=incorrect_q8,
                           correct_q9=correct_q9, incorrect_q9=incorrect_q9,
                           correct_q10=correct_q10, incorrect_q10=incorrect_q10,
                           correct_q11=correct_q11, incorrect_q11=incorrect_q11,
                           correct_q12=correct_q12, incorrect_q12=incorrect_q12)
