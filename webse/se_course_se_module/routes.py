from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import db, DBVAR, mail
from webse.se_course_se_module.forms import ChatFormUpdate, ChatFormExercise
from webse.se_course_se_module.forms import ModulsForm_m2_ch1_e1, ModulsForm_m2_ch1_e2, ModulsForm_m2_ch1_q1, ModulsForm_m2_ch1_q2
from webse.se_course_se_module.forms import ModulsForm_m2_ch2_e1, ModulsForm_m2_ch2_e2, ModulsForm_m2_ch2_e3, \
    ModulsForm_m2_ch2_q1, ModulsForm_m2_ch2_q2
from webse.se_course_se_module.forms import ModulsForm_m2_ch2_q3, ModulsForm_m2_ch2_q4, ModulsForm_m2_ch2_q5, \
    ModulsForm_m2_ch2_q6, ModulsForm_m2_ch2_q7, ModulsForm_m2_ch2_q8
from webse.se_course_se_module.forms import ModulsForm_m2_ch3_e1, ModulsForm_m2_ch3_e2, ModulsForm_m2_ch3_q1, ModulsForm_m2_ch3_q2
from webse.se_course_se_module.forms import ModulsForm_m2_ch3_q3, ModulsForm_m2_ch3_q4, ModulsForm_m2_ch3_q5, \
    ModulsForm_m2_ch3_q6, ModulsForm_m2_ch3_q7, ModulsForm_m2_ch3_q8, ModulsForm_m2_ch3_q9
from webse.se_course_se_module.forms import ModulsForm_m2_ch4_e1, ModulsForm_m2_ch4_e2, ModulsForm_m2_ch4_q1, \
    ModulsForm_m2_ch4_q2, ModulsForm_m2_ch4_q3
from webse.se_course_se_module.forms import ModulsForm_m2_ch4_q4, ModulsForm_m2_ch4_q5, ModulsForm_m2_ch4_q6, \
    ModulsForm_m2_ch4_q7, ModulsForm_m2_ch4_q8, ModulsForm_m2_ch4_q9, ModulsForm_m2_ch4_q10
from webse.se_course_se_module.forms import ModulsForm_m2_ch5_e1, ModulsForm_m2_ch5_e2, ModulsForm_m2_ch5_q1, \
    ModulsForm_m2_ch5_q2, ModulsForm_m2_ch5_q3
from webse.se_course_se_module.forms import ModulsForm_m2_ch5_q4, ModulsForm_m2_ch5_q5, ModulsForm_m2_ch5_q6, \
    ModulsForm_m2_ch5_q7, ModulsForm_m2_ch5_q8, ModulsForm_m2_ch5_q9, ModulsForm_m2_ch5_q10, ModulsForm_m2_ch5_q11, ModulsForm_m2_ch5_q12
from webse.se_course_se_module.forms import ModulsForm_m2_ch6_e1, ModulsForm_m2_ch6_e2, ModulsForm_m2_ch6_q1, \
    ModulsForm_m2_ch6_q2, ModulsForm_m2_ch6_q3
from webse.se_course_se_module.forms import ModulsForm_m2_ch6_q4, ModulsForm_m2_ch6_q5, ModulsForm_m2_ch6_q6, \
    ModulsForm_m2_ch6_q7, ModulsForm_m2_ch6_q8, ModulsForm_m2_ch6_q9, ModulsForm_m2_ch6_q10, ModulsForm_m2_ch6_q11, ModulsForm_m2_ch6_q12
from webse.se_course_se_module.forms import ModulsForm_m2_ch7_e1, ModulsForm_m2_ch7_e2, ModulsForm_m2_ch7_q1, \
    ModulsForm_m2_ch7_q2, ModulsForm_m2_ch7_q3
from webse.se_course_se_module.forms import ModulsForm_m2_ch7_q4, ModulsForm_m2_ch7_q5, ModulsForm_m2_ch7_q6, \
    ModulsForm_m2_ch7_q7, ModulsForm_m2_ch7_q8, ModulsForm_m2_ch7_q9, ModulsForm_m2_ch7_q10, ModulsForm_m2_ch7_q11, ModulsForm_m2_ch7_q12
from webse.se_course_se_module.forms import ModulsForm_m2_ch8_e1, ModulsForm_m2_ch8_e2, ModulsForm_m2_ch8_e3, ModulsForm_m2_ch8_e4, ModulsForm_m2_ch8_q1, \
    ModulsForm_m2_ch8_q2, ModulsForm_m2_ch8_q3
from webse.se_course_se_module.forms import ModulsForm_m2_ch8_q4, ModulsForm_m2_ch8_q5, ModulsForm_m2_ch8_q6, \
    ModulsForm_m2_ch8_q7, ModulsForm_m2_ch8_q8, ModulsForm_m2_ch8_q9, ModulsForm_m2_ch8_q10, ModulsForm_m2_ch8_q11, ModulsForm_m2_ch8_q12
from webse.se_course_se_module.forms import ModulsForm_m2_ch9_e1, ModulsForm_m2_ch9_e2, ModulsForm_m2_ch9_e3, ModulsForm_m2_ch9_e4, ModulsForm_m2_ch9_q1, \
    ModulsForm_m2_ch9_q2, ModulsForm_m2_ch9_q3
from webse.se_course_se_module.forms import ModulsForm_m2_ch9_q4, ModulsForm_m2_ch9_q5, ModulsForm_m2_ch9_q6, \
    ModulsForm_m2_ch9_q7, ModulsForm_m2_ch9_q8, ModulsForm_m2_ch9_q9, ModulsForm_m2_ch9_q10, ModulsForm_m2_ch9_q11, ModulsForm_m2_ch9_q12
from webse.se_course_se_module.forms import ModulsForm_m2_ch10_e1, ModulsForm_m2_ch10_e2, ModulsForm_m2_ch10_e3, ModulsForm_m2_ch10_e4, ModulsForm_m2_ch10_q1, \
    ModulsForm_m2_ch10_q2, ModulsForm_m2_ch10_q3
from webse.se_course_se_module.forms import ModulsForm_m2_ch10_q4, ModulsForm_m2_ch10_q5, ModulsForm_m2_ch10_q6, \
    ModulsForm_m2_ch10_q7, ModulsForm_m2_ch10_q8, ModulsForm_m2_ch10_q9, ModulsForm_m2_ch10_q10, ModulsForm_m2_ch10_q11, ModulsForm_m2_ch10_q12
from webse.models import Moduls, Chat
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from flask_mail import Message

se_course_se_module = Blueprint('se_course_se_module', __name__)


@se_course_se_module.route('/sustainable_energy_web')
@login_required
def sustainable_energy_web():
    return render_template('se_course/se web/sustainable_energy_web.html', title='SE Web')


##########################################
## Sustainable Energy Module, Chapter 1 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch1', methods=['GET', 'POST'])
@login_required
def se_web_ch1():
    form_m2_ch1_q1 = ModulsForm_m2_ch1_q1()
    form_m2_ch1_q2 = ModulsForm_m2_ch1_q2()

    if form_m2_ch1_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Chapter 1. Frame'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_q1.type.data, author=current_user)
        if moduls.question_str == 'Should also consider social aspects':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Chapter 1. Frame'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch1'))

    if form_m2_ch1_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Chapter 1. Frame'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_q2.type.data, author=current_user)
        if moduls.question_str == 'Sustainability and economy are a subsystem of the ecosystem':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Chapter 1. Frame'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch1'))
    return render_template('se_course/se web/ch1/se_web_ch1.html', title='SE Web - Ch1',
                           form_m2_ch1_q1=form_m2_ch1_q1,
                           form_m2_ch1_q2=form_m2_ch1_q2)


# SE, Ch1, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch1/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex1():
    return render_template('se_course/se web/ch1/se_web_ch1_ex1.html', title='SE Web - Ch1 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch1/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex1_questionnaire():
    form_m2_ch1_e1 = ModulsForm_m2_ch1_e1()

    if form_m2_ch1_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Chapter 1. Frame'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_e1.type.data, author=current_user)
        if moduls.question_str == 'Should include only environmental pollution, carbon emissions':
            moduls.question_option = 1
        elif moduls.question_str == 'Should include only poverty alleviation, gender equality':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Chapter 1. Frame'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch1_ex1_questionnaire'))
    return render_template('se_course/se web/ch1/se_web_ch1_ex1_questionnaire.html', title='SE Web - Ch1 - Ex1',
                           form_m2_ch1_e1=form_m2_ch1_e1)


@se_course_se_module.route('/sustainable_energy_web/ch1/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex1_questionnaire_refresh():
    form_m2_ch1_e1 = ModulsForm_m2_ch1_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()


    return render_template('se_course/se web/ch1/se_web_ch1_ex1_questionnaire.html', title='SE Web - Ch1 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch1_e1=form_m2_ch1_e1)


@se_course_se_module.route('/sustainable_energy_web/ch1/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex1_chat():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user,
                    chat_module='SE_ch1_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch1_ex1_chat_query'))
    return render_template('se_course/se web/ch1/se_web_ch1_ex1_chat_create.html', title='SE Web - Ch1 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 1, Exercise 1')


@se_course_se_module.route('/sustainable_energy_web/ch1/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch1_ex1').order_by(Chat.date_posted.desc()).paginate(
            page=page,
            per_page=4)
    return render_template('se_course/se web/ch1/se_web_ch1_ex1_chat_query.html', title='SE Web - Ch1 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 1, Exercise 1', func=read_image)


# SE, Ch1, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch1/ex2', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex2():
    return render_template('se_course/se web/ch1/se_web_ch1_ex2.html', title='SE Web - Ch1 - ex2')


@se_course_se_module.route('/sustainable_energy_web/ch1/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex2_questionnaire():
    form_m2_ch1_e2 = ModulsForm_m2_ch1_e2()
    if form_m2_ch1_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Chapter 1. Frame'). \
            filter(Moduls.question_num == 22).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_e2.type.data, author=current_user, question_section=None)
        if moduls.question_str == 'Green Economy is more related to welfare and environmental economics':
            moduls.question_option = 1
        elif moduls.question_str == 'Green Economy is more related to ecological economics':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Chapter 1. Frame'
        moduls.question_num = 22
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch1_ex2_questionnaire'))
    return render_template('se_course/se web/ch1/se_web_ch1_ex2_questionnaire.html', title='SE Web - Ch1 - ex2',
                           form_m2_ch1_e2=form_m2_ch1_e2)


@se_course_se_module.route('/sustainable_energy_web/ch1/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex2_questionnaire_refresh():
    form_m2_ch1_e2 = ModulsForm_m2_ch1_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 22). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 22). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 22). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 1. Frame'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()

    return render_template('se_course/se web/ch1/se_web_ch1_ex2_questionnaire.html', title='SE Web - Ch1 - Ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch1_e2=form_m2_ch1_e2)


@se_course_se_module.route('/sustainable_energy_web/ch1/ex2/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex2_chat():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user,
                    chat_module='SE_ch1_ex2',
                    chat_group='Exercise 2')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch1_ex2_chat_query'))
    return render_template('se_course/se web/ch1/se_web_ch1_ex2_chat_create.html', title='SE Web - Ch1 - Ex2',
                           form=form, legend='Sustainable Energy, Chapter 1, Exercise 2')


@se_course_se_module.route('/sustainable_energy_web/ch1/ex2/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch1_ex2_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch1_ex2').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch1/se_web_ch1_ex2_chat_query.html', title='SE Web - Ch1 - ex2',
                           chats=chats, legend='Sustainable Energy, Chapter 1, Exercise 2', func=read_image)


