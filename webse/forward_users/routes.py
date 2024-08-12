from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.forward_users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from webse.models import User
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import save_picture, read_image

forward_users= Blueprint('forward_users', __name__)

@forward_users.route('/forward/register', methods=['GET','POST'])
def forward_users_register():
    if current_user.is_authenticated:
        return redirect(url_for('forward_home.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution=form.institution.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('forward_users.forward_users_login'))
    return render_template('forward_home/forward_register.html', title='Register', form=form)

@forward_users.route('/forward/login', methods=['GET','POST'])
def forward_users_login():
    if current_user.is_authenticated:
        return redirect(url_for('forward_home.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have logged in! Now, you can start to use Forward!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('forward_home.home'))
        else:
            flash('Login Unsuccessful. Please check email and password!', 'danger')   
    return render_template('forward_home/forward_login.html', title='Login', form=form)       

@forward_users.route('/forward/logout')
def forward_users_logout():    
    logout_user()
    return redirect(url_for('forward_home.home'))

@forward_users.route('/forward/account', methods=['GET','POST'])
@login_required
def forward_users_account(): 
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.institution = form.institution.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('forward_users.forward_users_account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    encoded_data=read_image(current_user.image_file)

    return render_template('forward_home/forward_account.html', title='Account', image_file=encoded_data, form=form)   
