import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt
from webse.models import AnnouncementSE
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
se_course= Blueprint('se_course', __name__)


###########################
####   Block 0. Home   ####
###########################
@se_course.route('/sustainable_energy_course')
def se_course_home():
    page = request.args.get('page', 1, type=int)
    announcements = AnnouncementSE.query.order_by(AnnouncementSE.date_posted.desc()).paginate(page=page, per_page=1)
    return render_template('se_course/home.html', announcements=announcements, title='SE Course - Home',func=read_image)


###############################
####   Block 8. Teachers   ####
###############################
@se_course.route('/sustainable_energy_course/teachers')
def se_course_teachers():
	return render_template('se_course/teachers.html', title='SE Course - Teachers')