##########################################
## Sustainable Energy Module, Chapter 2 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch2', methods=['GET', 'POST'])
@login_required
def se_web_ch2():
    form_m2_ch2_q1 = ModulsForm_m2_ch2_q1()
    form_m2_ch2_q2 = ModulsForm_m2_ch2_q2()
    form_m2_ch2_q3 = ModulsForm_m2_ch2_q3()
    form_m2_ch2_q4 = ModulsForm_m2_ch2_q4()
    form_m2_ch2_q5 = ModulsForm_m2_ch2_q5()
    form_m2_ch2_q6 = ModulsForm_m2_ch2_q6()
    form_m2_ch2_q7 = ModulsForm_m2_ch2_q7()
    form_m2_ch2_q8 = ModulsForm_m2_ch2_q8()

    if form_m2_ch2_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q1.type.data, author=current_user)
        if moduls.question_str == 'Biologically productive area it takes to satisfy the demands of people':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))

    if form_m2_ch2_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q2.type.data, author=current_user)
        if moduls.question_str == 'Land and sea area available to provide the resources a population consumes and to absorb its wastes':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))

    if form_m2_ch2_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q3.type.data, author=current_user)
        if moduls.question_str == 'Both':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))

    if form_m2_ch2_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q4.type.data, author=current_user)
        if moduls.question_str == 'Both':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))

    if form_m2_ch2_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q5.type.data, author=current_user)
        if moduls.question_str == 'Reflect the relative productivity of a given land use type':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))

    if form_m2_ch2_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q6.type.data, author=current_user)
        if moduls.question_str == 'Very suitable, suitable, moderately suitable, marginally suitable, and not suitable':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))

    if form_m2_ch2_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q7.type.data, author=current_user)
        if moduls.question_str == 'In the 70s':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))

    if form_m2_ch2_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q8.type.data, author=current_user)
        if moduls.question_str == 'It represents the 60%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch2. Ecological Footprint and Biocapacity'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2'))
    return render_template('se_course/se web/ch2/se_web_ch2.html', title='SE Web - Ch2',
                           form_m2_ch2_q1=form_m2_ch2_q1, form_m2_ch2_q2=form_m2_ch2_q2,
                           form_m2_ch2_q3=form_m2_ch2_q3, form_m2_ch2_q4=form_m2_ch2_q4,
                           form_m2_ch2_q5=form_m2_ch2_q5, form_m2_ch2_q6=form_m2_ch2_q6,
                           form_m2_ch2_q7=form_m2_ch2_q7, form_m2_ch2_q8=form_m2_ch2_q8)


# SE, Ch2, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch2/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex1():
    return render_template('se_course/se web/ch2/se_web_ch2_ex1.html', title='SE Web - ch2 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch2/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex1_questionnaire():
    form_m2_ch2_e1 = ModulsForm_m2_ch2_e1()

    if form_m2_ch2_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_e1.type.data, author=current_user)
        if moduls.question_str == 'The ecological footprint should be charged to Norway':
            moduls.question_option = 1
        elif moduls.question_str == 'The ecological footprint should be charged to Spain':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Chapter 2. Ecological Footprint and Biocapacity'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2_ex1_questionnaire'))
    return render_template('se_course/se web/ch2/se_web_ch2_ex1_questionnaire.html', title='SE Web - ch2 - Ex1',
                           form_m2_ch2_e1=form_m2_ch2_e1)


@se_course_se_module.route('/sustainable_energy_web/ch2/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex1_questionnaire_refresh():
    form_m2_ch2_e1 = ModulsForm_m2_ch2_e1()

    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch2/se_web_ch2_ex1_questionnaire.html', title='SE Web - ch2 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch2_e1=form_m2_ch2_e1)


@se_course_se_module.route('/sustainable_energy_web/ch2/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex1_chat():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user,
                    chat_module='SE_ch2_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2_ex1_chat_query'))
    return render_template('se_course/se web/ch2/se_web_ch2_ex1_chat_create.html', title='SE Web - ch2 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 2, Exercise 1')


@se_course_se_module.route('/sustainable_energy_web/ch2/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch2_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch2/se_web_ch2_ex1_chat_query.html', title='SE Web - ch2 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 2, Exercise 1', func=read_image)


# SE, Ch2, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch2/ex2', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex2():
    return render_template('se_course/se web/ch2/se_web_ch2_ex2.html', title='SE Web - ch2 - ex2')


@se_course_se_module.route('/sustainable_energy_web/ch2/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex2_questionnaire():
    form_m2_ch2_e2 = ModulsForm_m2_ch2_e2()

    if form_m2_ch2_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_e2.type.data, author=current_user)
        if moduls.question_str == 'Land to capture carbon emissions':
            moduls.question_option = 1
        elif moduls.question_str == 'Cropland, grazing land, fishing grounds, forest products land':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Chapter 2. Ecological Footprint and Biocapacity'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2_ex2_questionnaire'))
    return render_template('se_course/se web/ch2/se_web_ch2_ex2_questionnaire.html', title='SE Web - ch2 - ex2',
                           form_m2_ch2_e2=form_m2_ch2_e2)


@se_course_se_module.route('/sustainable_energy_web/ch2/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex2_questionnaire_refresh():
    form_m2_ch2_e2 = ModulsForm_m2_ch2_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch2/se_web_ch2_ex2_questionnaire.html', title='SE Web - ch2 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch2_e2=form_m2_ch2_e2)


@se_course_se_module.route('/sustainable_energy_web/ch2/ex2/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex2_chat():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user,
                    chat_module='SE_ch2_ex2',
                    chat_group='Exercise 2')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2_ex2_chat_query'))
    return render_template('se_course/se web/ch2/se_web_ch2_ex2_chat_create.html', title='SE Web - ch2 - ex2',
                           form=form, legend='Sustainable Energy, Chapter 2, Exercise 2')


@se_course_se_module.route('/sustainable_energy_web/ch2/ex2/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex2_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch2_ex2').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch2/se_web_ch2_ex2_chat_query.html', title='SE Web - ch2 - ex2',
                           chats=chats, legend='Sustainable Energy, Chapter 2, Exercise 2', func=read_image)


# SE, Ch2, Exercise 3.
@se_course_se_module.route('/sustainable_energy_web/ch2/ex3', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex3():
    return render_template('se_course/se web/ch2/se_web_ch2_ex3.html', title='SE Web - ch2 - ex3')


@se_course_se_module.route('/sustainable_energy_web/ch2/ex3/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex3_questionnaire():
    form_m2_ch2_e3 = ModulsForm_m2_ch2_e3()

    if form_m2_ch2_e3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_e3.type.data, author=current_user)
        if moduls.question_str == 'Land to capture carbon emissions':
            moduls.question_option = 1
        elif moduls.question_str == 'Cropland':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Chapter 2. Ecological Footprint and Biocapacity'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2_ex3_questionnaire'))

    return render_template('se_course/se web/ch2/se_web_ch2_ex3_questionnaire.html', title='SE Web - ch2 - ex3',
                           form_m2_ch2_e3=form_m2_ch2_e3)


@se_course_se_module.route('/sustainable_energy_web/ch2/ex3/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex3_questionnaire_refresh():
    form_m2_ch2_e3 = ModulsForm_m2_ch2_e3()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Chapter 2. Ecological Footprint and Biocapacity'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch2/se_web_ch2_ex3_questionnaire.html', title='SE Web - ch2 - ex3',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch2_e3=form_m2_ch2_e3)


@se_course_se_module.route('/sustainable_energy_web/ch2/ex3/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex3_chat():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user,
                    chat_module='SE_ch2_ex3',
                    chat_group='Exercise 3')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch2_ex3_chat_query'))
    return render_template('se_course/se web/ch2/se_web_ch2_ex3_chat_create.html', title='SE Web - ch2 - ex3',
                           form=form, legend='Sustainable Energy, Chapter 2, Exercise 3')


@se_course_se_module.route('/sustainable_energy_web/ch2/ex3/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch2_ex3_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch2_ex3').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch2/se_web_ch2_ex3_chat_query.html', title='SE Web - ch2 - ex3',
                           chats=chats, legend='Sustainable Energy, Chapter 2, Exercise 3', func=read_image)


