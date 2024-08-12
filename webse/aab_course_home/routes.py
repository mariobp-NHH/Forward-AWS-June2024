from flask import render_template, url_for, Blueprint, request
from webse import application, db, bcrypt
from webse.models import AnnouncementGD
from webse.forward_users.utils import save_picture, read_image
aab_course= Blueprint('aab_course', __name__)

@aab_course.route('/auditing_accounting_business_course')
def aab_course_home():
    page = request.args.get('page', 1, type=int)
    announcements = AnnouncementGD.query.order_by(AnnouncementGD.date_posted.desc()).\
        filter((AnnouncementGD.user_id==198)).paginate(page=page, per_page=1)
    return render_template('aab_course/aab_course_home.html', announcements=announcements, title='Auditing Accounting and Business Course', func=read_image)
 
