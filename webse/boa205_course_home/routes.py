from flask import render_template, Blueprint, request
from webse.models import AnnouncementES
from webse.forward_users.utils import save_picture, read_image
boa205_course= Blueprint('boa205_course', __name__)

@boa205_course.route('/boa205_course')
def boa205_course_home():
    page = request.args.get('page', 1, type=int)
    announcements = AnnouncementES.query.order_by(AnnouncementES.date_posted.desc()).filter(AnnouncementES.user_id==500).paginate(page=page, per_page=1)
    return render_template('boa205_course/boa205_course_home.html', announcements=announcements, title='BOA205 Course', func=read_image)