##########################################
## Sustainable Energy Module, Chapter 3 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch3', methods=['GET', 'POST'])
@login_required
def se_web_ch3():
    form_m2_ch3_q1 = ModulsForm_m2_ch3_q1()
    form_m2_ch3_q2 = ModulsForm_m2_ch3_q2()
    form_m2_ch3_q3 = ModulsForm_m2_ch3_q3()
    form_m2_ch3_q4 = ModulsForm_m2_ch3_q4()
    form_m2_ch3_q5 = ModulsForm_m2_ch3_q5()
    form_m2_ch3_q6 = ModulsForm_m2_ch3_q6()
    form_m2_ch3_q7 = ModulsForm_m2_ch3_q7()
    form_m2_ch3_q8 = ModulsForm_m2_ch3_q8()
    form_m2_ch3_q9 = ModulsForm_m2_ch3_q9()

    if form_m2_ch3_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q1.type.data, author=current_user)
        if moduls.question_str == 'The debate about the starting date of the Antrophocene is still open':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q2.type.data, author=current_user)
        if moduls.question_str == 'Increase in arid areas':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q3.type.data, author=current_user)
        if moduls.question_str == 'Those elements do not interact with humans, and determine the relations of power and culture':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q2.type.data, author=current_user)
        if moduls.question_str == 'Biodiversity loss, climate crisis, and nitrogen cycle':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q5.type.data, author=current_user)
        if moduls.question_str == 'They are two interdependent imbalances that reinforce each other':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q6.type.data, author=current_user)
        if moduls.question_str == 'The cost of carbon in 2030 will be $75 per tonne of carbon dioxide in 2017 US dollars':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q7.type.data, author=current_user)
        if moduls.question_str == 'Multiplying the HDI by the arithmetic mean of carbon emissions and the ecological footprint':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q8.type.data, author=current_user)
        if moduls.question_str == 'The PHDI in country B is larger':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))

    if form_m2_ch3_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_q9.type.data, author=current_user)
        if moduls.question_str == 'It is closing the gap with the HDI':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3'))
    return render_template('se_course/se web/ch3/se_web_ch3.html', title='SE Web - ch3',
                           form_m2_ch3_q1=form_m2_ch3_q1, form_m2_ch3_q2=form_m2_ch3_q2,
                           form_m2_ch3_q3=form_m2_ch3_q3, form_m2_ch3_q4=form_m2_ch3_q4,
                           form_m2_ch3_q5=form_m2_ch3_q5, form_m2_ch3_q6=form_m2_ch3_q6,
                           form_m2_ch3_q7=form_m2_ch3_q7, form_m2_ch3_q8=form_m2_ch3_q8,
                           form_m2_ch3_q9=form_m2_ch3_q9)


# SE, Ch3, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch3/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex1():
    return render_template('se_course/se web/ch3/se_web_ch3_ex1.html', title='SE Web - ch3 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch3/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex1_questionnaire():
    form_m2_ch3_e1 = ModulsForm_m2_ch3_e1()

    if form_m2_ch3_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_e1.type.data, author=current_user)
        if moduls.question_str == 'At the beginning of the Agricultural Revolution 12.000–15.000 years ago':
            moduls.question_option = 1
        elif moduls.question_str == 'In 1945 after the detonation of the first atomic bomb':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3_ex1_questionnaire'))
    return render_template('se_course/se web/ch3/se_web_ch3_ex1_questionnaire.html', title='SE Web - ch3 - Ex1',
                           form_m2_ch3_e1=form_m2_ch3_e1)


@se_course_se_module.route('/sustainable_energy_web/ch3/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex1_questionnaire_refresh():
    form_m2_ch3_e1 = ModulsForm_m2_ch3_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch3/se_web_ch3_ex1_questionnaire.html', title='SE Web - ch3 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch3_e1=form_m2_ch3_e1)


@se_course_se_module.route('/sustainable_energy_web/ch3/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex1_chat():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user,
                    chat_module='SE_ch3_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3_ex1_chat_query'))
    return render_template('se_course/se web/ch3/se_web_ch3_ex1_chat_create.html', title='SE Web - ch3 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 3, Exercise 1')


@se_course_se_module.route('/sustainable_energy_web/ch3/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch3_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch3/se_web_ch3_ex1_chat_query.html', title='SE Web - ch3 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 3, Exercise 1', func=read_image)


# SE, Ch3, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch3/ex2', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex2():
    return render_template('se_course/se web/ch3/se_web_ch3_ex2.html', title='SE Web - ch3 - ex2')


@se_course_se_module.route('/sustainable_energy_web/ch3/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex2_questionnaire():
    form_m2_ch3_e2 = ModulsForm_m2_ch3_e2()

    if form_m2_ch3_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_e2.type.data, author=current_user)
        if moduls.question_str == 'Carbon emissions':
            moduls.question_option = 1
        elif moduls.question_str == 'Ecological Footprint':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch3. Human Development for the Anthropocene'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3_ex2_questionnaire'))
    return render_template('se_course/se web/ch3/se_web_ch3_ex2_questionnaire.html', title='SE Web - ch3 - ex2',
                           form_m2_ch3_e2=form_m2_ch3_e2)


@se_course_se_module.route('/sustainable_energy_web/ch3/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex2_questionnaire_refresh():
    form_m2_ch3_e2 = ModulsForm_m2_ch3_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch3. Human Development for the Anthropocene'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch3/se_web_ch3_ex2_questionnaire.html', title='SE Web - ch3 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch3_e2=form_m2_ch3_e2)


@se_course_se_module.route('/sustainable_energy_web/ch3/ex2/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex2_chat():
    form = ChatFormUpdate()
    if form.validate_on_submit():
        chat = Chat(title=form.title.data, content=form.content.data, author=current_user,
                    chat_module='SE_ch3_ex2',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch3_ex2_chat_query'))
    return render_template('se_course/se web/ch3/se_web_ch3_ex2_chat_create.html', title='SE Web - ch3 - ex2',
                           form=form, legend='Sustainable Energy, Chapter 3, Exercise 2')


@se_course_se_module.route('/sustainable_energy_web/ch3/ex2/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch3_ex2_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch3_ex2').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch3/se_web_ch3_ex2_chat_query.html', title='SE Web - ch3 - ex2',
                           chats=chats, legend='Sustainable Energy, Chapter 3, Exercise 2', func=read_image)


##########################################
## Sustainable Energy Module, Chapter 4 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch4', methods=['GET', 'POST'])
@login_required
def se_web_ch4():
    form_m2_ch4_q1 = ModulsForm_m2_ch4_q1()
    form_m2_ch4_q2 = ModulsForm_m2_ch4_q2()
    form_m2_ch4_q3 = ModulsForm_m2_ch4_q3()
    form_m2_ch4_q4 = ModulsForm_m2_ch4_q4()
    form_m2_ch4_q5 = ModulsForm_m2_ch4_q5()
    form_m2_ch4_q6 = ModulsForm_m2_ch4_q6()
    form_m2_ch4_q7 = ModulsForm_m2_ch4_q7()
    form_m2_ch4_q8 = ModulsForm_m2_ch4_q8()
    form_m2_ch4_q9 = ModulsForm_m2_ch4_q9()
    form_m2_ch4_q10 = ModulsForm_m2_ch4_q10()

    if form_m2_ch4_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q1.type.data, author=current_user)
        if moduls.question_str == 'Electrification, introduction of renewable energy, and energy efficiency':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q2.type.data, author=current_user)
        if moduls.question_str == 'Power sector, industry sector, transport sector and building sector':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q3.type.data, author=current_user)
        if moduls.question_str == 'The 86% of the electricity will be produced by using renewable energy':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q2.type.data, author=current_user)
        if moduls.question_str == '40% in the building sector, 33% in the industry sector, 22% in the transport sector':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q5.type.data, author=current_user)
        if moduls.question_str == 'Solar, wind, bioenergy and hydropower':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q6.type.data, author=current_user)
        if moduls.question_str == '1, EV; 2, hydrogen for heavy freight; 3, biofuels for road, aviation and marine transport':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q7.type.data, author=current_user)
        if moduls.question_str == 'Hydrogen and direct use of electricity for industrial heat and processes':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q8.type.data, author=current_user)
        if moduls.question_str == '1, Electric vehicles (EV); 2, biofuels heavy freight, for road, aviation and marine transport':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q9.type.data, author=current_user)
        if moduls.question_str == 'Investment, consumer expenditure, and trade':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 10
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))

    if form_m2_ch4_q10.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_q10.type.data, author=current_user)
        if moduls.question_str == 'It is closing the gap with the HDI':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4'))
    return render_template('se_course/se web/ch4/se_web_ch4.html', title='SE Web - ch4',
                           form_m2_ch4_q1=form_m2_ch4_q1, form_m2_ch4_q2=form_m2_ch4_q2,
                           form_m2_ch4_q3=form_m2_ch4_q3, form_m2_ch4_q4=form_m2_ch4_q4,
                           form_m2_ch4_q5=form_m2_ch4_q5, form_m2_ch4_q6=form_m2_ch4_q6,
                           form_m2_ch4_q7=form_m2_ch4_q7, form_m2_ch4_q8=form_m2_ch4_q8,
                           form_m2_ch4_q9=form_m2_ch4_q9, form_m2_ch4_q10=form_m2_ch4_q10)


# SE, ch4, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch4/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex1():
    return render_template('se_course/se web/ch4/se_web_ch4_ex1.html', title='SE Web - ch4 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch4/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex1_questionnaire():
    form_m2_ch4_e1 = ModulsForm_m2_ch4_e1()

    if form_m2_ch4_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_e1.type.data, author=current_user)
        if moduls.question_str == 'Electric vehicles, introduction of renewable energy, and energy efficiency':
            moduls.question_option = 1
        elif moduls.question_str == 'Electrification, introduction of renewable energy, and energy efficiency':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4_ex1_questionnaire'))
    return render_template('se_course/se web/ch4/se_web_ch4_ex1_questionnaire.html', title='SE Web - ch4 - Ex1',
                           form_m2_ch4_e1=form_m2_ch4_e1)


@se_course_se_module.route('/sustainable_energy_web/ch4/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex1_questionnaire_refresh():
    form_m2_ch4_e1 = ModulsForm_m2_ch4_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch4/se_web_ch4_ex1_questionnaire.html', title='SE Web - ch4 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch4_e1=form_m2_ch4_e1)


@se_course_se_module.route('/sustainable_energy_web/ch4/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex1_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 1', content=form.content.data, author=current_user,
                    chat_module='SE_ch4_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4_ex1_chat_query'))
    return render_template('se_course/se web/ch4/se_web_ch4_ex1_chat_create.html', title='SE Web - ch4 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 4, Exercise 1')


@se_course_se_module.route('/sustainable_energy_web/ch4/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch4_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch4/se_web_ch4_ex1_chat_query.html', title='SE Web - ch4 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 4, Exercise 1', func=read_image)


