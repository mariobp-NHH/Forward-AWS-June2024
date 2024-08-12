from flask import render_template, Blueprint, request
from webse.models import AnnouncementES
from webse.forward_users.utils import save_picture, read_image
es_course= Blueprint('es_course', __name__)

@es_course.route('/economías_del_español_curso')
def es_course_home():
    page = request.args.get('page', 1, type=int)
    announcements = AnnouncementES.query.order_by(AnnouncementES.date_posted.desc()).filter(AnnouncementES.user_id==1).paginate(page=page, per_page=1)
    return render_template('es_course/es_course_home.html', announcements=announcements, title='Economies of Spanish Course', func=read_image)
  

  
