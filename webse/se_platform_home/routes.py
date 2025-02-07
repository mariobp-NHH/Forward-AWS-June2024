from datetime import timedelta, datetime
from flask import render_template, Blueprint, request
from webse.models import ChatSEP
from webse.forward_users.utils import save_picture, read_image
se_platform_home= Blueprint('se_platform_home', __name__)

@se_platform_home.route('/sustainable_energy_platform')
def se_platform_home_home():
    page = request.args.get('page', 1, type=int)
    announcements = ChatSEP.query.filter_by(chat_module='home').order_by(ChatSEP.date_posted.desc()).paginate(page=page, per_page=1)
    return render_template('se_platform/se_platform_home.html', announcements=announcements, title='Home', func=read_image)

