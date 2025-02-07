import json
from flask import render_template, url_for, Blueprint, request, redirect, flash, jsonify
from webse import application, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from webse.gender_platform_questionnaires.forms import QuestionnaireForm_1_q1, QuestionnaireForm_1_q2, QuestionnaireForm_1_q3, QuestionnaireForm_1_q4, ChatFormQuestionnaire
from webse.gender_platform_questionnaires.forms import QuestionnaireForm_2_q1, QuestionnaireForm_2_q2, QuestionnaireForm_2_q3, QuestionnaireForm_2_q4
from webse.gender_platform_questionnaires.forms import QuestionnaireForm_3_q1, QuestionnaireForm_3_q2, QuestionnaireForm_3_q3, QuestionnaireForm_3_q4
from webse.gender_platform_questionnaires.forms import QuestionnaireForm_4_q1, QuestionnaireForm_4_q2, QuestionnaireForm_4_q3, QuestionnaireForm_4_q4
from webse.models import QuestionnaireGender, QuestionnaireGenderChat, User
from webse.forward_users.utils import read_image
gender_platform_questionnaires= Blueprint('gender_platform_questionnaires', __name__)

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire_home', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire_home():
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire_home.html', title='Questionnaire') 


@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire1/q1', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire1_q1():
    form_1_q1 = QuestionnaireForm_1_q1()
    if form_1_q1.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
            filter(QuestionnaireGender.title_question == 'Question 1'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 1).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q1.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 1'
        questionnaire.title_question = 'Question 1'
        questionnaire.question_num = 1
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 1 has been submitted! Now, it is time to answer question 2', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire1_q2'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire1_q1.html', title='Questionnaire 1, q1', form_1_q1=form_1_q1) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire1/q2', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire1_q2():
    form_1_q2 = QuestionnaireForm_1_q2()
    if form_1_q2.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
            filter(QuestionnaireGender.title_question == 'Question 2'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 2).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q2.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 1'
        questionnaire.title_question = 'Question 2'
        questionnaire.question_num = 2
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 2 has been submitted! Now, it is time to answer question 3', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire1_q3'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire1_q2.html', title='Questionnaire 1, q2', form_1_q2=form_1_q2)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire1/q3', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire1_q3():
    form_1_q3 = QuestionnaireForm_1_q3()
    if form_1_q3.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
            filter(QuestionnaireGender.title_question == 'Question 3'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 3).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q3.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 1'
        questionnaire.title_question = 'Question 3'
        questionnaire.question_num = 3
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 3 has been submitted! Now, it is time to answer question 4', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire1_q4'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire1_q3.html', title='Questionnaire 1, q3', form_1_q3=form_1_q3)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire1/q4', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire1_q4():
    form_1_q4 = QuestionnaireForm_1_q4()
    if form_1_q4.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
            filter(QuestionnaireGender.title_question == 'Question 4'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 4).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q4.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 1'
        questionnaire.title_question = 'Question 4'
        questionnaire.question_num = 4
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 4 has been submitted! You have done with questionnaire 1', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire1_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire1_q4.html', title='Questionnaire 1, q4', form_1_q4=form_1_q4)       

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire1/summary', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire1_summary():
    # Question 1
    q1 = [0, 0, 0, 0]
    q1_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[0]=q1_strongly_agree

    q1_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[1]=q1_agree

    q1_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[2]=q1_disagree    

    q1_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q1[3]=q1_stongly_disagree  

    # Question 2
    q2 = [0, 0, 0, 0]
    q2_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[0]=q2_strongly_agree

    q2_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[1]=q2_agree

    q2_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[2]=q2_disagree    

    q2_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q2[3]=q2_stongly_disagree           

    # Question 3
    q3 = [0, 0, 0, 0]
    q3_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[0]=q3_strongly_agree

    q3_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[1]=q3_agree

    q3_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[2]=q3_disagree    

    q3_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q3[3]=q3_stongly_disagree 

    # Question 4
    q4 = [0, 0, 0, 0]
    q4_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[0]=q4_strongly_agree

    q4_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[1]=q4_agree

    q4_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[2]=q4_disagree    

    q4_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 1'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q4[3]=q4_stongly_disagree   

    page = request.args.get('page', 1, type=int)
    chats = QuestionnaireGenderChat.query.filter(QuestionnaireGenderChat.title_questionnaire == 'Questionnaire 1').\
        filter(QuestionnaireGenderChat.university == 'none').order_by(QuestionnaireGenderChat.date_chat.desc()).paginate(page=page, per_page=4)        
  
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire1_summary.html', title='Questionnaire 1, summary',
        q1_results=json.dumps(q1), q2_results=json.dumps(q2), q3_results=json.dumps(q3), q4_results=json.dumps(q4),
        chats=chats, func=read_image) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire1/summary/chat', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire1_summary_chat():
    form = ChatFormQuestionnaire()
    if form.validate_on_submit():
        chat =  QuestionnaireGenderChat(title_chat=form.title.data, title_questionnaire='Questionnaire 1', content=form.content.data, author=current_user,
                    university='none')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire1_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire1_create_chat.html', title='Questionnaire 1 - Chat',
                           form=form, legend='Questionnaire 1 - Professors')

