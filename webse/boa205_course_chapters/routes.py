from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

boa205_course_chapters= Blueprint('boa205_course_chapters', __name__)

#Chapter 1
@boa205_course_chapters.route('/boa205_course/kapittel1', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch1():
    return render_template('boa205_course/chapters/ch_template.html', title='BØA205 Økonomistyring, kapittel 1')

