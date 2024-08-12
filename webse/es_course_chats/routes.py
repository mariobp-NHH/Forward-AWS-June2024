from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatES
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.es_course_chats.forms import ChatForm

es_course_chats= Blueprint('es_course_chats', __name__)

@es_course_chats.route('/economías_del_español_curso/crear_chat', methods=['GET', 'POST'])
@login_required
def es_course_chats_create_chat(): 
    return render_template('es_course/es_chats/es_course_create_chat_home.html', title='Crear Chat Home')

@es_course_chats.route('/economías_del_español_curso/ver_chat', methods=['GET', 'POST'])
@login_required
def es_course_chats_view_chat(): 
    return render_template('es_course/es_chats/es_course_view_chat_home.html', title='View Chat Home')

# These routes are specific for each chat (create-chat)
@es_course_chats.route('/economías_del_español_curso/chat_principal/nuevo', methods=['GET', 'POST'])
@login_required
def es_course_chats_new_main_chat(): 
    form = ChatForm()
    legend ='Crear chat (chat principal)'
    title = 'Crear chat (chat principal)'
    if form.validate_on_submit():
        chat = ChatES(title=form.title.data, content=form.content.data, author=current_user, institution='none', chapter='none', group='main_chat')
        db.session.add(chat)
        db.session.commit()
        flash('Tu chat sea creado!', 'success')
        return redirect(url_for('es_course.es_course_home'))
    return render_template('es_course/es_chats/es_course_create_chat.html', title=title, form=form, legend=legend)


# These routes are specific for each chat (view-chat)   
@es_course_chats.route("/economías_del_español_curso/chat_principal/ver")
@login_required
def es_course_chats_view_main_chats():
    title ='Ver Chat Principal'
    legend = 'Ver chat (chat principal)'
    page = request.args.get('page', 1, type=int)
    chats = ChatES.query.filter_by(group='main_chat')\
        .order_by(ChatES.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('es_course/es_chats/es_course_view_main_chats.html', chats=chats, title=title, legend=legend, func=read_image)    


# These routes are common for all the chats
@es_course_chats.route("/economías_del_español_curso/chat/<int:chat_id>")
def chat(chat_id):
    chat = ChatES.query.get_or_404(chat_id)
    return render_template('es_course/es_chats/es_course_chat.html', title=chat.title, chat=chat, func=read_image)    

@es_course_chats.route("/economías_del_español_curso/chat/<int:chat_id>/actualizar", methods=['GET', 'POST'])
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
        flash('Tu chat se ha actualizado!', 'success')
        return redirect(url_for('es_course.es_course_home'))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('es_course/es_chats/es_course_create_chat.html', title='Actualizar Chat',
                           form=form, legend='Actualizar Chat')    

@es_course_chats.route("/economías_del_español_curso/chat/<int:chat_id>/eliminar", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = ChatES.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Tu chat se ha eliminado!', 'success')
    return redirect(url_for('es_course.es_course_home'))   

@es_course_chats.route("/economías_del_español_curso/chat/<string:username>")
@login_required
def user_chats(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = ChatES.query.filter_by(author=user)\
        .order_by(ChatES.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('es_course/es_chats/es_course_user_chats.html', chats=chats, user=user, func=read_image)                              
