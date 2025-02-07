from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGender
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.gender_platform_chats.forms import ChatForm

gender_platform_chats= Blueprint('gender_platform_chats', __name__)

@gender_platform_chats.route('/gender_platform/chat/new', methods=['GET', 'POST'])
@login_required
def gender_platform_chats_new_chat(): 
    form = ChatForm()
    if form.validate_on_submit():
        chat = ChatGender(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gender_platform.gender_platform_home'))
    return render_template('gender_platform/gender_platform_create_chat.html', title='New Chat', form=form)

@gender_platform_chats.route("/gender_platform/chat/<int:chat_id>")
def chat(chat_id):
    chat = ChatGender.query.get_or_404(chat_id)
    return render_template('gender_platform/gender_platform_chat.html', title=chat.title, chat=chat, func=read_image)    

@gender_platform_chats.route("/gender_platform/chat/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat(chat_id):
    chat = ChatGender.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatForm()
    if form.validate_on_submit():
        chat.title = form.title.data
        chat.content = form.content.data
        db.session.commit()
        flash('Your chat has been updated!', 'success')
        return redirect(url_for('gender_platform.gender_platform_home'))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('gender_platform/gender_platform_create_chat.html', title='Update Chat',
                           form=form, legend='Update Chat', func=read_image)    

@gender_platform_chats.route("/gender_platform/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = ChatGender.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Your chat has been deleted!', 'success')
    return redirect(url_for('gender_platform.gender_platform_home'))   


@gender_platform_chats.route("/gender_platform/chat/<string:username>")
@login_required
def user_chats(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = ChatGender.query.filter_by(author=user)\
        .order_by(ChatGender.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('gender_platform/gender_platform_user_chats.html', chats=chats, user=user, func=read_image)                              
