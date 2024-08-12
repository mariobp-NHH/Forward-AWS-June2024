from flask import render_template, Blueprint

gd_course_app_carbon_app_2023_ch6=Blueprint('gd_course_app_carbon_app_2023_ch6',__name__)

# Home
@gd_course_app_carbon_app_2023_ch6.route('/green_digitalization_course/app_calculator/2023/ch6/home')
def home():
  return render_template('gd_course/chapters/ch6_home.html', title='home')

# Users
@gd_course_app_carbon_app_2023_ch6.route('/green_digitalization_course/app_calculator/2023/ch6/register')
def register():
  return render_template('gd_course/chapters/ch6_register.html', title='register')

@gd_course_app_carbon_app_2023_ch6.route('/green_digitalization_course/app_calculator/2023/ch6/login')
def login():
  return render_template('gd_course/chapters/ch6_login.html', title='login')

# Methodology
@gd_course_app_carbon_app_2023_ch6.route('/green_digitalization_course/app_calculator/2023/ch6/methodology')
def methodology():
  return render_template('gd_course/chapters/ch6_methodology.html', title='methodology')

# Carbon_app
@gd_course_app_carbon_app_2023_ch6.route('/green_digitalization_course/app_calculator/2023/ch6/carbon_app')
def carbon_app():
    return render_template('gd_course/chapters/ch6_carbon_app.html', title='gd_course_app_carbon_app_2023_ch6')

@gd_course_app_carbon_app_2023_ch6.route('/green_digitalization_course/app_calculator/2023/ch6/new_entry')
def new_entry():
    return render_template('gd_course/chapters/ch6_new_entry.html', title='new_entry')

@gd_course_app_carbon_app_2023_ch6.route('/green_digitalization_course/app_calculator/2023/ch6/your_data')
def your_data():
    return render_template('gd_course/chapters/ch6_your_data.html', title='your_data')