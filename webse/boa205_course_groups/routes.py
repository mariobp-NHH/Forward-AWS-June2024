from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
import random

boa205_course_groups= Blueprint('boa205_course_groups', __name__)

@boa205_course_groups.route('/boa205_course/grupper', methods=['GET', 'POST'])
@login_required
def boa205_course_groups_home():
    import random
    n = 10
    x = random.randint(1, n) 
    return render_template('boa205_course/groups/groups.html', title='BØA205 Økonomistyring, grupper',
        random_number=x)
