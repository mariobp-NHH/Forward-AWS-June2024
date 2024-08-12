from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatSEP
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.se_platform_announcements.forms import AnnouncementForm

se_platform_announcements= Blueprint('se_platform_announcements', __name__)

@se_platform_announcements.route('/sustainable_energy_platform/announcement/new', methods=['GET', 'POST'])
@login_required
def se_platform_announcements_new_announcement(): 
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement = ChatSEP(title=form.title.data, content=form.content.data, chat_module='home', chat_group='home', author=current_user)
        db.session.add(announcement)
        db.session.commit()
        flash('Your announcement has been created!', 'success')
        return redirect(url_for('se_platform_home.se_platform_home_home'))
    return render_template('se_platform/se_platform_announcements/se_platform_create_announcement.html', title='New announcement', form=form)

@se_platform_announcements.route("/sustainable_energy_platform/announcement/<int:announcement_id>")
def announcement(announcement_id):
    announcement = ChatSEP.query.get_or_404(announcement_id)
    return render_template('se_platform/se_platform_announcements/se_platform_announcement.html', title=announcement.title, announcement=announcement, func=read_image)    

@se_platform_announcements.route("/sustainable_energy_platform/announcement/<int:announcement_id>/update", methods=['GET', 'POST'])
@login_required
def update_announcement(announcement_id):
    announcement = ChatSEP.query.get_or_404(announcement_id)
    if announcement.author != current_user:
        abort(403)
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement.title = form.title.data
        announcement.content = form.content.data
        db.session.commit()
        flash('Your announcement has been updated!', 'success')
        return redirect(url_for('se_platform_home.se_platform_home_home'))
    elif request.method == 'GET':
        form.title.data = announcement.title
        form.content.data = announcement.content
    return render_template('se_platform/se_platform_announcements/se_platform_create_announcement.html', title='Update announcement',
                           form=form, legend='Update announcement')    

@se_platform_announcements.route("/sustainable_energy_platform/announcement/<int:announcement_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_announcement(announcement_id):
    announcement = ChatSEP.query.get_or_404(announcement_id)
    if announcement.author != current_user:
        abort(403)
    db.session.delete(announcement)
    db.session.commit()
    flash('Your announcement has been deleted!', 'success')
    return redirect(url_for('se_platform_home.se_platform_home_home'))   

@se_platform_announcements.route("/sustainable_energy_platform/announcement/<string:username>")
@login_required
def user_announcements(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    announcements = ChatSEP.query.filter_by(author=user)\
        .order_by(ChatSEP.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('se_platform/se_platform_announcements/se_platform_user_announcements.html', announcements=announcements, user=user, func=read_image)  

