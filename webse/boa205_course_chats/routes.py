from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatES
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.boa205_course_chats.forms import ChatForm

boa205_course_chats= Blueprint('boa205_course_chats', __name__)

@boa205_course_chats.route('/boa205_course/create_chat', methods=['GET', 'POST'])
@login_required
def boa205_course_chats_create_chat():
    return render_template('boa205_course/boa205_chats/boa205_course_create_chat_home.html', title='Opprett Chat Home')

@boa205_course_chats.route('/boa205_course/view_chat', methods=['GET', 'POST'])
@login_required
def boa205_course_chats_view_chat():
    return render_template('boa205_course/boa205_chats/boa205_course_view_chat_home.html', title='Se Chat Home')

# These routes are specific for each chat (create-chat)
@boa205_course_chats.route('/boa205_course/main_chat/new', methods=['GET', 'POST'])
@login_required
def boa205_course_chats_new_main_chat():
    form = ChatForm()
    legend ='Opprett chat (hovedchat)'
    title = 'Opprett chat (hovedchat)'
    if form.validate_on_submit():
        chat = ChatES(title=form.title.data, content=form.content.data, author=current_user, institution='none', chapter='none', group='boa205_main_chat')
        db.session.add(chat)
        db.session.commit()
        flash('Chatten din er opprettet!', 'success')
        return redirect(url_for('boa205_course.boa205_course_home'))
    return render_template('boa205_course/boa205_chats/boa205_course_create_chat.html', title=title, form=form, legend=legend)


# These routes are specific for each chat (view-chat)
@boa205_course_chats.route("/boa205_course/main_chat/view")
@login_required
def boa205_course_chats_view_main_chats():
    title ='Se hovedchat'
    legend = 'Se hovedchat'
    page = request.args.get('page', 1, type=int)
    chats = ChatES.query.filter_by(group='boa205_main_chat')\
        .order_by(ChatES.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('boa205_course/boa205_chats/boa205_course_view_main_chats.html', chats=chats, title=title, legend=legend, func=read_image)


# These routes are common for all the chats
@boa205_course_chats.route("/boa205_course/chat/<int:chat_id>")
def chat(chat_id):
    chat = ChatES.query.get_or_404(chat_id)
    return render_template('boa205_course/boa205_chats/boa205_course_chat.html', title=chat.title, chat=chat, func=read_image)

@boa205_course_chats.route("/boa205_course/chat/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat(chat_id):
    chat = ChatES.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatForm()
    if form.validate_on_submit():
        chat.title = form.title.data
        chat.content = form.content.data
        db.session.commit()
        flash('Chatten din har blitt oppdatert!', 'success')
        return redirect(url_for('boa205_course.boa205_course_home'))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('boa205_course/boa205_chats/boa205_course_create_chat.html', title='Oppdater Chat',
                           form=form, legend='Oppdater Chat')

@boa205_course_chats.route("/boa205_course/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = ChatES.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Chatten din er slettet!', 'success')
    return redirect(url_for('boa205_course.boa205_course_home'))

@boa205_course_chats.route("/boa205_course/chat/<string:username>")
@login_required
def user_chats(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = ChatES.query.filter_by(author=user)\
        .order_by(ChatES.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('boa205_course/boa205_chats/boa205_course_user_chats.html', chats=chats, user=user, func=read_image)
