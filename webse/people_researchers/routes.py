from flask import render_template, url_for, Blueprint
from webse import application, db
people_researchers= Blueprint('people_researchers', __name__)


@people_researchers.route('/mario_blazquez')
def mario_blazquez():
    return render_template('people_researchers/mario_blazquez/mario_blazquez_home.html', title='Mario Blazquez')

  