# SE, ch4, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch4/ex2', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex2():
    return render_template('se_course/se web/ch4/se_web_ch4_ex2.html', title='SE Web - ch4 - ex2')


@se_course_se_module.route('/sustainable_energy_web/ch4/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex2_questionnaire():
    form_m2_ch4_e2 = ModulsForm_m2_ch4_e2()

    if form_m2_ch4_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch4_e2.type.data, author=current_user)
        if moduls.question_str == 'Agricultural sector, car sector, steel sector and building sector':
            moduls.question_option = 1
        elif moduls.question_str == 'Power sector, car sector, chemical sector and building sector':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch4. Global Energy Transformation. A road map to 2050'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4_ex2_questionnaire'))
    return render_template('se_course/se web/ch4/se_web_ch4_ex2_questionnaire.html', title='SE Web - ch4 - ex2',
                           form_m2_ch4_e2=form_m2_ch4_e2)


@se_course_se_module.route('/sustainable_energy_web/ch4/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex2_questionnaire_refresh():
    form_m2_ch4_e2 = ModulsForm_m2_ch4_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch4. Global Energy Transformation. A road map to 2050'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch4/se_web_ch4_ex2_questionnaire.html', title='SE Web - ch4 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch4_e2=form_m2_ch4_e2)


@se_course_se_module.route('/sustainable_energy_web/ch4/ex2/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex2_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 2', content=form.content.data, author=current_user,
                    chat_module='SE_ch4_ex2',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch4_ex2_chat_query'))
    return render_template('se_course/se web/ch4/se_web_ch4_ex2_chat_create.html', title='SE Web - ch4 - ex2',
                           form=form, legend='Sustainable Energy, Chapter 4, Exercise 2')


@se_course_se_module.route('/sustainable_energy_web/ch4/ex2/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch4_ex2_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch4_ex2').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch4/se_web_ch4_ex2_chat_query.html', title='SE Web - ch4 - ex2',
                           chats=chats, legend='Sustainable Energy, Chapter 4, Exercise 2', func=read_image)

##########################################
## Sustainable Energy Module, Chapter 5 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch5', methods=['GET', 'POST'])
@login_required
def se_web_ch5():
    form_m2_ch5_q1 = ModulsForm_m2_ch5_q1()
    form_m2_ch5_q2 = ModulsForm_m2_ch5_q2()
    form_m2_ch5_q3 = ModulsForm_m2_ch5_q3()
    form_m2_ch5_q4 = ModulsForm_m2_ch5_q4()
    form_m2_ch5_q5 = ModulsForm_m2_ch5_q5()
    form_m2_ch5_q6 = ModulsForm_m2_ch5_q6()
    form_m2_ch5_q7 = ModulsForm_m2_ch5_q7()
    form_m2_ch5_q8 = ModulsForm_m2_ch5_q8()
    form_m2_ch5_q9 = ModulsForm_m2_ch5_q9()
    form_m2_ch5_q10 = ModulsForm_m2_ch5_q10()
    form_m2_ch5_q11 = ModulsForm_m2_ch5_q11()
    form_m2_ch5_q12 = ModulsForm_m2_ch5_q12()

    if form_m2_ch5_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q1.type.data, author=current_user)
        if moduls.question_str == 'Mass of wind that pass through an area A multiplied by the square of wind speed':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q2.type.data, author=current_user)
        if moduls.question_str == 'Measures actual production relative to possible production':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q3.type.data, author=current_user)
        if moduls.question_str == '45%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q2.type.data, author=current_user)
        if moduls.question_str == '59.3%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q5.type.data, author=current_user)
        if moduls.question_str == '35%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q6.type.data, author=current_user)
        if moduls.question_str == '5044 GW, 1000 GW':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q7.type.data, author=current_user)
        if moduls.question_str == '200 GW/yr, 45 GW/yr':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q8.type.data, author=current_user)
        if moduls.question_str == '650-1000 USD/KW, 1400-2800 USD/KW':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q9.type.data, author=current_user)
        if moduls.question_str == '0.02-0.03 USD/KWh, 0.03-0.07 USD/KWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q10.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 10).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q10.type.data, author=current_user)
        if moduls.question_str == '0.12 USD/KWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 10
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q11.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q11.type.data, author=current_user)
        if moduls.question_str == '32%-58%, 43%-60%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 11
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))

    if form_m2_ch5_q12.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 12).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_q12.type.data, author=current_user)
        if moduls.question_str == '6.06 M':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 12
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5'))
    return render_template('se_course/se web/ch5/se_web_ch5.html', title='SE Web - ch5',
                           form_m2_ch5_q1=form_m2_ch5_q1, form_m2_ch5_q2=form_m2_ch5_q2,
                           form_m2_ch5_q3=form_m2_ch5_q3, form_m2_ch5_q4=form_m2_ch5_q4,
                           form_m2_ch5_q5=form_m2_ch5_q5, form_m2_ch5_q6=form_m2_ch5_q6,
                           form_m2_ch5_q7=form_m2_ch5_q7, form_m2_ch5_q8=form_m2_ch5_q8,
                           form_m2_ch5_q9=form_m2_ch5_q9, form_m2_ch5_q10=form_m2_ch5_q10,
                           form_m2_ch5_q11=form_m2_ch5_q11, form_m2_ch5_q12=form_m2_ch5_q12)


# SE, ch5, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch5/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex1():
    return render_template('se_course/se web/ch5/se_web_ch5_ex1.html', title='SE Web - ch5 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch5/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex1_questionnaire():
    form_m2_ch5_e1 = ModulsForm_m2_ch5_e1()

    if form_m2_ch5_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_e1.type.data, author=current_user)
        if moduls.question_str == 'To minimize the weight of the turbine':
            moduls.question_option = 1
        elif moduls.question_str == 'To cover as much surface as possible and simultaneously minimize the cost of production':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5_ex1_questionnaire'))
    return render_template('se_course/se web/ch5/se_web_ch5_ex1_questionnaire.html', title='SE Web - ch5 - Ex1',
                           form_m2_ch5_e1=form_m2_ch5_e1)


@se_course_se_module.route('/sustainable_energy_web/ch5/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex1_questionnaire_refresh():
    form_m2_ch5_e1 = ModulsForm_m2_ch5_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch5/se_web_ch5_ex1_questionnaire.html', title='SE Web - ch5 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch5_e1=form_m2_ch5_e1)


@se_course_se_module.route('/sustainable_energy_web/ch5/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex1_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 1', content=form.content.data, author=current_user,
                    chat_module='SE_ch5_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5_ex1_chat_query'))
    return render_template('se_course/se web/ch5/se_web_ch5_ex1_chat_create.html', title='SE Web - ch5 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 5, Exercise 1')


@se_course_se_module.route('/sustainable_energy_web/ch5/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch5_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch5/se_web_ch5_ex1_chat_query.html', title='SE Web - ch5 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 5, Exercise 1', func=read_image)


# SE, ch5, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch5/ex2', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex2():
    return render_template('se_course/se web/ch5/se_web_ch5_ex2.html', title='SE Web - ch5 - ex2')


@se_course_se_module.route('/sustainable_energy_web/ch5/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex2_questionnaire():
    form_m2_ch5_e2 = ModulsForm_m2_ch5_e2()

    if form_m2_ch5_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch5_e2.type.data, author=current_user)
        if moduls.question_str == '30%':
            moduls.question_option = 1
        elif moduls.question_str == '35%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch5. Sustainable Energy. Wind Energy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5_ex2_questionnaire'))
    return render_template('se_course/se web/ch5/se_web_ch5_ex2_questionnaire.html', title='SE Web - ch5 - ex2',
                           form_m2_ch5_e2=form_m2_ch5_e2)


@se_course_se_module.route('/sustainable_energy_web/ch5/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex2_questionnaire_refresh():
    form_m2_ch5_e2 = ModulsForm_m2_ch5_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch5/se_web_ch5_ex2_questionnaire.html', title='SE Web - ch5 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch5_e2=form_m2_ch5_e2)


@se_course_se_module.route('/sustainable_energy_web/ch5/ex2/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex2_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 2', content=form.content.data, author=current_user,
                    chat_module='SE_ch5_ex2',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch5_ex2_chat_query'))
    return render_template('se_course/se web/ch5/se_web_ch5_ex2_chat_create.html', title='SE Web - ch5 - ex2',
                           form=form, legend='Sustainable Energy, Chapter 5, Exercise 2')


@se_course_se_module.route('/sustainable_energy_web/ch5/ex2/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch5_ex2_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch5_ex2').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch5/se_web_ch5_ex2_chat_query.html', title='SE Web - ch5 - ex2',
                           chats=chats, legend='Sustainable Energy, Chapter 5, Exercise 2', func=read_image)

