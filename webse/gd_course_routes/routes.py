from flask import render_template, url_for, Blueprint, request
from webse import application, db, bcrypt
from webse.models import AnnouncementGD
from webse.forward_users.utils import save_picture, read_image
gd_course= Blueprint('gd_course', __name__)


@gd_course.route('/green_digitalization_course')
def gd_course_home():
    page = request.args.get('page', 1, type=int)
    announcements = AnnouncementGD.query.order_by(AnnouncementGD.date_posted.desc()).paginate(page=page, per_page=1)
    return render_template('gd_course/gd_course_home.html', announcements=announcements, title='Green Digitalization Course', func=read_image)
  

  