# Quetionnaire 2
@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire2/q1', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire2_q1():
    form_1_q1 = QuestionnaireForm_2_q1()
    if form_1_q1.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
            filter(QuestionnaireGender.title_question == 'Question 1'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 1).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q1.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 2'
        questionnaire.title_question = 'Question 1'
        questionnaire.question_num = 1
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 1 has been submitted! Now, it is time to answer question 2', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire2_q2'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire2_q1.html', title='Questionnaire 2, q1', form_1_q1=form_1_q1) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire2/q2', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire2_q2():
    form_1_q2 = QuestionnaireForm_2_q2()
    if form_1_q2.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
            filter(QuestionnaireGender.title_question == 'Question 2'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 2).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q2.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 2'
        questionnaire.title_question = 'Question 2'
        questionnaire.question_num = 2
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 2 has been submitted! Now, it is time to answer question 3', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire2_q3'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire2_q2.html', title='Questionnaire 2, q2', form_1_q2=form_1_q2)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire2/q3', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire2_q3():
    form_1_q3 = QuestionnaireForm_2_q3()
    if form_1_q3.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
            filter(QuestionnaireGender.title_question == 'Question 3'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 3).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q3.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 2'
        questionnaire.title_question = 'Question 3'
        questionnaire.question_num = 3
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 3 has been submitted! Now, it is time to answer question 4', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire2_q4'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire2_q3.html', title='Questionnaire 2, q3', form_1_q3=form_1_q3)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire2/q4', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire2_q4():
    form_1_q4 = QuestionnaireForm_2_q4()
    if form_1_q4.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
            filter(QuestionnaireGender.title_question == 'Question 4'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 4).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q4.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 2'
        questionnaire.title_question = 'Question 4'
        questionnaire.question_num = 4
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 4 has been submitted! You have done with questionnaire 1', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire2_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire2_q4.html', title='Questionnaire 2, q4', form_1_q4=form_1_q4)       

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire2/summary', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire2_summary():
    # Question 1
    q1 = [0, 0, 0, 0]
    q1_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[0]=q1_strongly_agree

    q1_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[1]=q1_agree

    q1_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[2]=q1_disagree    

    q1_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q1[3]=q1_stongly_disagree  

    # Question 2
    q2 = [0, 0, 0, 0]
    q2_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[0]=q2_strongly_agree

    q2_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[1]=q2_agree

    q2_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[2]=q2_disagree    

    q2_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q2[3]=q2_stongly_disagree           

    # Question 3
    q3 = [0, 0, 0, 0]
    q3_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[0]=q3_strongly_agree

    q3_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[1]=q3_agree

    q3_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[2]=q3_disagree    

    q3_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q3[3]=q3_stongly_disagree 

    # Question 4
    q4 = [0, 0, 0, 0]
    q4_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[0]=q4_strongly_agree

    q4_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[1]=q4_agree

    q4_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[2]=q4_disagree    

    q4_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 2'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q4[3]=q4_stongly_disagree   

    page = request.args.get('page', 1, type=int)
    chats = QuestionnaireGenderChat.query.filter(QuestionnaireGenderChat.title_questionnaire == 'Questionnaire 2').\
        filter(QuestionnaireGenderChat.university == 'none').order_by(QuestionnaireGenderChat.date_chat.desc()).paginate(page=page, per_page=4)        
  
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire2_summary.html', title='Questionnaire 2, summary',
        q1_results=json.dumps(q1), q2_results=json.dumps(q2), q3_results=json.dumps(q3), q4_results=json.dumps(q4),
        chats=chats, func=read_image) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire2/summary/chat', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire2_summary_chat():
    form = ChatFormQuestionnaire()
    if form.validate_on_submit():
        chat =  QuestionnaireGenderChat(title_chat=form.title.data, title_questionnaire='Questionnaire 2', content=form.content.data, author=current_user,
                    university='none')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire2_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire2_create_chat.html', title='Questionnaire 2 - Chat',
                           form=form, legend='Questionnaire 2 - Students')                          