@se_course_se_module.route('/sustainable_energy_web/ch5/email', methods=['GET', 'POST'])
@login_required
def ch5_email():
    entries = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).all()

    incorrect = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==0). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    correct = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_result==1). \
        filter(Moduls.title_mo=='Sustainable Energy'). \
        filter(Moduls.title_ch=='Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option==50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q1 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q1 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 1). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q2 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q2 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 2). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q3 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q3 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 3). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q4 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q4 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 4). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q5 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q5 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 5). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q6 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q6 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 6). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q7 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q7 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 7). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q8 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q8 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 8). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q9 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q9 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 9). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q10 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q10 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 10). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q11 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q11 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 11). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    incorrect_q12 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 0). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()

    correct_q12 = Moduls.query.filter_by(author=current_user). \
        filter(Moduls.question_num == 12). \
        filter(Moduls.question_result == 1). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch5. Sustainable Energy. Wind Energy'). \
        filter(Moduls.question_option == 50). \
        order_by(Moduls.question_num.asc()).count()
    flash('We have sent you an email with your statistics for chapter 5!', 'info')
    msg = Message('Your statistics',
                  sender='mblazquezdepaz@gmail.com',
                  recipients=[current_user.email])
    msg.body = f'''
Hello, your statistics for chapter 6 are in the next link ({url_for('se_course_statistics.statistics_se_ch5', _external=True)}), and below:
Hello, your statistics for chapter 6 are in the next link (https://forwardedu.org/sustainable_energy_web/statistics/se_ch5), and below:
Number of correct answers: {correct}.
Number of incorrect answers: {incorrect}.
Answer question 1 (where 0 means incorrect, and 1 means correct): {correct_q1}.
Answer question 2 (where 0 means incorrect, and 1 means correct): {correct_q2}.
Answer question 3 (where 0 means incorrect, and 1 means correct): {correct_q3}.
Answer question 4 (where 0 means incorrect, and 1 means correct): {correct_q4}.
Answer question 5 (where 0 means incorrect, and 1 means correct): {correct_q5}.
Answer question 6 (where 0 means incorrect, and 1 means correct): {correct_q6}.
Answer question 7 (where 0 means incorrect, and 1 means correct): {correct_q7}.
Answer question 8 (where 0 means incorrect, and 1 means correct): {correct_q8}.
Answer question 9 (where 0 means incorrect, and 1 means correct): {correct_q9}.
Answer question 10 (where 0 means incorrect, and 1 means correct): {correct_q10}.
Answer question 11 (where 0 means incorrect, and 1 means correct): {correct_q11}.
Answer question 12 (where 0 means incorrect, and 1 means correct): {correct_q12}.
'''
    mail.send(msg)
    return redirect(url_for('se_course_se_module.se_web_ch5'))




##########################################
## Sustainable Energy Module, Chapter 6 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch6', methods=['GET', 'POST'])
@login_required
def se_web_ch6():
    form_m2_ch6_q1 = ModulsForm_m2_ch6_q1()
    form_m2_ch6_q2 = ModulsForm_m2_ch6_q2()
    form_m2_ch6_q3 = ModulsForm_m2_ch6_q3()
    form_m2_ch6_q4 = ModulsForm_m2_ch6_q4()
    form_m2_ch6_q5 = ModulsForm_m2_ch6_q5()
    form_m2_ch6_q6 = ModulsForm_m2_ch6_q6()
    form_m2_ch6_q7 = ModulsForm_m2_ch6_q7()
    form_m2_ch6_q8 = ModulsForm_m2_ch6_q8()
    form_m2_ch6_q9 = ModulsForm_m2_ch6_q9()
    form_m2_ch6_q10 = ModulsForm_m2_ch6_q10()
    form_m2_ch6_q11 = ModulsForm_m2_ch6_q11()
    form_m2_ch6_q12 = ModulsForm_m2_ch6_q12()

    if form_m2_ch6_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q1.type.data, author=current_user)
        if moduls.question_str == 'The cost has dropped from 0.5 $/KWh to 0.01-0.02 $/KWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q2.type.data, author=current_user)
        if moduls.question_str == 'The cost has dropped from 1160 $/KWh to 176 $/KWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q3.type.data, author=current_user)
        if moduls.question_str == 'Non-concentrating collectors at home, while concentrating collectors in power plants':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q2.type.data, author=current_user)
        if moduls.question_str == 'CST is mainly used in the industry, while CSP is mainly used in generation':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q5.type.data, author=current_user)
        if moduls.question_str == '0.26':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q6.type.data, author=current_user)
        if moduls.question_str == '0.03':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q7.type.data, author=current_user)
        if moduls.question_str == 'Making the N-layer thin and heavily doped, and making the P-layer thick and poorly doped':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q8.type.data, author=current_user)
        if moduls.question_str == 'The combination of Amps and Volts that maximize Watts':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q9.type.data, author=current_user)
        if moduls.question_str == '8500 GW':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q10.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 10).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q10.type.data, author=current_user)
        if moduls.question_str == 'Asia 4800 GW, North-America 1720 GW, Europe 890 GW, Africa 670 GW':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 10
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q11.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q11.type.data, author=current_user)
        if moduls.question_str == 'From 4621 USD/KW in 2010 to 481-165 USD/KW in 2050':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 11
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))

    if form_m2_ch6_q12.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 12).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_q12.type.data, author=current_user)
        if moduls.question_str == '0.16 Euros/KWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 12
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6'))
    return render_template('se_course/se web/ch6/se_web_ch6.html', title='SE Web - ch6',
                           form_m2_ch6_q1=form_m2_ch6_q1, form_m2_ch6_q2=form_m2_ch6_q2,
                           form_m2_ch6_q3=form_m2_ch6_q3, form_m2_ch6_q4=form_m2_ch6_q4,
                           form_m2_ch6_q5=form_m2_ch6_q5, form_m2_ch6_q6=form_m2_ch6_q6,
                           form_m2_ch6_q7=form_m2_ch6_q7, form_m2_ch6_q8=form_m2_ch6_q8,
                           form_m2_ch6_q9=form_m2_ch6_q9, form_m2_ch6_q10=form_m2_ch6_q10,
                           form_m2_ch6_q11=form_m2_ch6_q11, form_m2_ch6_q12=form_m2_ch6_q12)


# SE, ch6, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch6/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex1():
    return render_template('se_course/se web/ch6/se_web_ch6_ex1.html', title='SE Web - ch6 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch6/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex1_questionnaire():
    form_m2_ch6_e1 = ModulsForm_m2_ch6_e1()

    if form_m2_ch6_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_e1.type.data, author=current_user)
        if moduls.question_str == '25%':
            moduls.question_option = 1
        elif moduls.question_str == '35%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6_ex1_questionnaire'))
    return render_template('se_course/se web/ch6/se_web_ch6_ex1_questionnaire.html', title='SE Web - ch6 - Ex1',
                           form_m2_ch6_e1=form_m2_ch6_e1)


@se_course_se_module.route('/sustainable_energy_web/ch6/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex1_questionnaire_refresh():
    form_m2_ch6_e1 = ModulsForm_m2_ch6_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch6/se_web_ch6_ex1_questionnaire.html', title='SE Web - ch6 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch6_e1=form_m2_ch6_e1)


@se_course_se_module.route('/sustainable_energy_web/ch6/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex1_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 1', content=form.content.data, author=current_user,
                    chat_module='SE_ch6_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6_ex1_chat_query'))
    return render_template('se_course/se web/ch6/se_web_ch6_ex1_chat_create.html', title='SE Web - Ch6 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 6, Exercise 1')


@se_course_se_module.route('/sustainable_energy_web/ch6/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch6_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch6/se_web_ch6_ex1_chat_query.html', title='SE Web - ch6 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 6, Exercise 1', func=read_image)


# SE, ch6, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch6/ex2', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex2():
    return render_template('se_course/se web/ch6/se_web_ch6_ex2.html', title='SE Web - ch6 - ex2')


@se_course_se_module.route('/sustainable_energy_web/ch6/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex2_questionnaire():
    form_m2_ch6_e2 = ModulsForm_m2_ch6_e2()

    if form_m2_ch6_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch6_e2.type.data, author=current_user)
        if moduls.question_str == 'From 0.37 USD/KWh to 0.085 USD/KWh':
            moduls.question_option = 1
        elif moduls.question_str == 'From 0.12 USD/KWh to 0.09 USD/KWh':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch6.  Sustainable Energy. Solar Energy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6_ex2_questionnaire'))
    return render_template('se_course/se web/ch6/se_web_ch6_ex2_questionnaire.html', title='SE Web - ch6 - ex2',
                           form_m2_ch6_e2=form_m2_ch6_e2)


@se_course_se_module.route('/sustainable_energy_web/ch6/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex2_questionnaire_refresh():
    form_m2_ch6_e2 = ModulsForm_m2_ch6_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch6.  Sustainable Energy. Solar Energy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch6/se_web_ch6_ex2_questionnaire.html', title='SE Web - ch6 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch6_e2=form_m2_ch6_e2)


@se_course_se_module.route('/sustainable_energy_web/ch6/ex2/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex2_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 2', content=form.content.data, author=current_user,
                    chat_module='SE_ch6_ex2',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch6_ex2_chat_query'))
    return render_template('se_course/se web/ch6/se_web_ch6_ex2_chat_create.html', title='SE Web - ch6 - ex2',
                           form=form, legend='Sustainable Energy, Chapter 6, Exercise 2')


@se_course_se_module.route('/sustainable_energy_web/ch6/ex2/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch6_ex2_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch6_ex2').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch6/se_web_ch6_ex2_chat_query.html', title='SE Web - ch6 - ex2',
                           chats=chats, legend='Sustainable Energy, Chapter 6, Exercise 2', func=read_image)

##########################################
## Sustainable Energy Module, Chapter 7 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch7', methods=['GET', 'POST'])
@login_required
def se_web_ch7():
    form_m2_ch7_q1 = ModulsForm_m2_ch7_q1()
    form_m2_ch7_q2 = ModulsForm_m2_ch7_q2()
    form_m2_ch7_q3 = ModulsForm_m2_ch7_q3()
    form_m2_ch7_q4 = ModulsForm_m2_ch7_q4()
    form_m2_ch7_q5 = ModulsForm_m2_ch7_q5()
    form_m2_ch7_q6 = ModulsForm_m2_ch7_q6()
    form_m2_ch7_q7 = ModulsForm_m2_ch7_q7()
    form_m2_ch7_q8 = ModulsForm_m2_ch7_q8()
    form_m2_ch7_q9 = ModulsForm_m2_ch7_q9()
    form_m2_ch7_q10 = ModulsForm_m2_ch7_q10()
    form_m2_ch7_q11 = ModulsForm_m2_ch7_q11()
    form_m2_ch7_q12 = ModulsForm_m2_ch7_q12()

    if form_m2_ch7_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q1.type.data, author=current_user)
        if moduls.question_str == 'Indonesia + UK':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q2.type.data, author=current_user)
        if moduls.question_str == 'Lower time to charge, and lower fuel storage requirements':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q3.type.data, author=current_user)
        if moduls.question_str == 'The electrons go into the water, and the H2 is produced by a reduction process':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q2.type.data, author=current_user)
        if moduls.question_str == 'Lossing two electrons':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q5.type.data, author=current_user)
        if moduls.question_str == 'Cell, stack, and system level':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q6.type.data, author=current_user)
        if moduls.question_str == 'Efficiency, current of the stack, durability, and investment cost':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q7.type.data, author=current_user)
        if moduls.question_str == '80% reduction electrolyser cost, electricity cost from 53 USD/MWh to 20 USD/MWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q8.type.data, author=current_user)
        if moduls.question_str == '30 USD/MWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q9.type.data, author=current_user)
        if moduls.question_str == 'Bionergy in the transport sector and CCS in industry sector':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q10.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 10).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q10.type.data, author=current_user)
        if moduls.question_str == 'Hydrogen can be used as an energy carrier, in fuel cells, and as a chemical':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 10
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q11.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q11.type.data, author=current_user)
        if moduls.question_str == 'Supply of electricity, demand of hydrogen, and flexibility of the electrolyser':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 11
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))

    if form_m2_ch7_q12.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 12).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_q12.type.data, author=current_user)
        if moduls.question_str == 'Seasonality of renewable energy production (mainly solar and wind)':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 12
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7'))
    return render_template('se_course/se web/ch7/se_web_ch7.html', title='SE Web - ch7',
                           form_m2_ch7_q1=form_m2_ch7_q1, form_m2_ch7_q2=form_m2_ch7_q2,
                           form_m2_ch7_q3=form_m2_ch7_q3, form_m2_ch7_q4=form_m2_ch7_q4,
                           form_m2_ch7_q5=form_m2_ch7_q5, form_m2_ch7_q6=form_m2_ch7_q6,
                           form_m2_ch7_q7=form_m2_ch7_q7, form_m2_ch7_q8=form_m2_ch7_q8,
                           form_m2_ch7_q9=form_m2_ch7_q9, form_m2_ch7_q10=form_m2_ch7_q10,
                           form_m2_ch7_q11=form_m2_ch7_q11, form_m2_ch7_q12=form_m2_ch7_q12)


