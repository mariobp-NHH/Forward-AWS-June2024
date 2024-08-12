from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.gd_course_chats.forms import ChatForm

gd_course_chats= Blueprint('gd_course_chats', __name__)

@gd_course_chats.route('/green_digitalization_course/create_chat', methods=['GET', 'POST'])
@login_required
def gd_course_chats_create_chat(): 
    return render_template('gd_course/gd_chats/gd_course_create_chat_home.html', title='Create Chat Home')

@gd_course_chats.route('/green_digitalization_course/view_chat', methods=['GET', 'POST'])
@login_required
def gd_course_chats_view_chat(): 
    return render_template('gd_course/gd_chats/gd_course_view_chat_home.html', title='View Chat Home')

# These routes are specific for each chat (create-chat)
@gd_course_chats.route('/green_digitalization_course/main_chat/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_main_chat(): 
    form = ChatForm()
    legend ='Create chat (main chat)'
    title = 'Create chat (main chat)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='none', chapter='none', group='main_chat')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)

    #HVL
@gd_course_chats.route('/green_digitalization_course/chat_HVL_g1/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g1_chat(): 
    form = ChatForm()
    legend ='Create chat group 1 (HVL)'
    title = 'Create chat group 1 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)

@gd_course_chats.route('/green_digitalization_course/chat_HVL_g2/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g2_chat(): 
    form = ChatForm()
    legend ='Create chat group 2 (HVL)'
    title = 'Create chat group 2 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 2')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)

@gd_course_chats.route('/green_digitalization_course/chat_HVL_g3/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g3_chat(): 
    form = ChatForm()
    legend ='Create chat group 3 (HVL)'
    title = 'Create chat group 3 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 3')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)    

@gd_course_chats.route('/green_digitalization_course/chat_HVL_g4/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g4_chat(): 
    form = ChatForm()
    legend ='Create chat group 4 (HVL)'
    title = 'Create chat group 4 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 4')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)       

@gd_course_chats.route('/green_digitalization_course/chat_HVL_g5/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g5_chat(): 
    form = ChatForm()
    legend ='Create chat group 5 (HVL)'
    title = 'Create chat group 5 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 5')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)  

@gd_course_chats.route('/green_digitalization_course/chat_HVL_g6/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g6_chat(): 
    form = ChatForm()
    legend ='Create chat group 6 (HVL)'
    title = 'Create chat group 6 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 6')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)   

@gd_course_chats.route('/green_digitalization_course/chat_HVL_g7/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g7_chat(): 
    form = ChatForm()
    legend ='Create chat group 7 (HVL)'
    title = 'Create chat group 7 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 7')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)  

@gd_course_chats.route('/green_digitalization_course/chat_HVL_g8/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_HVL_g8_chat(): 
    form = ChatForm()
    legend ='Create chat group 8 (HVL)'
    title = 'Create chat group 8 (HVL)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='HVL', chapter='none', group='group 8')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)     

        #NHH
@gd_course_chats.route('/green_digitalization_course/chat_NHH_g1/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g1_chat(): 
    form = ChatForm()
    legend ='Create chat group 1 (NHH)'
    title = 'Create chat group 1 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)

@gd_course_chats.route('/green_digitalization_course/chat_NHH_g2/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g2_chat(): 
    form = ChatForm()
    legend ='Create chat group 2 (NHH)'
    title = 'Create chat group 2 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 2')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)

@gd_course_chats.route('/green_digitalization_course/chat_NHH_g3/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g3_chat(): 
    form = ChatForm()
    legend ='Create chat group 3 (NHH)'
    title = 'Create chat group 3 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 3')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)    

@gd_course_chats.route('/green_digitalization_course/chat_NHH_g4/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g4_chat(): 
    form = ChatForm()
    legend ='Create chat group 4 (NHH)'
    title = 'Create chat group 4 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 4')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)       

@gd_course_chats.route('/green_digitalization_course/chat_NHH_g5/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g5_chat(): 
    form = ChatForm()
    legend ='Create chat group 5 (NHH)'
    title = 'Create chat group 5 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 5')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)  

@gd_course_chats.route('/green_digitalization_course/chat_NHH_g6/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g6_chat(): 
    form = ChatForm()
    legend ='Create chat group 6 (NHH)'
    title = 'Create chat group 6 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 6')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)   

@gd_course_chats.route('/green_digitalization_course/chat_NHH_g7/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g7_chat(): 
    form = ChatForm()
    legend ='Create chat group 7 (NHH)'
    title = 'Create chat group 7 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 7')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)  

@gd_course_chats.route('/green_digitalization_course/chat_NHH_g8/new', methods=['GET', 'POST'])
@login_required
def gd_course_chats_new_NHH_g8_chat(): 
    form = ChatForm()
    legend ='Create chat group 8 (NHH)'
    title = 'Create chat group 8 (NHH)'
    if form.validate_on_submit():
        chat = ChatGD(title=form.title.data, content=form.content.data, author=current_user, institution='NHH', chapter='none', group='group 8')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gd_course.gd_course_home'))
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title=title, form=form, legend=legend)     


# These routes are specific for each chat (view-chat)   
@gd_course_chats.route("/green_digitalization_course/main_chat/view")
@login_required
def gd_course_chats_view_main_chats():
    title ='View Main Chat'
    legend = 'View chat (main chat)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='main_chat')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_main_chats.html', chats=chats, title=title, legend=legend, func=read_image)    

    # HVL
