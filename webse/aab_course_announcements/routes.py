from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, AnnouncementGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.aab_course_announcements.forms import AnnouncementForm

aab_course_announcements= Blueprint('aab_course_announcements', __name__)

@aab_course_announcements.route('/auditing_accounting_business_course/announcement/new', methods=['GET', 'POST'])
@login_required
def aab_course_announcements_new_announcement(): 
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement = AnnouncementGD(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(announcement)
        db.session.commit()
        flash('Your announcement has been created!', 'success')
        return redirect(url_for('aab_course.aab_course_home'))
    return render_template('aab_course/aab_announcements/aab_course_create_announcement.html', title='New announcement', form=form)

@aab_course_announcements.route("/auditing_accounting_business_course/announcement/<int:announcement_id>")
def announcement(announcement_id):
    announcement = AnnouncementGD.query.get_or_404(announcement_id)
    return render_template('aab_course/aab_announcements/aab_course_announcement.html', title=announcement.title, announcement=announcement, func=read_image)    

@aab_course_announcements.route("/auditing_accounting_business_course/announcement/<int:announcement_id>/update", methods=['GET', 'POST'])
@login_required
def update_announcement(announcement_id):
    announcement = AnnouncementGD.query.get_or_404(announcement_id)
    if announcement.author != current_user:
        abort(403)
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement.title = form.title.data
        announcement.content = form.content.data
        db.session.commit()
        flash('Your announcement has been updated!', 'success')
        return redirect(url_for('aab_course.aab_course_home'))
    elif request.method == 'GET':
        form.title.data = announcement.title
        form.content.data = announcement.content
    return render_template('aab_course/aab_announcements/aab_course_create_announcement.html', title='Update announcement',
                           form=form, legend='Update announcement')    

@aab_course_announcements.route("/auditing_accounting_business_course/announcement/<int:announcement_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_announcement(announcement_id):
    announcement = AnnouncementGD.query.get_or_404(announcement_id)
    if announcement.author != current_user:
        abort(403)
    db.session.delete(announcement)
    db.session.commit()
    flash('Your announcement has been deleted!', 'success')
    return redirect(url_for('aab_course.aab_course_home'))   

@aab_course_announcements.route("/auditing_accounting_business_course/announcement/<string:username>")
@login_required
def user_announcements(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    announcements = AnnouncementGD.query.filter_by(author=user)\
        .order_by(AnnouncementGD.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('aab_course/aab_announcements/aab_course_user_announcements.html', announcements=announcements, user=user, func=read_image)                              