# Quetionnaire 3
@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire3/q1', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire3_q1():
    form_1_q1 = QuestionnaireForm_3_q1()
    if form_1_q1.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
            filter(QuestionnaireGender.title_question == 'Question 1'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 1).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q1.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 3'
        questionnaire.title_question = 'Question 1'
        questionnaire.question_num = 1
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 1 has been submitted! Now, it is time to answer question 2', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire3_q2'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire3_q1.html', title='Questionnaire 3, q1', form_1_q1=form_1_q1) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire3/q2', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire3_q2():
    form_1_q2 = QuestionnaireForm_3_q2()
    if form_1_q2.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
            filter(QuestionnaireGender.title_question == 'Question 2'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 2).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q2.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 3'
        questionnaire.title_question = 'Question 2'
        questionnaire.question_num = 2
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 2 has been submitted! Now, it is time to answer question 3', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire3_q3'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire3_q2.html', title='Questionnaire 3, q2', form_1_q2=form_1_q2)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire3/q3', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire3_q3():
    form_1_q3 = QuestionnaireForm_3_q3()
    if form_1_q3.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
            filter(QuestionnaireGender.title_question == 'Question 3'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 3).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q3.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 3'
        questionnaire.title_question = 'Question 3'
        questionnaire.question_num = 3
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 3 has been submitted! Now, it is time to answer question 4', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire3_q4'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire3_q3.html', title='Questionnaire 3, q3', form_1_q3=form_1_q3)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire3/q4', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire3_q4():
    form_1_q4 = QuestionnaireForm_3_q4()
    if form_1_q4.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
            filter(QuestionnaireGender.title_question == 'Question 4'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 4).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q4.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 3'
        questionnaire.title_question = 'Question 4'
        questionnaire.question_num = 4
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 4 has been submitted! You have done with questionnaire 1', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire3_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire3_q4.html', title='Questionnaire 3, q4', form_1_q4=form_1_q4)       

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire3/summary', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire3_summary():
    # Question 1
    q1 = [0, 0, 0, 0]
    q1_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[0]=q1_strongly_agree

    q1_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[1]=q1_agree

    q1_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[2]=q1_disagree    

    q1_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q1[3]=q1_stongly_disagree  

    # Question 2
    q2 = [0, 0, 0, 0]
    q2_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[0]=q2_strongly_agree

    q2_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[1]=q2_agree

    q2_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[2]=q2_disagree    

    q2_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q2[3]=q2_stongly_disagree           

    # Question 3
    q3 = [0, 0, 0, 0]
    q3_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[0]=q3_strongly_agree

    q3_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[1]=q3_agree

    q3_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[2]=q3_disagree    

    q3_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q3[3]=q3_stongly_disagree 

    # Question 4
    q4 = [0, 0, 0, 0]
    q4_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[0]=q4_strongly_agree

    q4_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[1]=q4_agree

    q4_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[2]=q4_disagree    

    q4_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 3'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q4[3]=q4_stongly_disagree   

    page = request.args.get('page', 1, type=int)
    chats = QuestionnaireGenderChat.query.filter(QuestionnaireGenderChat.title_questionnaire == 'Questionnaire 3').\
        filter(QuestionnaireGenderChat.university == 'none').order_by(QuestionnaireGenderChat.date_chat.desc()).paginate(page=page, per_page=4)        
  
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire3_summary.html', title='Questionnaire 3, summary',
        q1_results=json.dumps(q1), q2_results=json.dumps(q2), q3_results=json.dumps(q3), q4_results=json.dumps(q4),
        chats=chats, func=read_image) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire3/summary/chat', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire3_summary_chat():
    form = ChatFormQuestionnaire()
    if form.validate_on_submit():
        chat =  QuestionnaireGenderChat(title_chat=form.title.data, title_questionnaire='Questionnaire 3', content=form.content.data, author=current_user,
                    university='none')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire3_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire3_create_chat.html', title='Questionnaire 3 - Chat',
                           form=form, legend='Questionnaire 3 - Administrative Staff')

