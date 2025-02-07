from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatSEP, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.papers.spot_go.forms import ChatForm, SpotGo_q1, SpotGo_q2, SpotGo_q3, SpotGo_q4, SpotGo_q5, SpotGo_q6

papers_spot_go= Blueprint('papers_spot_go', __name__)

@papers_spot_go.route('/papers/spot_go/authors')
def papers_spot_go_authors(): 
    return render_template('papers/spot_go/authors.html', title='Spot-GO, authors')

@papers_spot_go.route('/papers/spot_go/calendar')
def papers_spot_go_calendar(): 
    return render_template('papers/spot_go/calendar.html', title='Spot-GO, calendar')   

@papers_spot_go.route('/papers/spot_go/chat', methods=['GET', 'POST'])
@login_required
def papers_spot_go_chat_main():
    page = request.args.get('page', 1, type=int)
    chats = ChatSEP.query.filter_by(chat_module='spot_go_main').order_by(ChatSEP.date_posted.desc()).paginate(page=page, per_page=1) 
    return render_template('papers/spot_go/general_chat_summary.html', title='Spot-GO, chat-summary', chats=chats, func=read_image)  

@papers_spot_go.route('/papers/spot_go/chat/new', methods=['GET', 'POST'])
@login_required
def spot_go_chat_main_new_chat(): 
    form = ChatForm()
    if form.validate_on_submit():
        chat = ChatSEP(title=form.title.data, content=form.content.data, chat_module='spot_go_main', chat_group='spot_go_main', author=current_user)
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('papers_spot_go.papers_spot_go_chat_main'))
    return render_template('papers/spot_go/main_chat/spot_go_create_chat.html', title='Spot-GO, new chat', form=form)

@papers_spot_go.route("/papers/spot_go/chat/<int:chat_id>")
def chat_main(chat_id):
    chat = ChatSEP.query.get_or_404(chat_id)
    return render_template('papers/spot_go/main_chat/spot_go_chat.html', title=chat.title, chat=chat, func=read_image)    

@papers_spot_go.route("/papers/spot_go/chat/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat_main(chat_id):
    chat = ChatSEP.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatForm()
    if form.validate_on_submit():
        chat.title = form.title.data
        chat.content = form.content.data
        db.session.commit()
        flash('Your chat has been updated!', 'success')
        return redirect(url_for('papers_spot_go.papers_spot_go_chat_main'))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('papers/spot_go/main_chat/spot_go_create_chat.html', title='Spot-GO, update chat',
                           form=form, legend='Update chat')    

@papers_spot_go.route("/papers/spot_go/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat_main(chat_id):
    chat = ChatSEP.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Your chat has been deleted!', 'success')
    return redirect(url_for('papers_spot_go.papers_spot_go_chat_main'))   

@papers_spot_go.route("/papers/spot_go/chat/<string:username>")
@login_required
def user_chats_main(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = ChatSEP.query.filter_by(author=user)\
        .order_by(ChatSEP.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('papers/spot_go/main_chat/spot_go_user_chats.html', chats=chats, user=user, func=read_image)  

@papers_spot_go.route('/papers/spot_go/students_questions', methods=['GET', 'POST'])
@login_required
def papers_spot_go_students_questions(): 
    spot_go_q1 = SpotGo_q1()
    spot_go_q2 = SpotGo_q2()
    spot_go_q3 = SpotGo_q3()
    spot_go_q4 = SpotGo_q4()
    spot_go_q5 = SpotGo_q5()
    spot_go_q6 = SpotGo_q6()

    if spot_go_q1.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'spot_go'). \
            filter(ModulsGD.title_ch == 'spot_go'). \
            filter(ModulsGD.question_num == 1).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=spot_go_q1.type.data, author=current_user)
        if moduls.question_str == 'An increase in competition in the spot market':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'spot_go'
        moduls.title_ch = 'spot_go'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'spot_go'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('papers_spot_go.papers_spot_go_students_questions'))

    if spot_go_q2.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'spot_go'). \
            filter(ModulsGD.title_ch == 'spot_go'). \
            filter(ModulsGD.question_num == 2).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=spot_go_q2.type.data, author=current_user)
        if moduls.question_str == 'It fosters competition in the spot market':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'spot_go'
        moduls.title_ch = 'spot_go'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'spot_go'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('papers_spot_go.papers_spot_go_students_questions'))

    if spot_go_q3.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'spot_go'). \
            filter(ModulsGD.title_ch == 'spot_go'). \
            filter(ModulsGD.question_num == 3).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=spot_go_q3.type.data, author=current_user)
        if moduls.question_str == 'Allow only the new green production technology capacity to participate in the GO market':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'spot_go'
        moduls.title_ch = 'spot_go'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'spot_go'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('papers_spot_go.papers_spot_go_students_questions'))    

    if spot_go_q4.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'spot_go'). \
            filter(ModulsGD.title_ch == 'spot_go'). \
            filter(ModulsGD.question_num == 4).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=spot_go_q4.type.data, author=current_user)
        if moduls.question_str == 'It deactivates the competition in the GO market':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'spot_go'
        moduls.title_ch = 'spot_go'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'spot_go'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('papers_spot_go.papers_spot_go_students_questions'))   
    if spot_go_q5.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'spot_go'). \
            filter(ModulsGD.title_ch == 'spot_go'). \
            filter(ModulsGD.question_num == 5).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=spot_go_q5.type.data, author=current_user)
        if moduls.question_str == '5.137':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'spot_go'
        moduls.title_ch = 'spot_go'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'spot_go'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('papers_spot_go.papers_spot_go_students_questions')) 
    if spot_go_q6.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'spot_go'). \
            filter(ModulsGD.title_ch == 'spot_go'). \
            filter(ModulsGD.question_num == 6).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=spot_go_q6.type.data, author=current_user)
        if moduls.question_str == '4.954':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'spot_go'
        moduls.title_ch = 'spot_go'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'spot_go'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('papers_spot_go.papers_spot_go_students_questions')) 
    return render_template('papers/spot_go/students_questions.html', title='Spot-GO, students questions',
        spot_go_q1=spot_go_q1, spot_go_q2=spot_go_q2, spot_go_q3=spot_go_q3,
        spot_go_q4=spot_go_q4, spot_go_q5=spot_go_q5, spot_go_q6=spot_go_q6)

