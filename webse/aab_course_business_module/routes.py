from flask import render_template, url_for, Blueprint, request, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from webse import application, db, bcrypt, DBVAR
from webse.models import AnnouncementGD
from webse.models import Moduls
from webse.forward_users.utils import save_picture, read_image
from webse.aab_course_business_module.forms import ModulsForm_m2_ch1_e1, ModulsForm_m2_ch1_e2, ModulsForm_m2_ch1_e3, ModulsForm_m2_ch1_e4, \
    ModulsForm_m2_ch1_q1, ModulsForm_m2_ch1_q2, ModulsForm_m2_ch2_e1, ModulsForm_m2_ch2_e2, ModulsForm_m2_ch2_e3, ModulsForm_m2_ch2_e4, \
    ModulsForm_m2_ch2_q1, ModulsForm_m2_ch2_q2, ModulsForm_m2_ch2_q3, ModulsForm_m2_ch2_q4, ModulsForm_m2_ch2_q5, ModulsForm_m2_ch2_q6,\
    ModulsForm_m2_ch3_e1, ModulsForm_m2_ch3_e2
aab_course_business_module= Blueprint('aab_course_business_module', __name__)

# Business module
@aab_course_business_module.route('/sustainable_business_models_course/business_module')
def aab_course_business_module_home():
    return render_template('aab_course/aab_business_module/business_module_home.html', title='Sustainable Business Models Course, App Module')
  
#Chapter 1
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1', methods=['GET', 'POST'])
@login_required
def ch1(): 
    form_m2_ch1_q1 = ModulsForm_m2_ch1_q1()
    form_m2_ch1_q2 = ModulsForm_m2_ch1_q2()

    if form_m2_ch1_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_q1.type.data, author=current_user)
        if moduls.question_str == 'Buy green energy from another country':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch1. AAB Course Business Module. Smart Cities'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch1'))

    if form_m2_ch1_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_q2.type.data, author=current_user)
        if moduls.question_str == 'Focus only on the aesthetic':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch1. AAB Course Business Module. Smart Cities'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch1'))
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1.html', title='Auditing, Accounting and Business Course, Business Module,  ch1',
        form_m2_ch1_q1=form_m2_ch1_q1, form_m2_ch1_q2=form_m2_ch1_q2)  

#Chapter 1, Exercise 1.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def ch1_ex1_questionnaire():
    form_m2_ch1_e1 = ModulsForm_m2_ch1_e1()
    if form_m2_ch1_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_e1.type.data, author=current_user)
        if moduls.question_str == 'Reducing the waste of food in supermarkets and restaurants':
            moduls.question_option = 1
        elif moduls.question_str == 'Reducing transport carbon emissions and the public transport':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch1. AAB Course Business Module. Smart Cities'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch1_ex1_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex1_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - Ex1',
                           form_m2_ch1_e1=form_m2_ch1_e1)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch1_ex1_questionnaire_refresh():
    form_m2_ch1_e1 = ModulsForm_m2_ch1_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex1_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch1_e1=form_m2_ch1_e1)

#Chapter 1, Exercise 2.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def ch1_ex2_questionnaire():
    form_m2_ch1_e2 = ModulsForm_m2_ch1_e2()
    if form_m2_ch1_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_e2.type.data, author=current_user)
        if moduls.question_str == 'Yes, substantially':
            moduls.question_option = 1
        elif moduls.question_str == 'Yes, slightly':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch1. AAB Course Business Module. Smart Cities'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch1_ex2_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex2_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - ex2',
                           form_m2_ch1_e2=form_m2_ch1_e2)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch1_ex2_questionnaire_refresh():
    form_m2_ch1_e2 = ModulsForm_m2_ch1_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex2_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch1_e2=form_m2_ch1_e2)

#Chapter 1, Exercise 3.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex3/questionnaire', methods=['GET', 'POST'])
@login_required
def ch1_ex3_questionnaire():
    form_m2_ch1_e3 = ModulsForm_m2_ch1_e3()
    if form_m2_ch1_e3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_e3.type.data, author=current_user)
        if moduls.question_str == 'Yes, substantially':
            moduls.question_option = 1
        elif moduls.question_str == 'Yes, slightly':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch1. AAB Course Business Module. Smart Cities'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch1_ex3_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex3_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - ex3',
                           form_m2_ch1_e3=form_m2_ch1_e3)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex3/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch1_ex3_questionnaire_refresh():
    form_m2_ch1_e3 = ModulsForm_m2_ch1_e3()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex3_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - ex3',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch1_e3=form_m2_ch1_e3)

#Chapter 1, Exercise 4.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex4/questionnaire', methods=['GET', 'POST'])
@login_required
def ch1_ex4_questionnaire():
    form_m2_ch1_e4 = ModulsForm_m2_ch1_e4()
    if form_m2_ch1_e4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch1_e4.type.data, author=current_user)
        if moduls.question_str == 'Yes, substantially':
            moduls.question_option = 1
        elif moduls.question_str == 'Yes, slightly':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch1. AAB Course Business Module. Smart Cities'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch1_ex4_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex4_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - ex4',
                           form_m2_ch1_e4=form_m2_ch1_e4)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch1/ex4/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch1_ex4_questionnaire_refresh():
    form_m2_ch1_e4 = ModulsForm_m2_ch1_e4()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch1. AAB Course Business Module. Smart Cities'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch1/ch1_ex4_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch1 - ex4',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch1_e4=form_m2_ch1_e4)

