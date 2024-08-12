from flask import render_template, url_for, Blueprint
from webse import application, db
forward_home= Blueprint('forward_home', __name__)


@forward_home.route('/home')
@forward_home.route('/')
def home():
    db.create_all()
    return render_template('forward_home/home.html', title='Home')

@forward_home.route('/developers')
def developers():
    return render_template('forward_home/developers.html', title='Developers')

  