@papers_spot_go.route('/papers/spot_go/students_answers', methods=['GET', 'POST'])
@login_required
def students_answers():
    page = request.args.get('page', 1, type=int)
    chats = ChatSEP.query.filter_by(chat_module='spot_go_student').order_by(ChatSEP.date_posted.desc()).paginate(page=page, per_page=1) 

    entries = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.title_mo=='spot_go'). \
        filter(ModulsGD.title_ch=='spot_go'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).all()

    incorrect = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==0). \
        filter(ModulsGD.title_mo=='spot_go'). \
        filter(ModulsGD.title_ch=='spot_go'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct = ModulsGD.query.filter_by(author=current_user). \
        filter(ModulsGD.question_result==1). \
        filter(ModulsGD.title_mo=='spot_go'). \
        filter(ModulsGD.title_ch=='spot_go'). \
        filter(ModulsGD.question_option==50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q1 = ModulsGD.query.filter(ModulsGD.question_num == 1). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q2 = ModulsGD.query.filter(ModulsGD.question_num == 2). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q3 = ModulsGD.query.filter(ModulsGD.question_num == 3). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    incorrect_q4 = ModulsGD.query.filter(ModulsGD.question_num == 4). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q4 = ModulsGD.query.filter(ModulsGD.question_num == 4). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count() 

    incorrect_q5 = ModulsGD.query.filter(ModulsGD.question_num == 5). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q5 = ModulsGD.query.filter(ModulsGD.question_num == 5). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()    

    incorrect_q6 = ModulsGD.query.filter(ModulsGD.question_num == 6). \
        filter(ModulsGD.question_result == 0). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()

    correct_q6 = ModulsGD.query.filter(ModulsGD.question_num == 6). \
        filter(ModulsGD.question_result == 1). \
        filter(ModulsGD.title_mo == 'spot_go'). \
        filter(ModulsGD.title_ch == 'spot_go'). \
        filter(ModulsGD.question_option == 50). \
        order_by(ModulsGD.question_num.asc()).count()       

    return render_template('papers/spot_go/students_answers.html', title='Spot-GO, students answers', entries=entries,
                           correct=correct, incorrect=incorrect,
                           correct_q1=correct_q1, incorrect_q1=incorrect_q1,
                           correct_q2=correct_q2, incorrect_q2=incorrect_q2,
                           correct_q3=correct_q3, incorrect_q3=incorrect_q3,
                           correct_q4=correct_q4, incorrect_q4=incorrect_q4,
                           correct_q5=correct_q5, incorrect_q5=incorrect_q5,
                           correct_q6=correct_q6, incorrect_q6=incorrect_q6,
                           chats=chats, func=read_image)

@papers_spot_go.route('/papers/spot_go/students_answers/new', methods=['GET', 'POST'])
@login_required
def spot_go_chat_student_new_chat(): 
    form = ChatForm()
    if form.validate_on_submit():
        chat = ChatSEP(title=form.title.data, content=form.content.data, chat_module='spot_go_student', chat_group='spot_go_student', author=current_user)
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('papers_spot_go.students_answers'))
    return render_template('papers/spot_go/student_chat/spot_go_create_chat.html', title='Spot-GO, new chat', form=form)

@papers_spot_go.route("/papers/spot_go/students_answers/<int:chat_id>")
def chat_student(chat_id):
    chat = ChatSEP.query.get_or_404(chat_id)
    return render_template('papers/spot_go/student_chat/spot_go_chat.html', title=chat.title, chat=chat, func=read_image)    

@papers_spot_go.route("/papers/spot_go/students_answers/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat_student(chat_id):
    chat = ChatSEP.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatForm()
    if form.validate_on_submit():
        chat.title = form.title.data
        chat.content = form.content.data
        db.session.commit()
        flash('Your chat has been updated!', 'success')
        return redirect(url_for('papers_spot_go.students_answers'))
    elif request.method == 'GET':
        form.title.data = chat.title
        form.content.data = chat.content
    return render_template('papers/spot_go/student_chat/spot_go_create_chat.html', title='Spot-GO, update chat',
                           form=form, legend='Update chat')    

@papers_spot_go.route("/papers/spot_go/students_answers/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat_student(chat_id):
    chat = ChatSEP.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    db.session.delete(chat)
    db.session.commit()
    flash('Your chat has been deleted!', 'success')
    return redirect(url_for('papers_spot_go.students_answers'))   

@papers_spot_go.route("/papers/spot_go/students_answers/<string:username>")
@login_required
def user_chats_student(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = ChatSEP.query.filter_by(author=user)\
        .order_by(ChatSEP.date_posted.desc())\
        .paginate(page=page, per_page=2)
    return render_template('papers/spot_go/student_chat/spot_go_user_chats.html', chats=chats, user=user, func=read_image)  