#Chapter 2
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2', methods=['GET', 'POST'])
@login_required
def ch2():
    form_m2_ch2_q1 = ModulsForm_m2_ch2_q1()
    form_m2_ch2_q2 = ModulsForm_m2_ch2_q2()
    form_m2_ch2_q3 = ModulsForm_m2_ch2_q3()
    form_m2_ch2_q4 = ModulsForm_m2_ch2_q4()
    form_m2_ch2_q5 = ModulsForm_m2_ch2_q5()
    form_m2_ch2_q6 = ModulsForm_m2_ch2_q6()

    if form_m2_ch2_q1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module.  Digitalization and Energy'). \
            filter(Moduls.question_num == 1).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q1.type.data, author=current_user)
        if moduls.question_str == 'Electricity is produced in remote rural areas':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module.  Digitalization and Energy'
        moduls.question_num = 1
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2'))

    if form_m2_ch2_q2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module.  Digitalization and Energy'). \
            filter(Moduls.question_num == 2).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q2.type.data, author=current_user)
        if moduls.question_str == 'Long-term contracts reduce the incentives to restric output':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module.  Digitalization and Energy'
        moduls.question_num = 2
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2')) 

    if form_m2_ch2_q3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module.  Digitalization and Energy'). \
            filter(Moduls.question_num == 3).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q3.type.data, author=current_user)
        if moduls.question_str == 'Electricity consumption is stable during the day':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module.  Digitalization and Energy'
        moduls.question_num = 3
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2'))  

    if form_m2_ch2_q4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module.  Digitalization and Energy'). \
            filter(Moduls.question_num == 4).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q4.type.data, author=current_user)
        if moduls.question_str == 'Stable consumption in the industry':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module.  Digitalization and Energy'
        moduls.question_num = 4
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2')) 

    if form_m2_ch2_q5.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module.  Digitalization and Energy'). \
            filter(Moduls.question_num == 5).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q5.type.data, author=current_user)
        if moduls.question_str == 'Creates value to the customers that make upwards or downwards consumption':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module.  Digitalization and Energy'
        moduls.question_num = 5
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2'))  

    if form_m2_ch2_q6.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module.  Digitalization and Energy'). \
            filter(Moduls.question_num == 6).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_q6.type.data, author=current_user)
        if moduls.question_str == 'Solve the congestion problems in the grid at local level':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module.  Digitalization and Energy'
        moduls.question_num = 6
        moduls.question_option = 50
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2')) 

    return render_template('aab_course/aab_business_module/chapters/ch2/ch2.html', title='Auditing, Accounting and Business Course, Business Module, ch2',
        form_m2_ch2_q1=form_m2_ch2_q1, form_m2_ch2_q2=form_m2_ch2_q2, form_m2_ch2_q3=form_m2_ch2_q3, form_m2_ch2_q4=form_m2_ch2_q4,
        form_m2_ch2_q5=form_m2_ch2_q5, form_m2_ch2_q6=form_m2_ch2_q6) 

#Chapter 2, Exercise 1.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def ch2_ex1_questionnaire():
    form_m2_ch2_e1 = ModulsForm_m2_ch2_e1()
    if form_m2_ch2_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_e1.type.data, author=current_user)
        if moduls.question_str == 'Demand is difficult to forecast':
            moduls.question_option = 1
        elif moduls.question_str == 'Storage is prohibitively costly':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module. Energy and Digitalization'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2_ex1_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex1_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - Ex1',
                           form_m2_ch2_e1=form_m2_ch2_e1)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch2_ex1_questionnaire_refresh():
    form_m2_ch2_e1 = ModulsForm_m2_ch2_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex1_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch2_e1=form_m2_ch2_e1)

#Chapter 2, Exercise 2.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def ch2_ex2_questionnaire():
    form_m2_ch2_e2 = ModulsForm_m2_ch2_e2()
    if form_m2_ch2_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_e2.type.data, author=current_user)
        if moduls.question_str == 'The transmission line can be congested':
            moduls.question_option = 1
        elif moduls.question_str == 'Low demand elasticity':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module. Energy and Digitalization'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2_ex2_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex2_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - ex2',
                           form_m2_ch2_e2=form_m2_ch2_e2)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch2_ex2_questionnaire_refresh():
    form_m2_ch2_e2 = ModulsForm_m2_ch2_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex2_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch2_e2=form_m2_ch2_e2)

