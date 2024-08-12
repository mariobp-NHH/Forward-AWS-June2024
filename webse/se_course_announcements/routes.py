import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt
from webse.se_course_announcements.forms import AnnouncementForm
from webse.models import AnnouncementSE
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

se_course_announcements = Blueprint('se_course_announcements', __name__)

##################################
####   Block 2. Announcement   ###
###################################

@se_course_announcements.route("/sustainable_energy_course/announcement/new", methods=['GET', 'POST'])
@login_required
def new_announcement():
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement = AnnouncementSE(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(announcement)
        db.session.commit()
        flash('Your announcement has been created!', 'success')
        return redirect(url_for('se_course.se_course_home'))
    return render_template('se_course/announcement/create_announcement.html', title='New Announcement',
                           form=form, legend='New Announcement')

@se_course_announcements.route("/sustainable_energy_course/announcement/<int:announcement_id>")
def announcement(announcement_id):
    announcement = AnnouncementSE.query.get_or_404(announcement_id)
    return render_template('se_course/announcement/announcement.html', title=announcement.title, announcement=announcement,func=read_image)



@se_course_announcements.route("/sustainable_energy_course/announcement/<int:announcement_id>/update", methods=['GET', 'POST'])
@login_required
def update_announcement(announcement_id):
    announcement = AnnouncementSE.query.get_or_404(announcement_id)
    if announcement.author != current_user:
        abort(403)
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement.title = form.title.data
        announcement.content = form.content.data
        db.session.commit()
        flash('Your announcement has been updated!', 'success')
        return redirect(url_for('se_course.se_course_home', announcement_id=announcement.id))
    elif request.method == 'GET':
        form.title.data = announcement.title
        form.content.data = announcement.content
    return render_template('se_course/announcement/create_announcement.html', title='Update Announcement',
                           form=form, legend='Update Announcement')


@se_course_announcements.route("/sustainable_energy_course/announcement/<int:announcement_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_announcement(announcement_id):
    announcement = AnnouncementSE.query.get_or_404(int(announcement_id))
    if announcement.author != current_user:
        abort(403)
    db.session.delete(announcement)
    db.session.commit()
    flash('Your announcement has been deleted!', 'success')
    return redirect(url_for('se_course.se_course_home'))
