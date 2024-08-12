from flask import render_template, url_for, Blueprint
from webse import application, db
boilerplates= Blueprint('boilerplates', __name__)


@boilerplates.route('/boilerplates')
def boilerplates_home():
    return render_template('boilerplates/boilerplates_home.html', title='Boilerplates')



  
