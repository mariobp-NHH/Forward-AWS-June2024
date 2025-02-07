from flask import render_template, url_for, Blueprint, request
from webse import application, db, bcrypt
from webse.models import ChatGender
from webse.forward_users.utils import read_image
gender_platform= Blueprint('gender_platform', __name__)


@gender_platform.route('/gender_platform')
def gender_platform_home():
    page = request.args.get('page', 1, type=int)
    chats = ChatGender.query.order_by(ChatGender.date_posted.desc()).paginate(page=page, per_page=1)
    return render_template('gender_platform/gender_platform_home.html', chats=chats, title='Gender Platform', func=read_image)
  
