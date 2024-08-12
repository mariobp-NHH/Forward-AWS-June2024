from flask import render_template, Blueprint, redirect, flash, url_for
from webse.gd_course_app_calculator_2023_ch8.forms import RegistrationForm, LoginForm

gd_course_app_carbon_app_2023_ch8=Blueprint('gd_course_app_carbon_app_2023_ch8',__name__)

# Home
@gd_course_app_carbon_app_2023_ch8.route('/green_digitalization_course/app_calculator/2023/ch8/home')
def home():
  return render_template('gd_course/chapters/ch8_home.html', title='home')

# Users
@gd_course_app_carbon_app_2023_ch8.route('/green_digitalization_course/app_calculator/2023/ch8/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      flash('Your account has been created! Now, you are able to login!', 'success')
      return redirect(url_for('gd_course_app_carbon_app_2023_ch8.home'))
  return render_template('gd_course/chapters/ch8_register.html', title='register', form=form)

@gd_course_app_carbon_app_2023_ch8.route('/green_digitalization_course/app_calculator/2023/ch8/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'fjell@demo.com' and form.email.data == 'regn':
        flash('You have logged in! Now, you can start to use Forward!', 'success')
        return redirect(url_for('gd_course_app_carbon_app_2023_ch8.home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('gd_course/chapters/ch8_login.html', title='login', form=form)

# Methodology
@gd_course_app_carbon_app_2023_ch8.route('/green_digitalization_course/app_calculator/2023/ch8/methodology')
def methodology():
  return render_template('gd_course/chapters/ch8_methodology.html', title='methodology')

# Carbon_app
@gd_course_app_carbon_app_2023_ch8.route('/green_digitalization_course/app_calculator/2023/ch8/carbon_app')
def carbon_app():
    return render_template('gd_course/chapters/ch8_carbon_app.html', title='gd_course_app_carbon_app_2023_ch8')

@gd_course_app_carbon_app_2023_ch8.route('/green_digitalization_course/app_calculator/2023/ch8/new_entry')
def new_entry():
    return render_template('gd_course/chapters/ch8_new_entry.html', title='new_entry')

@gd_course_app_carbon_app_2023_ch8.route('/green_digitalization_course/app_calculator/2023/ch8/your_data')
def your_data():
    return render_template('gd_course/chapters/ch8_your_data.html', title='your_data')