# Quetionnaire 4
@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire4/q1', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire4_q1():
    form_1_q1 = QuestionnaireForm_4_q1()
    if form_1_q1.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
            filter(QuestionnaireGender.title_question == 'Question 1'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 1).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q1.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 4'
        questionnaire.title_question = 'Question 1'
        questionnaire.question_num = 1
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 1 has been submitted! Now, it is time to answer question 2', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire4_q2'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire4_q1.html', title='Questionnaire 4, q1', form_1_q1=form_1_q1) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire4/q2', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire4_q2():
    form_1_q2 = QuestionnaireForm_4_q2()
    if form_1_q2.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
            filter(QuestionnaireGender.title_question == 'Question 2'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 2).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q2.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 4'
        questionnaire.title_question = 'Question 2'
        questionnaire.question_num = 2
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 2 has been submitted! Now, it is time to answer question 3', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire4_q3'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire4_q2.html', title='Questionnaire 4, q2', form_1_q2=form_1_q2)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire4/q3', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire4_q3():
    form_1_q3 = QuestionnaireForm_4_q3()
    if form_1_q3.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
            filter(QuestionnaireGender.title_question == 'Question 3'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 3).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q3.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 4'
        questionnaire.title_question = 'Question 3'
        questionnaire.question_num = 3
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 3 has been submitted! Now, it is time to answer question 4', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire4_q4'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire4_q3.html', title='Questionnaire 4, q3', form_1_q3=form_1_q3)   

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire4/q4', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire4_q4():
    form_1_q4 = QuestionnaireForm_4_q4()
    if form_1_q4.validate_on_submit():
        QuestionnaireGender.query.filter_by(author=current_user). \
            filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
            filter(QuestionnaireGender.title_question == 'Question 4'). \
            filter(QuestionnaireGender.university == 'none'). \
            filter(QuestionnaireGender.question_num == 4).delete()
        db.session.commit()
        questionnaire = QuestionnaireGender(question_str=form_1_q4.type.data, author = current_user)
        if questionnaire.question_str == 'Strongly agree':
            questionnaire.question_option = 1
        elif questionnaire.question_str == 'Agree':
            questionnaire.question_option = 2
        elif questionnaire.question_str == 'Disagree':
            questionnaire.question_option = 3  
        else:
            questionnaire.question_option = 4 
        questionnaire.title_questionnaire = 'Questionnaire 4'
        questionnaire.title_question = 'Question 4'
        questionnaire.question_num = 4
        questionnaire.university = 'none'
        db.session.add(questionnaire)
        db.session.commit()
        flash('Your answer to question 4 has been submitted! You have done with questionnaire 1', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire4_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire4_q4.html', title='Questionnaire 4, q4', form_1_q4=form_1_q4)       

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire4/summary', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire4_summary():
    # Question 1
    q1 = [0, 0, 0, 0]
    q1_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[0]=q1_strongly_agree

    q1_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[1]=q1_agree

    q1_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q1[2]=q1_disagree    

    q1_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 1).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q1[3]=q1_stongly_disagree  

    # Question 2
    q2 = [0, 0, 0, 0]
    q2_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[0]=q2_strongly_agree

    q2_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[1]=q2_agree

    q2_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q2[2]=q2_disagree    

    q2_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 2).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q2[3]=q2_stongly_disagree           

    # Question 3
    q3 = [0, 0, 0, 0]
    q3_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[0]=q3_strongly_agree

    q3_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[1]=q3_agree

    q3_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q3[2]=q3_disagree    

    q3_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 3).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q3[3]=q3_stongly_disagree 

    # Question 4
    q4 = [0, 0, 0, 0]
    q4_strongly_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 1). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[0]=q4_strongly_agree

    q4_agree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 2). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[1]=q4_agree

    q4_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 3). \
        order_by(QuestionnaireGender.question_num.asc()).count()
    q4[2]=q4_disagree    

    q4_stongly_disagree = QuestionnaireGender.query.filter(QuestionnaireGender.question_num == 4).\
        filter(QuestionnaireGender.title_questionnaire == 'Questionnaire 4'). \
        filter(QuestionnaireGender.university == 'none').filter(QuestionnaireGender.question_option == 4). \
        order_by(QuestionnaireGender.question_num.asc()).count()  
    q4[3]=q4_stongly_disagree   

    page = request.args.get('page', 1, type=int)
    chats = QuestionnaireGenderChat.query.filter(QuestionnaireGenderChat.title_questionnaire == 'Questionnaire 4').\
        filter(QuestionnaireGenderChat.university == 'none').order_by(QuestionnaireGenderChat.date_chat.desc()).paginate(page=page, per_page=4)        
  
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire4_summary.html', title='Questionnaire 4, summary',
        q1_results=json.dumps(q1), q2_results=json.dumps(q2), q3_results=json.dumps(q3), q4_results=json.dumps(q4),
        chats=chats, func=read_image) 