@gd_course_chats.route("/green_digitalization_course/HVL_g1/view")
@login_required
def gd_course_chats_view_HVL_g1_chats():
    title ='View chat group 1 (HVL)'
    legend = 'View chat group 1 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 1')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g1_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/HVL_g2/view")
@login_required
def gd_course_chats_view_HVL_g2_chats():
    title ='View chat group 2 (HVL)'
    legend = 'View chat group 2 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 2')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g2_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/HVL_g3/view")
@login_required
def gd_course_chats_view_HVL_g3_chats():
    title ='View chat group 3 (HVL)'
    legend = 'View chat group 3 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 3')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g3_chats.html', chats=chats, title=title, legend=legend, func=read_image)      

@gd_course_chats.route("/green_digitalization_course/HVL_g4/view")
@login_required
def gd_course_chats_view_HVL_g4_chats():
    title ='View chat group 4 (HVL)'
    legend = 'View chat group 4 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 4')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g4_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/HVL_g5/view")
@login_required
def gd_course_chats_view_HVL_g5_chats():
    title ='View chat group 5 (HVL)'
    legend = 'View chat group 5 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 5')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g5_chats.html', chats=chats, title=title, legend=legend, func=read_image) 

@gd_course_chats.route("/green_digitalization_course/HVL_g6/view")
@login_required
def gd_course_chats_view_HVL_g6_chats():
    title ='View chat group 6 (HVL)'
    legend = 'View chat group 6 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 6')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g6_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/HVL_g7/view")
@login_required
def gd_course_chats_view_HVL_g7_chats():
    title ='View chat group 7 (HVL)'
    legend = 'View chat group 7 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 7')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g7_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/HVL_g8/view")
@login_required
def gd_course_chats_view_HVL_g8_chats():
    title ='View chat group 8 (HVL)'
    legend = 'View chat group 8 (HVL)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 8')\
        .filter_by(institution='HVL')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_HVL_g8_chats.html', chats=chats, title=title, legend=legend, func=read_image) 

    # NHH
@gd_course_chats.route("/green_digitalization_course/NHH_g1/view")
@login_required
def gd_course_chats_view_NHH_g1_chats():
    title ='View chat group 1 (NHH)'
    legend = 'View chat group 1 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 1')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g1_chats.html', chats=chats, title=title, legend=legend, func=read_image) 

@gd_course_chats.route("/green_digitalization_course/NHH_g2/view")
@login_required
def gd_course_chats_view_NHH_g2_chats():
    title ='View chat group 2 (NHH)'
    legend = 'View chat group 2 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 2')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g2_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/NHH_g3/view")
@login_required
def gd_course_chats_view_NHH_g3_chats():
    title ='View chat group 3 (NHH)'
    legend = 'View chat group 3 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 3')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g3_chats.html', chats=chats, title=title, legend=legend, func=read_image)      

@gd_course_chats.route("/green_digitalization_course/NHH_g4/view")
@login_required
def gd_course_chats_view_NHH_g4_chats():
    title ='View chat group 4 (NHH)'
    legend = 'View chat group 4 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 4')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g4_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/NHH_g5/view")
@login_required
def gd_course_chats_view_NHH_g5_chats():
    title ='View chat group 5 (NHH)'
    legend = 'View chat group 5 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 5')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g5_chats.html', chats=chats, title=title, legend=legend, func=read_image) 

@gd_course_chats.route("/green_digitalization_course/NHH_g6/view")
@login_required
def gd_course_chats_view_NHH_g6_chats():
    title ='View chat group 6 (NHH)'
    legend = 'View chat group 6 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 6')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g6_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/NHH_g7/view")
@login_required
def gd_course_chats_view_NHH_g7_chats():
    title ='View chat group 7 (NHH)'
    legend = 'View chat group 7 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 7')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g7_chats.html', chats=chats, title=title, legend=legend, func=read_image)  

@gd_course_chats.route("/green_digitalization_course/NHH_g8/view")
@login_required
def gd_course_chats_view_NHH_g8_chats():
    title ='View chat group 8 (NHH)'
    legend = 'View chat group 8 (NHH)'
    page = request.args.get('page', 1, type=int)
    chats = ChatGD.query.filter_by(group='group 8')\
        .filter_by(institution='NHH')\
        .order_by(ChatGD.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('gd_course/gd_chats/gd_course_view_NHH_g8_chats.html', chats=chats, title=title, legend=legend, func=read_image) 

# These routes are common for all the chats
@gd_course_chats.route("/green_digitalization_course/chat/<int:chat_id>")
def chat(chat_id):
    chat = ChatGD.query.get_or_404(chat_id)
    return render_template('gd_course/gd_chats/gd_course_chat.html', title=chat.title, chat=chat, func=read_image)    

@gd_course_chats.route("/green_digitalization_course/chat/<int:chat_id>/update", methods=['GET', 'POST'])
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
        return redirect(url_for('gd_course.gd_course_home'))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('gd_course/gd_chats/gd_course_create_chat.html', title='Update Chat',
                           form=form, legend='Update Chat')    

@gd_course_chats.route("/green_digitalization_course/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = ChatGD.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Your chat has been deleted!', 'success')
    return redirect(url_for('gd_course.gd_course_home'))   

@gd_course_chats.route("/green_digitalization_course/chat/<string:username>")
@login_required
def user_chats(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = ChatGD.query.filter_by(author=user)\
        .order_by(ChatGD.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('gd_course/gd_chats/gd_course_user_chats.html', chats=chats, user=user, func=read_image)                              