#Chapter 2, Exercise 3.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex3/questionnaire', methods=['GET', 'POST'])
@login_required
def ch2_ex3_questionnaire():
    form_m2_ch2_e3 = ModulsForm_m2_ch2_e3()
    if form_m2_ch2_e3.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_e3.type.data, author=current_user)
        if moduls.question_str == 'The introduction of sensors at home':
            moduls.question_option = 1
        elif moduls.question_str == 'The introduction of sensors in the grid':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module. Energy and Digitalization'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2_ex3_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex3_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - ex3',
                           form_m2_ch2_e3=form_m2_ch2_e3)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex3/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch2_ex3_questionnaire_refresh():
    form_m2_ch2_e3 = ModulsForm_m2_ch2_e3()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex3_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - ex3',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch2_e3=form_m2_ch2_e3)

#Chapter 2, Exercise 4.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex4/questionnaire', methods=['GET', 'POST'])
@login_required
def ch2_ex4_questionnaire():
    form_m2_ch2_e4 = ModulsForm_m2_ch2_e4()
    if form_m2_ch2_e4.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch2_e4.type.data, author=current_user)
        if moduls.question_str == 'Yes, substantially':
            moduls.question_option = 1
        elif moduls.question_str == 'Yes, slightly':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch2. AAB Course Business Module. Energy and Digitalization'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch2_ex4_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex4_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - ex4',
                           form_m2_ch2_e4=form_m2_ch2_e4)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch2/ex4/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch2_ex4_questionnaire_refresh():
    form_m2_ch2_e4 = ModulsForm_m2_ch2_e4()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch2. AAB Course Business Module. Energy and Digitalization'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch2/ch2_ex4_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch2 - ex4',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch2_e4=form_m2_ch2_e4)


#Chapter 3
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch3', methods=['GET', 'POST'])
@login_required
def ch3(): 
    return render_template('aab_course/aab_business_module/chapters/ch3/ch3.html', title='Auditing, Accounting and Business Course, Business Module, ch3') 

#Chapter 3, Exercise 1.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch3/ex1/questionnaire', methods=['GET', 'POST'])
@login_required
def ch3_ex1_questionnaire():
    form_m2_ch3_e1 = ModulsForm_m2_ch3_e1()
    if form_m2_ch3_e1.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_e1.type.data, author=current_user)
        if moduls.question_str == 'Access in real time to databases, information, and simulations':
            moduls.question_option = 1
        elif moduls.question_str == 'Better information from the consumers':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch3. AAB Course Business Module. Auditing and Digitalization'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch3_ex1_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch3/ch3_ex1_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch3 - Ex1',
                           form_m2_ch3_e1=form_m2_ch3_e1)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch3/ex1/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch3_ex1_questionnaire_refresh():
    form_m2_ch3_e1 = ModulsForm_m2_ch3_e1()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch3/ch3_ex1_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch3 - Ex1',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch3_e1=form_m2_ch3_e1)

#Chapter 3, Exercise 2.
@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch3/ex2/questionnaire', methods=['GET', 'POST'])
@login_required
def ch3_ex2_questionnaire():
    form_m2_ch3_e2 = ModulsForm_m2_ch3_e2()
    if form_m2_ch3_e2.validate_on_submit():
        Moduls.query.filter_by(author=current_user). \
            filter(Moduls.title_mo == 'AAB Course Business Module'). \
            filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
            filter(Moduls.question_num == 11).delete()
        db.session.commit()
        moduls = Moduls(question_str=form_m2_ch3_e2.type.data, author=current_user)
        if moduls.question_str == 'Statistical packages (e.g., R, Stata); programming languages (e.g., Python)':
            moduls.question_option = 1
        elif moduls.question_str == 'Excel with basic functionality':
            moduls.question_option = 2
        else:
            moduls.question_option = 3
        moduls.title_mo = 'AAB Course Business Module'
        moduls.title_ch = 'Ch3. AAB Course Business Module. Auditing and Digitalization'
        moduls.question_num = 11
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('aab_course_business_module.ch3_ex2_questionnaire'))
    return render_template('aab_course/aab_business_module/chapters/ch3/ch3_ex2_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch3 - ex2',
                           form_m2_ch3_e2=form_m2_ch3_e2)

@aab_course_business_module.route('/auditing_accounting_business_course/business_module/ch3/ex2/questionnaire/refresh', methods=['GET', 'POST'])
@login_required
def ch3_ex2_questionnaire_refresh():
    form_m2_ch3_e2 = ModulsForm_m2_ch3_e2()
    option_1 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
        filter(Moduls.question_option == 1). \
        order_by(Moduls.question_num.asc()).count()

    option_2 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
        filter(Moduls.question_option == 2). \
        order_by(Moduls.question_num.asc()).count()

    option_3 = Moduls.query.filter(Moduls.question_num == 11). \
        filter(Moduls.title_mo == 'AAB Course Business Module'). \
        filter(Moduls.title_ch == 'Ch3. AAB Course Business Module. Auditing and Digitalization'). \
        filter(Moduls.question_option == 3). \
        order_by(Moduls.question_num.asc()).count()
    return render_template('aab_course/aab_business_module/chapters/ch3/ch3_ex2_questionnaire.html', title='Auditing, Accounting and Business Course, Business Module,  ch3 - ex2',
                           option_1=option_1, option_2=option_2, option_3=option_3,
                           form_m2_ch3_e2=form_m2_ch3_e2)


  
