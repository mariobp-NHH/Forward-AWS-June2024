import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt
from webse.models import User, AnnouncementSE
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

se_course_users = Blueprint('se_course_users', __name__)

######################################
####   Block 1. User Information   ###
######################################
@se_course_users.route("/sustainable_energy_course/announcement/user/<string:username>")
def user_announcements(username):
    page = request.args.get('page', 1, type=int)
    userin = User.query.filter_by(username=username).first_or_404()
    announcements = AnnouncementSE.query.filter_by(author=userin)\
        .order_by(AnnouncementSE.date_posted.desc())\
        .paginate(page=page, per_page=4)
    return render_template('se_course/announcement/user_announcements.html', announcements=announcements, userpage=userin,func=read_image)
