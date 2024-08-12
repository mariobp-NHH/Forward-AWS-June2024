from flask import render_template, url_for, Blueprint, request
from webse import application, db, bcrypt
from webse.models import AnnouncementGD
from webse.forward_users.utils import save_picture, read_image
sbm_course= Blueprint('sbm_course', __name__)

@sbm_course.route('/sustainable_business_models_course')
def sbm_course_home():
    page = request.args.get('page', 1, type=int)
    announcements = AnnouncementGD.query.order_by(AnnouncementGD.date_posted.desc()).\
        filter((AnnouncementGD.user_id==172) | (AnnouncementGD.user_id==173)).paginate(page=page, per_page=1)
    return render_template('sbm_course/sbm_course_home.html', announcements=announcements, title='Sustainable Business Models Course', func=read_image)

@sbm_course.route('/sustainable_business_models_course/app_module')
def sbm_course_app_module():
    return render_template('sbm_course/sbm_app_module/app_module_home.html', title='Sustainable Business Models Course, App Module')
  
#Chapter 8
@sbm_course.route('/sustainable_business_models_course/app_module/chapter8')
def sbm_course_chapters_ch8(): 
    return render_template('sbm_course/sbm_app_module/chapters/ch8.html', title='Sustainable Business Models Course, ch8')   

#Chapter 9
@sbm_course.route('/sustainable_business_models_course/app_module/chapter9')
def sbm_course_chapters_ch9(): 
    return render_template('sbm_course/sbm_app_module/chapters/ch9.html', title='Sustainable Business Models Course, ch9') 

#Chapter 10
@sbm_course.route('/sustainable_business_models_course/app_module/chapter10')
def sbm_course_chapters_ch10(): 
    return render_template('sbm_course/sbm_app_module/chapters/ch10.html', title='Sustainable Business Models Course, ch10') 
  
