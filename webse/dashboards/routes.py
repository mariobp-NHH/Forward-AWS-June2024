from flask import Flask, render_template, Blueprint

dashboards = Blueprint('dashboards', __name__)

@dashboards.route('/dashboards/home')
def home():
    return render_template('dashboards/home_dashboards.html')