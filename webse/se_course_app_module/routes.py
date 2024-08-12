import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

se_course_app_module = Blueprint('se_course_app_module', __name__)

#################################
####   Block 9. App Module   ####
#################################
# App web
@se_course_app_module.route('/sustainable_energy_course/app_web')
@login_required
def app_web():
	return render_template('se_course/app web/app_web.html', title='App Web')

# App Module, Chapter 1.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch1', methods=['GET', 'POST'])
@login_required
def app_web_ch1():
    return render_template('se_course/app web/ch1/app_web_ch1.html', title='App Web - Ch1')

# App Module, Chapter 2.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch2', methods=['GET', 'POST'])
@login_required
def app_web_ch2():
    return render_template('se_course/app web/ch2/app_web_ch2.html', title='App Web - Ch2')

# App Module, Chapter 3.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch3', methods=['GET', 'POST'])
@login_required
def app_web_ch3():
    return render_template('se_course/app web/ch3/app_web_ch3.html', title='App Web - Ch3')

# App Module, Chapter 4.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch4', methods=['GET', 'POST'])
@login_required
def app_web_ch4():
    return render_template('se_course/app web/ch4/app_web_ch4.html', title='App Web - Ch4')

# App Module, Chapter 5.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch5', methods=['GET', 'POST'])
@login_required
def app_web_ch5():
    return render_template('se_course/app web/ch5/app_web_ch5.html', title='App Web - Ch5')

# App Module, Chapter 6.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch6', methods=['GET', 'POST'])
@login_required
def app_web_ch6():
    return render_template('se_course/app web/ch6/app_web_ch6.html', title='App Web - Ch6')

# App Module, Chapter 7.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch7', methods=['GET', 'POST'])
@login_required
def app_web_ch7():
    return render_template('se_course/app web/ch7/app_web_ch7.html', title='App Web - Ch7')

# App Module, Chapter 8.
@se_course_app_module.route('/sustainable_energy_course/app_web/ch8', methods=['GET', 'POST'])
@login_required
def app_web_ch8():
    return render_template('se_course/app web/ch8/app_web_ch8.html', title='App Web - Ch8')