@gender_platform_questionnaires.route('/gender_platform/IWD/2023/questionnaire4/summary/chat', methods=['GET', 'POST'])
@login_required
def gender_platform_questionnaire4_summary_chat():
    form = ChatFormQuestionnaire()
    if form.validate_on_submit():
        chat =  QuestionnaireGenderChat(title_chat=form.title.data, title_questionnaire='Questionnaire 4', content=form.content.data, author=current_user,
                    university='none')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire4_summary'))
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire4_create_chat.html', title='Questionnaire 4 - Chat',
                           form=form, legend='Questionnaire 4 - Maintenance Staff')
                                                     
# These routes are common for all the chats
@gender_platform_questionnaires.route("/gender_platform/IWD/2023/questionnaire4/summary/chat/<int:chat_id>") 
def chat(chat_id):
    chat = QuestionnaireGenderChat.query.get_or_404(chat_id)
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire_chat.html', title=chat.title_chat, chat=chat, func=read_image)    

@gender_platform_questionnaires.route("/gender_platform/IWD/2023/questionnaire4/summary/chat/<int:chat_id>/update", methods=['GET', 'POST'])
@login_required
def update_chat(chat_id):
    chat = QuestionnaireGenderChat.query.get_or_404(chat_id)
    if chat.author != current_user:
        abort(403)
    form = ChatFormQuestionnaire()
    if chat.title_questionnaire=='Questionnaire 1':
        if form.validate_on_submit():
            chat.title_chat=form.title.data
            chat.content=form.content.data
            db.session.commit()
            flash('Your chat has been updated!', 'success')
            return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire1_summary'))
        elif request.method == 'GET':
            form.title.data = chat.title_chat
            form.content.data = chat.content
    elif chat.title_questionnaire=='Questionnaire 2':
        if form.validate_on_submit():
            chat.title_chat=form.title.data
            chat.content=form.content.data
            db.session.commit()
            flash('Your chat has been updated!', 'success')
            return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire2_summary'))
        elif request.method == 'GET':
            form.title.data = chat.title_chat
            form.content.data = chat.content 
    elif chat.title_questionnaire=='Questionnaire 3':
        if form.validate_on_submit():
            chat.title_chat=form.title.data
            chat.content=form.content.data
            db.session.commit()
            flash('Your chat has been updated!', 'success')
            return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire3_summary'))
        elif request.method == 'GET':
            form.title.data = chat.title_chat
            form.content.data = chat.content
    elif chat.title_questionnaire=='Questionnaire 4':
        if form.validate_on_submit():
            chat.title_chat=form.title.data
            chat.content=form.content.data
            db.session.commit()
            flash('Your chat has been updated!', 'success')
            return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire4_summary'))
        elif request.method == 'GET':
            form.title.data = chat.title_chat
            form.content.data = chat.content        
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire_create_chat.html', title='Update Chat',
                           form=form, legend='Update Chat')    

@gender_platform_questionnaires.route("/gender_platform/IWD/2023/questionnaire4/summary/chat/<int:chat_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_chat(chat_id):
    chat = QuestionnaireGenderChat.query.get_or_404(chat_id)
    if chat.title_questionnaire=='Questionnaire 1':
        if chat.author != current_user:
            abort(403)
        db.session.delete(chat)
        db.session.commit()
        flash('Your chat has been deleted!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire1_summary'))   
    elif chat.title_questionnaire=='Questionnaire 2':
        if chat.author != current_user:
            abort(403)
        db.session.delete(chat)
        db.session.commit()
        flash('Your chat has been deleted!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire2_summary')) 
    elif chat.title_questionnaire=='Questionnaire 3':
        if chat.author != current_user:
            abort(403)
        db.session.delete(chat)
        db.session.commit()
        flash('Your chat has been deleted!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire3_summary')) 
    elif chat.title_questionnaire=='Questionnaire 4':
        if chat.author != current_user:
            abort(403)
        db.session.delete(chat)
        db.session.commit()
        flash('Your chat has been deleted!', 'success')
        return redirect(url_for('gender_platform_questionnaires.gender_platform_questionnaire4_summary'))            

@gender_platform_questionnaires.route("/gender_platform/IWD/2023/questionnaire4/summary/chat/<string:username>")
@login_required
def user_chats(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    chats = QuestionnaireGenderChat.query.filter_by(author=user)\
        .order_by(QuestionnaireGenderChat.date_chat.desc())\
        .paginate(page=page, per_page=2)
    return render_template('gender_platform/questionnaires/gender_platform_questionnaire_user_chats.html', chats=chats, user=user, func=read_image)                              

                          