# SE, ch7, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch7/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex1():
    return render_template('se_course/se web/ch7/se_web_ch7_ex1.html', title='SE Web - ch7 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch7/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex1_questionnaire():
    form_m2_ch7_e1 = ModulsForm_m2_ch7_e1()

    if form_m2_ch7_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_e1.type.data, author=current_user)
        if moduls.question_str == 'Cost of electrolysers, and cost of electricity':
            moduls.question_option = 1
        elif moduls.question_str == 'Cost of electrolysers and storage cost':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7_ex1_questionnaire'))
    return render_template('se_course/se web/ch7/se_web_ch7_ex1_questionnaire.html', title='SE Web - ch7 - Ex1',
                           form_m2_ch7_e1=form_m2_ch7_e1)


@se_course_se_module.route('/sustainable_energy_web/ch7/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex1_questionnaire_refresh():
    form_m2_ch7_e1 = ModulsForm_m2_ch7_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch7/se_web_ch7_ex1_questionnaire.html', title='SE Web - ch7 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch7_e1=form_m2_ch7_e1)


@se_course_se_module.route('/sustainable_energy_web/ch7/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex1_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 1', content=form.content.data, author=current_user,
                    chat_module='SE_ch7_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7_ex1_chat_query'))
    return render_template('se_course/se web/ch7/se_web_ch7_ex1_chat_create.html', title='SE Web - Ch7 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 7, Exercise 1')


@se_course_se_module.route('/sustainable_energy_web/ch7/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch7_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch7/se_web_ch7_ex1_chat_query.html', title='SE Web - Ch7 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 7, Exercise 1', func=read_image)


# SE, ch7, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch7/ex2', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex2():
    return render_template('se_course/se web/ch7/se_web_ch7_ex2.html', title='SE Web - ch7 - ex2')


@se_course_se_module.route('/sustainable_energy_web/ch7/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex2_questionnaire():
    form_m2_ch7_e2 = ModulsForm_m2_ch7_e2()

    if form_m2_ch7_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch7_e2.type.data, author=current_user)
        if moduls.question_str == 'Heavy industry and transport sector':
            moduls.question_option = 1
        elif moduls.question_str == 'Heavy industry and building sector':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch7.  Sustainable Energy. Hydrogen'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7_ex2_questionnaire'))
    return render_template('se_course/se web/ch7/se_web_ch7_ex2_questionnaire.html', title='SE Web - ch7 - ex2',
                           form_m2_ch7_e2=form_m2_ch7_e2)


@se_course_se_module.route('/sustainable_energy_web/ch7/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex2_questionnaire_refresh():
    form_m2_ch7_e2 = ModulsForm_m2_ch7_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch7.  Sustainable Energy. Hydrogen'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch7/se_web_ch7_ex2_questionnaire.html', title='SE Web - ch7 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch7_e2=form_m2_ch7_e2)


@se_course_se_module.route('/sustainable_energy_web/ch7/ex2/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex2_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 2', content=form.content.data, author=current_user,
                    chat_module='SE_ch7_ex2',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch7_ex2_chat_query'))
    return render_template('se_course/se web/ch7/se_web_ch7_ex2_chat_create.html', title='SE Web - Ch7 - ex2',
                           form=form, legend='Sustainable Energy, Chapter 7, Exercise 2')


@se_course_se_module.route('/sustainable_energy_web/ch7/ex2/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch7_ex2_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch7_ex2').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch7/se_web_ch7_ex2_chat_query.html', title='SE Web - Ch7 - ex2',
                           chats=chats, legend='Sustainable Energy, Chapter 7, Exercise 2', func=read_image)

##########################################
## Sustainable Energy Module, Chapter 8 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch8', methods=['GET', 'POST'])
@login_required
def se_web_ch8():
    form_m2_ch8_q1 = ModulsForm_m2_ch8_q1()
    form_m2_ch8_q2 = ModulsForm_m2_ch8_q2()
    form_m2_ch8_q3 = ModulsForm_m2_ch8_q3()
    form_m2_ch8_q4 = ModulsForm_m2_ch8_q4()
    form_m2_ch8_q5 = ModulsForm_m2_ch8_q5()
    form_m2_ch8_q6 = ModulsForm_m2_ch8_q6()
    form_m2_ch8_q7 = ModulsForm_m2_ch8_q7()
    form_m2_ch8_q8 = ModulsForm_m2_ch8_q8()
    form_m2_ch8_q9 = ModulsForm_m2_ch8_q9()
    form_m2_ch8_q10 = ModulsForm_m2_ch8_q10()
    form_m2_ch8_q11 = ModulsForm_m2_ch8_q11()
    form_m2_ch8_q12 = ModulsForm_m2_ch8_q12()

    if form_m2_ch8_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q1.type.data, author=current_user)
        if moduls.question_str == 'The reduction in methane emissions':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q2.type.data, author=current_user)
        if moduls.question_str == 'Incineration, and gasification to obtain biodiesel and hydrogen':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q3.type.data, author=current_user)
        if moduls.question_str == 'Downstream by taking the waste; upstream, by producing high-value products':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q2.type.data, author=current_user)
        if moduls.question_str == '21.6%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q5.type.data, author=current_user)
        if moduls.question_str == 'In the water-gas-shift process':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q6.type.data, author=current_user)
        if moduls.question_str == 'In the cleaning and upgrading process':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q7.type.data, author=current_user)
        if moduls.question_str == 'Providing heat used in the chemical and manufacturing processes':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q8.type.data, author=current_user)
        if moduls.question_str == 'Aviation and marine transport':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q9.type.data, author=current_user)
        if moduls.question_str == 'In biomass gasification processes with carbon capture storage':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q10.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 10).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q10.type.data, author=current_user)
        if moduls.question_str == '24%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 10
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q11.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q11.type.data, author=current_user)
        if moduls.question_str == '20%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 11
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))

    if form_m2_ch8_q12.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 12).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_q12.type.data, author=current_user)
        if moduls.question_str == 'Seasonality of renewable energy production (mainly solar and wind)':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 12
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8'))
    return render_template('se_course/se web/ch8/se_web_ch8.html', title='SE Web - ch8',
                           form_m2_ch8_q1=form_m2_ch8_q1, form_m2_ch8_q2=form_m2_ch8_q2,
                           form_m2_ch8_q3=form_m2_ch8_q3, form_m2_ch8_q4=form_m2_ch8_q4,
                           form_m2_ch8_q5=form_m2_ch8_q5, form_m2_ch8_q6=form_m2_ch8_q6,
                           form_m2_ch8_q7=form_m2_ch8_q7, form_m2_ch8_q8=form_m2_ch8_q8,
                           form_m2_ch8_q9=form_m2_ch8_q9, form_m2_ch8_q10=form_m2_ch8_q10,
                           form_m2_ch8_q11=form_m2_ch8_q11, form_m2_ch8_q12=form_m2_ch8_q12)


# SE, ch8, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch8/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex1():
    return render_template('se_course/se web/ch8/se_web_ch8_ex1.html', title='SE Web - ch8 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch8/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex1_questionnaire():
    form_m2_ch8_e1 = ModulsForm_m2_ch8_e1()

    if form_m2_ch8_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_e1.type.data, author=current_user)
        if moduls.question_str == 'Only in the gasification process':
            moduls.question_option = 1
        elif moduls.question_str == 'Only in the anaerobic digestion process':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8_ex1_questionnaire'))
    return render_template('se_course/se web/ch8/se_web_ch8_ex1_questionnaire.html', title='SE Web - ch8 - Ex1',
                           form_m2_ch8_e1=form_m2_ch8_e1)


@se_course_se_module.route('/sustainable_energy_web/ch8/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex1_questionnaire_refresh():
    form_m2_ch8_e1 = ModulsForm_m2_ch8_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch8/se_web_ch8_ex1_questionnaire.html', title='SE Web - ch8 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch8_e1=form_m2_ch8_e1)


@se_course_se_module.route('/sustainable_energy_web/ch8/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex1_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 1', content=form.content.data, author=current_user,
                    chat_module='SE_ch8_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8_ex1_chat_query'))
    return render_template('se_course/se web/ch8/se_web_ch8_ex1_chat_create.html', title='SE Web - ch8 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 8, Exercise')


@se_course_se_module.route('/sustainable_energy_web/ch8/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch8_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch8/se_web_ch8_ex1_chat_query.html', title='SE Web - ch8 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 8, Exercise', func=read_image)


