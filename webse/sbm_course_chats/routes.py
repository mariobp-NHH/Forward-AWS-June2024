from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.sbm_course_chats.forms import ChatForm

sbm_course_chats= Blueprint('sbm_course_chats', __name__)

# These routes are specific for each chat (create-chat)
@sbm_course_chats.route('/sustainable_business_models_course/new', methods=['GET', 'POST'])
@login_required
def sbm_course_chats_new_main_chat(): 
    form = ChatForm()
    legend ='Create chat (main chat)'
    title = 'Create chat (main chat)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='none', chapter='none', group='NMBU_2023')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('sbm_course_chats.sbm_course_chats_view_main_chats'))
    return render_template('sbm_course/sbm_chats/sbm_course_create_chat.html', title=title, form=form, legend=legend)

# These routes are specific for each chat (view-chat)   
@sbm_course_chats.route("/sustainable_business_models_course/view")
@login_required
def sbm_course_chats_view_main_chats():
    title ='View Main Chat'
    legend = 'View chat (main chat)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='NMBU_2023')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('sbm_course/sbm_chats/sbm_course_view_main_chats.html', chats=chats, title=title, legend=legend, func=read_image)    

# These routes are common for all the chats
@sbm_course_chats.route("/sustainable_business_models_course/chat/<int:chat_id>")
def chat(chat_id):
    chat = ChatGD.query.get_or_404(chat_id)
    return render_template('sbm_course/sbm_chats/sbm_course_chat.html', title=chat.title, chat=chat, func=read_image)    

@sbm_course_chats.route("/sustainable_business_models_course/chat/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat(chat_id):
    chat = ChatGD.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatForm()
    if form.validate_on_submit():
        chat.title = form.title.data
        chat.content = form.content.data
        db.session.commit()
        flash('Your chat has been updated!', 'success')
        return redirect(url_for('sbm_course_chats.sbm_course_chats_view_main_chats'))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('sbm_course/sbm_chats/sbm_course_create_chat.html', title='Update Chat',
                           form=form, legend='Update Chat')    

@sbm_course_chats.route("/sustainable_business_models_course/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = ChatGD.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Your chat has been deleted!', 'success')
    return redirect(url_for('sbm_course_chats.sbm_course_chats_view_main_chats'))   

@sbm_course_chats.route("/sustainable_business_models_course/chat/<string:username>")
@login_required
def user_chats(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = ChatGD.query.filter_by(author=user)\
        .order_by(ChatGD.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('sbm_course/sbm_chats/sbm_course_user_chats.html', chats=chats, user=user, func=read_image)                              