# SE, ch8, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch8/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex2_questionnaire():
    form_m2_ch8_e2 = ModulsForm_m2_ch8_e2()

    if form_m2_ch8_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_e2.type.data, author=current_user)
        if moduls.question_str == '4%':
            moduls.question_option = 1
        elif moduls.question_str == '14%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8_ex2_questionnaire'))
    return render_template('se_course/se web/ch8/se_web_ch8_ex2_questionnaire.html', title='SE Web - ch8 - ex2',
                           form_m2_ch8_e2=form_m2_ch8_e2)


@se_course_se_module.route('/sustainable_energy_web/ch8/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex2_questionnaire_refresh():
    form_m2_ch8_e2 = ModulsForm_m2_ch8_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch8/se_web_ch8_ex2_questionnaire.html', title='SE Web - ch8 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch8_e2=form_m2_ch8_e2)

# SE, ch8, Exercise 3.
@se_course_se_module.route('/sustainable_energy_web/ch8/ex3/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex3_questionnaire():
    form_m2_ch8_e3 = ModulsForm_m2_ch8_e3()

    if form_m2_ch8_e3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_e3.type.data, author=current_user)
        if moduls.question_str == '10%':
            moduls.question_option = 1
        elif moduls.question_str == '20%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8_ex3_questionnaire'))
    return render_template('se_course/se web/ch8/se_web_ch8_ex3_questionnaire.html', title='SE Web - ch8 - ex3',
                           form_m2_ch8_e3=form_m2_ch8_e3)


@se_course_se_module.route('/sustainable_energy_web/ch8/ex3/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex3_questionnaire_refresh():
    form_m2_ch8_e3 = ModulsForm_m2_ch8_e3()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch8/se_web_ch8_ex3_questionnaire.html', title='SE Web - ch8 - ex3',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch8_e3=form_m2_ch8_e3)

# SE, ch8, Exercise 4.
@se_course_se_module.route('/sustainable_energy_web/ch8/ex4/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex4_questionnaire():
    form_m2_ch8_e4 = ModulsForm_m2_ch8_e4()

    if form_m2_ch8_e4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch8_e4.type.data, author=current_user)
        if moduls.question_str == '7%':
            moduls.question_option = 1
        elif moduls.question_str == '14%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch8. Sustainable Energy. Bioenergy'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch8_ex4_questionnaire'))
    return render_template('se_course/se web/ch8/se_web_ch8_ex4_questionnaire.html', title='SE Web - ch8 - ex4',
                           form_m2_ch8_e4=form_m2_ch8_e4)


@se_course_se_module.route('/sustainable_energy_web/ch8/ex4/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch8_ex4_questionnaire_refresh():
    form_m2_ch8_e4 = ModulsForm_m2_ch8_e4()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch8. Sustainable Energy. Bioenergy'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch8/se_web_ch8_ex4_questionnaire.html', title='SE Web - ch8 - ex4',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch8_e4=form_m2_ch8_e4)

##########################################
## Sustainable Energy Module, Chapter 9 ##
##########################################
@se_course_se_module.route('/sustainable_energy_web/ch9', methods=['GET', 'POST'])
@login_required
def se_web_ch9():
    form_m2_ch9_q1 = ModulsForm_m2_ch9_q1()
    form_m2_ch9_q2 = ModulsForm_m2_ch9_q2()
    form_m2_ch9_q3 = ModulsForm_m2_ch9_q3()
    form_m2_ch9_q4 = ModulsForm_m2_ch9_q4()
    form_m2_ch9_q5 = ModulsForm_m2_ch9_q5()
    form_m2_ch9_q6 = ModulsForm_m2_ch9_q6()
    form_m2_ch9_q7 = ModulsForm_m2_ch9_q7()
    form_m2_ch9_q8 = ModulsForm_m2_ch9_q8()
    form_m2_ch9_q9 = ModulsForm_m2_ch9_q9()
    form_m2_ch9_q10 = ModulsForm_m2_ch9_q10()
    form_m2_ch9_q11 = ModulsForm_m2_ch9_q11()
    form_m2_ch9_q12 = ModulsForm_m2_ch9_q12()

    if form_m2_ch9_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q1.type.data, author=current_user)
        if moduls.question_str == 'Battery life expectancy, charging stations, autonomy (kilometers without charging the battery)':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q2.type.data, author=current_user)
        if moduls.question_str == 'Levels 1 and 2: 2-20 miles per hour; level 3: 60-80 miles in 20 minutes':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q3.type.data, author=current_user)
        if moduls.question_str == 'Tesla':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q2.type.data, author=current_user)
        if moduls.question_str == 'The zinc bar becomes thinner':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q2.type.data, author=current_user)
        if moduls.question_str == 'The cooper bar becomes thicker':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q6.type.data, author=current_user)
        if moduls.question_str == 'Keep the charge in the zinc-sulfate and the copper-sulfate neutral to keep electrons moving':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q7.type.data, author=current_user)
        if moduls.question_str == '85% of the time the cars are parked':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q8.type.data, author=current_user)
        if moduls.question_str == '14TWh':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q9.type.data, author=current_user)
        if moduls.question_str == 'The energy needs of EVs represent no more than 10% to 15% of total electricity production':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q10.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 10).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q10.type.data, author=current_user)
        if moduls.question_str == 'The peak demand would increase by 19%':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 10
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q11.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q11.type.data, author=current_user)
        if moduls.question_str == 'All the enumerated measures':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 11
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))

    if form_m2_ch9_q12.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 12).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_q12.type.data, author=current_user)
        if moduls.question_str == 'V2G, second-life batteries, and smart buildings "as-a-service"':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 12
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9'))
    return render_template('se_course/se web/ch9/se_web_ch9.html', title='SE Web - ch9',
                           form_m2_ch9_q1=form_m2_ch9_q1, form_m2_ch9_q2=form_m2_ch9_q2,
                           form_m2_ch9_q3=form_m2_ch9_q3, form_m2_ch9_q4=form_m2_ch9_q4,
                           form_m2_ch9_q5=form_m2_ch9_q5, form_m2_ch9_q6=form_m2_ch9_q6,
                           form_m2_ch9_q7=form_m2_ch9_q7, form_m2_ch9_q8=form_m2_ch9_q8,
                           form_m2_ch9_q9=form_m2_ch9_q9, form_m2_ch9_q10=form_m2_ch9_q10,
                           form_m2_ch9_q11=form_m2_ch9_q11, form_m2_ch9_q12=form_m2_ch9_q12)


# SE, ch9, Exercise 1.
@se_course_se_module.route('/sustainable_energy_web/ch9/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex1():
    return render_template('se_course/se web/ch9/se_web_ch9_ex1.html', title='SE Web - ch9 - Ex1')


@se_course_se_module.route('/sustainable_energy_web/ch9/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex1_questionnaire():
    form_m2_ch9_e1 = ModulsForm_m2_ch9_e1()

    if form_m2_ch9_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_e1.type.data, author=current_user)
        if moduls.question_str == '75%':
            moduls.question_option = 1
        elif moduls.question_str == '80%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9_ex1_questionnaire'))
    return render_template('se_course/se web/ch9/se_web_ch9_ex1_questionnaire.html', title='SE Web - ch9 - Ex1',
                           form_m2_ch9_e1=form_m2_ch9_e1)


@se_course_se_module.route('/sustainable_energy_web/ch9/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex1_questionnaire_refresh():
    form_m2_ch9_e1 = ModulsForm_m2_ch9_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch9/se_web_ch9_ex1_questionnaire.html', title='SE Web - ch9 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch9_e1=form_m2_ch9_e1)


@se_course_se_module.route('/sustainable_energy_web/ch9/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex1_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 1', content=form.content.data, author=current_user,
                    chat_module='SE_ch9_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9_ex1_chat_query'))
    return render_template('se_course/se web/ch9/se_web_ch9_ex1_chat_create.html', title='SE Web - ch9 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 9, Exercise')


@se_course_se_module.route('/sustainable_energy_web/ch9/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch9_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch9/se_web_ch9_ex1_chat_query.html', title='SE Web - ch9 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 9, Exercise', func=read_image)


# SE, ch9, Exercise 2.
@se_course_se_module.route('/sustainable_energy_web/ch9/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex2_questionnaire():
    form_m2_ch9_e2 = ModulsForm_m2_ch9_e2()

    if form_m2_ch9_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_e2.type.data, author=current_user)
        if moduls.question_str == '25%':
            moduls.question_option = 1
        elif moduls.question_str == '30%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9_ex2_questionnaire'))
    return render_template('se_course/se web/ch9/se_web_ch9_ex2_questionnaire.html', title='SE Web - ch9 - ex2',
                           form_m2_ch9_e2=form_m2_ch9_e2)


@se_course_se_module.route('/sustainable_energy_web/ch9/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex2_questionnaire_refresh():
    form_m2_ch9_e2 = ModulsForm_m2_ch9_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch9/se_web_ch9_ex2_questionnaire.html', title='SE Web - ch9 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch9_e2=form_m2_ch9_e2)

# SE, ch9, Exercise 3.
@se_course_se_module.route('/sustainable_energy_web/ch9/ex3/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex3_questionnaire():
    form_m2_ch9_e3 = ModulsForm_m2_ch9_e3()

    if form_m2_ch9_e3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_e3.type.data, author=current_user)
        if moduls.question_str == '5 TWh':
            moduls.question_option = 1
        elif moduls.question_str == '8 TWh':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9_ex3_questionnaire'))
    return render_template('se_course/se web/ch9/se_web_ch9_ex3_questionnaire.html', title='SE Web - ch9 - ex3',
                           form_m2_ch9_e3=form_m2_ch9_e3)


@se_course_se_module.route('/sustainable_energy_web/ch9/ex3/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex3_questionnaire_refresh():
    form_m2_ch9_e3 = ModulsForm_m2_ch9_e3()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch9/se_web_ch9_ex3_questionnaire.html', title='SE Web - ch9 - ex3',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch9_e3=form_m2_ch9_e3)

# SE, ch9, Exercise 4.
@se_course_se_module.route('/sustainable_energy_web/ch9/ex4/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex4_questionnaire():
    form_m2_ch9_e4 = ModulsForm_m2_ch9_e4()

    if form_m2_ch9_e4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch9_e4.type.data, author=current_user)
        if moduls.question_str == '5%':
            moduls.question_option = 1
        elif moduls.question_str == '8%':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch9. Sustainable Energy. Batteries and EV'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch9_ex4_questionnaire'))
    return render_template('se_course/se web/ch9/se_web_ch9_ex4_questionnaire.html', title='SE Web - ch9 - ex4',
                           form_m2_ch9_e4=form_m2_ch9_e4)


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch9/ex4/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch9_ex4_questionnaire_refresh():
    form_m2_ch9_e4 = ModulsForm_m2_ch9_e4()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch9. Sustainable Energy. Batteries and EV'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch9/se_web_ch9_ex4_questionnaire.html', title='SE Web - ch9 - ex4',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch9_e4=form_m2_ch9_e4)

##########################################
## Sustainable Energy Module, Chapter 10 ##
##########################################
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10', methods=['GET', 'POST'])
@login_required
def se_web_ch10():
    form_m2_ch10_q1 = ModulsForm_m2_ch10_q1()
    form_m2_ch10_q2 = ModulsForm_m2_ch10_q2()
    form_m2_ch10_q3 = ModulsForm_m2_ch10_q3()
    form_m2_ch10_q4 = ModulsForm_m2_ch10_q4()
    form_m2_ch10_q5 = ModulsForm_m2_ch10_q5()
    form_m2_ch10_q6 = ModulsForm_m2_ch10_q6()
    form_m2_ch10_q7 = ModulsForm_m2_ch10_q7()
    form_m2_ch10_q8 = ModulsForm_m2_ch10_q8()
    form_m2_ch10_q9 = ModulsForm_m2_ch10_q9()
    form_m2_ch10_q10 = ModulsForm_m2_ch10_q10()
    form_m2_ch10_q11 = ModulsForm_m2_ch10_q11()
    form_m2_ch10_q12 = ModulsForm_m2_ch10_q12()

    if form_m2_ch10_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q1.type.data, author=current_user)
        if moduls.question_str == 'Direct carbon capture technologies are 50 times more expensive':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q2.type.data, author=current_user)
        if moduls.question_str == 'Enhanced oil recovery (EOR)':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q3.type.data, author=current_user)
        if moduls.question_str == '300-800 Dollars/Tonne':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q2.type.data, author=current_user)
        if moduls.question_str == 'A Carbon Capture and Utilisation technology (CCU)':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q2.type.data, author=current_user)
        if moduls.question_str == 'A CDR technology':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q6.type.data, author=current_user)
        if moduls.question_str == 'Both classifications could be possible':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q7.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 7).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q7.type.data, author=current_user)
        if moduls.question_str == 'The estimated cost of CCS in the iron and steel industry are USD 75–131/tCO2':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 7
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q8.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 8).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q8.type.data, author=current_user)
        if moduls.question_str == 'The estimated cost of CCS in the cement industry are USD 62–102/tCO2':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 8
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q9.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 9).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q9.type.data, author=current_user)
        if moduls.question_str == 'The estimated costs of bioenergy with carbon capture and storage are USD 69–105/tCO2':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 9
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q10.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 10).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q10.type.data, author=current_user)
        if moduls.question_str == 'CCS in the industry sector must reach 3.4 Gtpa by 2050':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 10
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q11.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q11.type.data, author=current_user)
        if moduls.question_str == 'Bioenergy with CCS must reach 4.5 Gtpa by 2050':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 11
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))

    if form_m2_ch10_q12.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 12).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_q12.type.data, author=current_user)
        if moduls.question_str == 'Cement, chemical, steel sectors and blue hydrogen':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 12
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10'))
    return render_template('se_course/se web/ch10/se_web_ch10.html', title='SE Web - ch10',
                           form_m2_ch10_q1=form_m2_ch10_q1, form_m2_ch10_q2=form_m2_ch10_q2,
                           form_m2_ch10_q3=form_m2_ch10_q3, form_m2_ch10_q4=form_m2_ch10_q4,
                           form_m2_ch10_q5=form_m2_ch10_q5, form_m2_ch10_q6=form_m2_ch10_q6,
                           form_m2_ch10_q7=form_m2_ch10_q7, form_m2_ch10_q8=form_m2_ch10_q8,
                           form_m2_ch10_q9=form_m2_ch10_q9, form_m2_ch10_q10=form_m2_ch10_q10,
                           form_m2_ch10_q11=form_m2_ch10_q11, form_m2_ch10_q12=form_m2_ch10_q12)


# SE, ch10, Exercise 1.
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex1', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex1():
    return render_template('se_course/se web/ch10/se_web_ch10_ex1.html', title='SE Web - ch10 - Ex1')


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex1_questionnaire():
    form_m2_ch10_e1 = ModulsForm_m2_ch10_e1()

    if form_m2_ch10_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_e1.type.data, author=current_user)
        if moduls.question_str == 'Production of synthetic fuels by combining CO2 and hydrogen':
            moduls.question_option = 1
        elif moduls.question_str == 'BECCS (bioenergy with carbon capture and storage)':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10_ex1_questionnaire'))
    return render_template('se_course/se web/ch10/se_web_ch10_ex1_questionnaire.html', title='SE Web - ch10 - Ex1',
                           form_m2_ch10_e1=form_m2_ch10_e1)


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex1_questionnaire_refresh():
    form_m2_ch10_e1 = ModulsForm_m2_ch10_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch10/se_web_ch10_ex1_questionnaire.html', title='SE Web - ch10 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch10_e1=form_m2_ch10_e1)


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex1/chat', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex1_chat():
    form = ChatFormExercise()
    if form.validate_on_submit():
        chat = Chat(title='Exercise 1', content=form.content.data, author=current_user,
                    chat_module='SE_ch10_ex1',
                    chat_group='Exercise 1')
        db.session.add(chat)
        db.session.commit()
        flash('Your chat has been created!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10_ex1_chat_query'))
    return render_template('se_course/se web/ch10/se_web_ch10_ex1_chat_create.html', title='SE Web - ch10 - Ex1',
                           form=form, legend='Sustainable Energy, Chapter 10, Exercise')


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex1/chat/query', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex1_chat_query():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter(Chat.chat_module == 'SE_ch10_ex1').order_by(Chat.date_posted.desc()).paginate(page=page,
                                                                                                           per_page=4)
    return render_template('se_course/se web/ch10/se_web_ch10_ex1_chat_query.html', title='SE Web - ch10 - Ex1',
                           chats=chats, legend='Sustainable Energy, Chapter 10, Exercise', func=read_image)


# SE, ch10, Exercise 2.
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex2_questionnaire():
    form_m2_ch10_e2 = ModulsForm_m2_ch10_e2()

    if form_m2_ch10_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_e2.type.data, author=current_user)
        if moduls.question_str == 'Capture':
            moduls.question_option = 1
        elif moduls.question_str == 'Transport':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10_ex2_questionnaire'))
    return render_template('se_course/se web/ch10/se_web_ch10_ex2_questionnaire.html', title='SE Web - ch10 - ex2',
                           form_m2_ch10_e2=form_m2_ch10_e2)


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex2_questionnaire_refresh():
    form_m2_ch10_e2 = ModulsForm_m2_ch10_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch10/se_web_ch10_ex2_questionnaire.html', title='SE Web - ch10 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch10_e2=form_m2_ch10_e2)

# SE, ch10, Exercise 3.
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex3/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex3_questionnaire():
    form_m2_ch10_e3 = ModulsForm_m2_ch10_e3()

    if form_m2_ch10_e3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_e3.type.data, author=current_user)
        if moduls.question_str == '100 Dollars/Tonne':
            moduls.question_option = 1
        elif moduls.question_str == '200 Dollars/Tonne':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10_ex3_questionnaire'))
    return render_template('se_course/se web/ch10/se_web_ch10_ex3_questionnaire.html', title='SE Web - ch10 - ex3',
                           form_m2_ch10_e3=form_m2_ch10_e3)


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex3/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex3_questionnaire_refresh():
    form_m2_ch10_e3 = ModulsForm_m2_ch10_e3()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch10/se_web_ch10_ex3_questionnaire.html', title='SE Web - ch10 - ex3',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch10_e3=form_m2_ch10_e3)

# SE, ch10, Exercise 4.
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex4/questionnaire', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex4_questionnaire():
    form_m2_ch10_e4 = ModulsForm_m2_ch10_e4()

    if form_m2_ch10_e4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'Sustainable Energy'). \
            filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch10_e4.type.data, author=current_user)
        if moduls.question_str == 'Transport and Industry':
            moduls.question_option = 1
        elif moduls.question_str == 'Power and building':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'Sustainable Energy'
        moduls.title_ch = 'Ch10. Sustainable Energy. Carbon Capture Storage'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('se_course_se_module.se_web_ch10_ex4_questionnaire'))
    return render_template('se_course/se web/ch10/se_web_ch10_ex4_questionnaire.html', title='SE Web - ch10 - ex4',
                           form_m2_ch10_e4=form_m2_ch10_e4)


@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch10/ex4/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def se_web_ch10_ex4_questionnaire_refresh():
    form_m2_ch10_e4 = ModulsForm_m2_ch10_e4()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'Sustainable Energy'). \
        filter(Moduls.title_ch == 'Ch10. Sustainable Energy. Carbon Capture Storage'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('se_course/se web/ch10/se_web_ch10_ex4_questionnaire.html', title='SE Web - ch10 - ex4',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch10_e4=form_m2_ch10_e4)

###########################################
## Sustainable Energy Module, Chapter 11 ##
###########################################
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch11', methods=['GET', 'POST'])
@login_required
def se_web_ch11():
    return render_template('se_course/se web/ch11/se_web_ch11.html', title='SE Web - ch11')

###########################################
## Sustainable Energy Module, Chapter 12 ##
###########################################
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch12', methods=['GET', 'POST'])
@login_required
def se_web_ch12():
    return render_template('se_course/se web/ch12/se_web_ch12.html', title='SE Web - ch12')

###########################################
## Sustainable Energy Module, Chapter 13 ##
###########################################
@se_course_se_module.route('/sustainable_energy_course/sustainable_energy_web/ch13', methods=['GET', 'POST'])
@login_required
def se_web_ch13():
    return render_template('se_course/se web/ch13/se_web_ch13.html', title='SE Web - ch13')
