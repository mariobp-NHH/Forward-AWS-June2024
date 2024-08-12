from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image
from webse.gd_course_chapters.forms import ModulsForm_gdc_ch1_q1, ModulsForm_gdc_ch1_q2, ModulsForm_gdc_ch1_q3
from webse.gd_course_chapters.forms import ModulsForm_gdc_ch2_q1, ModulsForm_gdc_ch2_q2, ModulsForm_gdc_ch2_q3, ModulsForm_gdc_ch2_q4, ModulsForm_gdc_ch2_q5, ModulsForm_gdc_ch2_q6
from webse.gd_course_chapters.forms import ModulsForm_gdc_ch3_q1, ModulsForm_gdc_ch3_q2, ModulsForm_gdc_ch3_q3, ModulsForm_gdc_ch3_q4, ModulsForm_gdc_ch3_q5, ModulsForm_gdc_ch3_q6
from webse.gd_course_chapters.forms import ModulsForm_gdc_ch3_q7, ModulsForm_gdc_ch3_q8, ModulsForm_gdc_ch3_q9, ModulsForm_gdc_ch3_q10

gd_course_chapters= Blueprint('gd_course_chapters', __name__)

@gd_course_chapters.route('/green_digitalization_course/chapter1', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch1(): 
    form_gdc_ch1_q1 = ModulsForm_gdc_ch1_q1()
    form_gdc_ch1_q2 = ModulsForm_gdc_ch1_q2()
    form_gdc_ch1_q3 = ModulsForm_gdc_ch1_q3()

    if form_gdc_ch1_q1.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch1'). \
            filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
            filter(ModulsGD.question_num == 1).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch1_q1.type.data, author=current_user)
        if moduls.question_str == 'Add Python to environmental variables':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch1'
        moduls.title_ch = 'Chapter 1. Installation and First Flask App'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'ch1'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch1'))

    if form_gdc_ch1_q2.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch1'). \
            filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
            filter(ModulsGD.question_num == 2).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch1_q2.type.data, author=current_user)
        if moduls.question_str == 'Installing the basic tools in your virtual environment to run your first app':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch1'
        moduls.title_ch = 'Chapter 1. Installation and First Flask App'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'ch1'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch1'))

    if form_gdc_ch1_q3.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch1'). \
            filter(ModulsGD.title_ch == 'Chapter 1. Installation and First Flask App'). \
            filter(ModulsGD.question_num == 3).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch1_q3.type.data, author=current_user)
        if moduls.question_str == 'Both lines of code':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch1'
        moduls.title_ch = 'Chapter 1. Installation and First Flask App'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'ch1'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch1'))    
    return render_template('gd_course/chapters/ch1.html', title='Green Digitalization Course, ch1',
        form_gdc_ch1_q1=form_gdc_ch1_q1, form_gdc_ch1_q2=form_gdc_ch1_q2, form_gdc_ch1_q3=form_gdc_ch1_q3)

#Chapter 2
@gd_course_chapters.route('/green_digitalization_course/chapter2', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch2(): 
    form_gdc_ch2_q1 = ModulsForm_gdc_ch2_q1()
    form_gdc_ch2_q2 = ModulsForm_gdc_ch2_q2()
    form_gdc_ch2_q3 = ModulsForm_gdc_ch2_q3()
    form_gdc_ch2_q4 = ModulsForm_gdc_ch2_q4()
    form_gdc_ch2_q5 = ModulsForm_gdc_ch2_q5()
    form_gdc_ch2_q6 = ModulsForm_gdc_ch2_q6()

    if form_gdc_ch2_q1.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 1).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q1.type.data, author=current_user)
        if moduls.question_str == 'render_template':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))

    if form_gdc_ch2_q2.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 2).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q2.type.data, author=current_user)
        if moduls.question_str == '<title>{{title}}</title>':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))

    if form_gdc_ch2_q3.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 3).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q3.type.data, author=current_user)
        if moduls.question_str == '<ul><li>...</li></ul>':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))    

    if form_gdc_ch2_q4.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 4).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q4.type.data, author=current_user)
        if moduls.question_str == 'url_for':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))   

    if form_gdc_ch2_q5.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 5).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q4.type.data, author=current_user)
        if moduls.question_str == 'Jinja2 is the Flask template engine that allows us to render logical statements in our html files':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))  

    if form_gdc_ch2_q6.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch2'). \
            filter(ModulsGD.title_ch == 'Chapter 2. Structure and Templates'). \
            filter(ModulsGD.question_num == 6).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch2_q4.type.data, author=current_user)
        if moduls.question_str == '{% block content %} {% endblock %}':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch2'
        moduls.title_ch = 'Chapter 2. Structure and Templates'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'ch2'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch2'))          
    return render_template('gd_course/chapters/ch2.html', title='Green Digitalization Course, ch2',
        form_gdc_ch2_q1=form_gdc_ch2_q1, form_gdc_ch2_q2=form_gdc_ch2_q2, form_gdc_ch2_q3=form_gdc_ch2_q3,
        form_gdc_ch2_q4=form_gdc_ch2_q4, form_gdc_ch2_q5=form_gdc_ch2_q5, form_gdc_ch2_q6=form_gdc_ch2_q6)

#Chapter 3
@gd_course_chapters.route('/green_digitalization_course/chapter3', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch3():   
    form_gdc_ch3_q1 = ModulsForm_gdc_ch3_q1()
    form_gdc_ch3_q2 = ModulsForm_gdc_ch3_q2()
    form_gdc_ch3_q3 = ModulsForm_gdc_ch3_q3()
    form_gdc_ch3_q4 = ModulsForm_gdc_ch3_q4()   
    form_gdc_ch3_q5 = ModulsForm_gdc_ch3_q5()   
    form_gdc_ch3_q6 = ModulsForm_gdc_ch3_q6() 
    form_gdc_ch3_q7 = ModulsForm_gdc_ch3_q7() 
    form_gdc_ch3_q8 = ModulsForm_gdc_ch3_q8() 
    form_gdc_ch3_q9 = ModulsForm_gdc_ch3_q9() 
    form_gdc_ch3_q10 = ModulsForm_gdc_ch3_q10() 

    if form_gdc_ch3_q1.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 1).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q1.type.data, author=current_user)
        if moduls.question_str == 'It is used by search engine algorithms to list pages in search results':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))

    if form_gdc_ch3_q2.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 2).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q2.type.data, author=current_user)
        if moduls.question_str == 'The description of your web page, the authorship, or the viewport':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))

    if form_gdc_ch3_q3.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 3).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q3.type.data, author=current_user)
        if moduls.question_str == 'It defines the relationship between the current document and an external resource':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))    

    if form_gdc_ch3_q4.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 4).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q4.type.data, author=current_user)
        if moduls.question_str == 'The viewport is the user visible area of a web page':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        flash('Your answer has been submitted!', 'success')
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))

    if form_gdc_ch3_q5.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 5).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q5.type.data, author=current_user)
        if moduls.question_str == 'The padding and border of that element are included in the width and height':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))    

    if form_gdc_ch3_q6.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 6).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q6.type.data, author=current_user)
        if moduls.question_str == 'It always takes up the full width available':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3')) 
    if form_gdc_ch3_q7.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 7).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q7.type.data, author=current_user)
        if moduls.question_str == 'It is formatted as an inline element, but you can apply height and width values':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 7
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))    
    if form_gdc_ch3_q8.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 8).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q8.type.data, author=current_user)
        if moduls.question_str == 'justify-content: center;  align-items: center':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 8
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3')) 
    if form_gdc_ch3_q9.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 9).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q9.type.data, author=current_user)
        if moduls.question_str == 'How much a flex item will grow relative to the rest of the flex items':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 9
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))
    if form_gdc_ch3_q10.validate_on_submit():
        ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'ch3'). \
            filter(ModulsGD.title_ch == 'Chapter 3. HTML: Head and Body'). \
            filter(ModulsGD.question_num == 10).delete()
        db.session.commit()
        moduls = ModulsGD(question_str=form_gdc_ch3_q10.type.data, author=current_user)
        if moduls.question_str == 'The capability of the device':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'ch3'
        moduls.title_ch = 'Chapter 3. HTML: Head and Body'
        moduls.question_num = 10
        moduls.question_option = 50 
        moduls.question_section = 'ch3'       
        db.session.add(moduls)
        db.session.commit()
        return redirect(url_for('gd_course_chapters.gd_course_chapters_ch3'))  
    return render_template('gd_course/chapters/ch3.html', title='Green Digitalization Course, ch3',
        form_gdc_ch3_q1=form_gdc_ch3_q1, form_gdc_ch3_q2=form_gdc_ch3_q2, form_gdc_ch3_q3=form_gdc_ch3_q3,
        form_gdc_ch3_q4=form_gdc_ch3_q4, form_gdc_ch3_q5=form_gdc_ch3_q5, form_gdc_ch3_q6=form_gdc_ch3_q6,
        form_gdc_ch3_q7=form_gdc_ch3_q7, form_gdc_ch3_q8=form_gdc_ch3_q8, form_gdc_ch3_q9=form_gdc_ch3_q9,
        form_gdc_ch3_q10=form_gdc_ch3_q10)

@gd_course_chapters.route('/green_digitalization_course/chapter3/box_sizing')
@login_required
def gd_course_chapters_ch3_box_sizing():  
    return render_template('gd_course/chapters/ch3_box_sizing.html', title='Green Digitalization Course, ch3, box-sizing')

@gd_course_chapters.route('/green_digitalization_course/chapter3/block_inline')
@login_required
def gd_course_chapters_ch3_block_inline():  
    return render_template('gd_course/chapters/ch3_block_inline.html', title='Green Digitalization Course, ch3, block-inline')

@gd_course_chapters.route('/green_digitalization_course/chapter3/display')
@login_required
def gd_course_chapters_ch3_display():  
    return render_template('gd_course/chapters/ch3_display.html', title='Green Digitalization Course, ch3, display')

@gd_course_chapters.route('/green_digitalization_course/chapter3/css_flex_container')
@login_required
def gd_course_chapters_ch3_css_flex_container():  
    return render_template('gd_course/chapters/ch3_css_flex_container.html', title='Green Digitalization Course, ch3, css_flex_container')

@gd_course_chapters.route('/green_digitalization_course/chapter3/css_flex_items')
@login_required
def gd_course_chapters_ch3_css_flex_items():  
    return render_template('gd_course/chapters/ch3_css_flex_items.html', title='Green Digitalization Course, ch3, css_flex_items')

@gd_course_chapters.route('/green_digitalization_course/chapter3/media_query')
@login_required
def gd_course_chapters_ch3_media_query():  
    return render_template('gd_course/chapters/ch3_media_query.html', title='Green Digitalization Course, ch3, media_query')

@gd_course_chapters.route('/green_digitalization_course/chapter3/week1')
@login_required
def gd_course_chapters_ch3_week1():  
    return render_template('gd_course/chapters/ch3_week1.html', title='Green Digitalization Course, ch3, week1')

@gd_course_chapters.route('/green_digitalization_course/chapter3/week2')
@login_required
def gd_course_chapters_ch3_week2():  
    return render_template('gd_course/chapters/ch3_week2.html', title='Green Digitalization Course, ch3, week2')

#Chapter 4
@gd_course_chapters.route('/green_digitalization_course/chapter4', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch4(): 
    return render_template('gd_course/chapters/ch4.html', title='Green Digitalization Course, ch4') 

@gd_course_chapters.route('/green_digitalization_course/chapter4/home1')
@login_required
def gd_course_chapters_ch4_home1():  
    return render_template('gd_course/chapters/ch4_home1.html', title='Green Digitalization Course, ch4, home1') 

@gd_course_chapters.route('/green_digitalization_course/chapter4/methodology1')
@login_required
def gd_course_chapters_ch4_methodology1():  
    return render_template('gd_course/chapters/ch4_methodology1.html', title='Green Digitalization Course, ch4, methodology1') 

@gd_course_chapters.route('/green_digitalization_course/chapter4/carbon_app1')
@login_required
def gd_course_chapters_ch4_carbon_app1():  
    return render_template('gd_course/chapters/ch4_carbon_app1.html', title='Green Digitalization Course, ch4, carbon_app1')  

@gd_course_chapters.route('/green_digitalization_course/chapter4/home2')
@login_required
def gd_course_chapters_ch4_home2():  
    return render_template('gd_course/chapters/ch4_home2.html', title='Green Digitalization Course, ch4, home2') 

@gd_course_chapters.route('/green_digitalization_course/chapter4/methodology2')
@login_required
def gd_course_chapters_ch4_methodology2():  
    return render_template('gd_course/chapters/ch4_methodology2.html', title='Green Digitalization Course, ch4, methodology2') 

@gd_course_chapters.route('/green_digitalization_course/chapter4/carbon_app2')
@login_required
def gd_course_chapters_ch4_carbon_app2():  
    return render_template('gd_course/chapters/ch4_carbon_app2.html', title='Green Digitalization Course, ch4, carbon_app2')  

#Chapter 5
@gd_course_chapters.route('/green_digitalization_course/chapter5', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch5(): 
    return render_template('gd_course/chapters/ch5.html', title='Green Digitalization Course, ch5')   

@gd_course_chapters.route('/green_digitalization_course/chapter5/home')
@login_required
def gd_course_chapters_ch5_home():  
    return render_template('gd_course/chapters/ch5_home.html', title='Green Digitalization Course, ch5, home') 

@gd_course_chapters.route('/green_digitalization_course/chapter5/methodology')
@login_required
def gd_course_chapters_ch5_methodology():  
    return render_template('gd_course/chapters/ch5_methodology.html', title='Green Digitalization Course, ch5, methodology') 

@gd_course_chapters.route('/green_digitalization_course/chapter5/carbon_app')
@login_required
def gd_course_chapters_ch5_carbon_app():  
    return render_template('gd_course/chapters/ch5_carbon_app.html', title='Green Digitalization Course, ch5, carbon_app') 

#Chapter 6
@gd_course_chapters.route('/green_digitalization_course/chapter6', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch6(): 
    return render_template('gd_course/chapters/ch6.html', title='Green Digitalization Course, ch6') 

#Chapter 7
@gd_course_chapters.route('/green_digitalization_course/chapter7', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch7(): 
    return render_template('gd_course/chapters/ch7.html', title='Green Digitalization Course, ch7')   

#Chapter 8
@gd_course_chapters.route('/green_digitalization_course/chapter8', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch8(): 
    return render_template('gd_course/chapters/ch8.html', title='Green Digitalization Course, ch8') 

#Chapter 9
@gd_course_chapters.route('/green_digitalization_course/chapter9', methods=['GET', 'POST'])
@login_required
def gd_course_chapters_ch9(): 
    return render_template('gd_course/chapters/ch9.html', title='Green Digitalization Course, ch9')   

#Chapter 10
@gd_course_chapters.route('/green_digitalization_course/chapter10', methods=['GET', 'POST'])
def gd_course_chapters_ch10(): 
    return render_template('gd_course/chapters/ch10.html', title='Green Digitalization Course, ch10')  

#Midway Conference
@gd_course_chapters.route('/green_digitalization_course/conference', methods=['GET', 'POST'])
def gd_course_chapters_conference(): 
    return render_template('gd_course/chapters/conference.html', title='Green Digitalization Course, conference')   

#Chapter 11
@gd_course_chapters.route('/green_digitalization_course/chapter11', methods=['GET', 'POST'])
def gd_course_chapters_ch11(): 
    return render_template('gd_course/chapters/ch11.html', title='Green Digitalization Course, ch11')   

#Chapter 12
@gd_course_chapters.route('/green_digitalization_course/chapter12', methods=['GET', 'POST'])
def gd_course_chapters_ch12(): 
    return render_template('gd_course/chapters/ch12.html', title='Green Digitalization Course, ch12') 

#Chapter 13
@gd_course_chapters.route('/green_digitalization_course/chapter13', methods=['GET', 'POST'])
def gd_course_chapters_ch13(): 
    return render_template('gd_course/chapters/ch13.html', title='Green Digitalization Course, ch13') 

#Chapter 14
@gd_course_chapters.route('/green_digitalization_course/chapter14', methods=['GET', 'POST'])
def gd_course_chapters_ch14(): 
    return render_template('gd_course/chapters/ch14.html', title='Green Digitalization Course, ch14')   

#Lysdagen
@gd_course_chapters.route('/green_digitalization_course/lysdagen', methods=['GET', 'POST'])
def gd_course_chapters_lysdagen(): 
    return render_template('gd_course/chapters/lysdagen.html', title='Green Digitalization Course, lysdagen') 

#Haugesund
@gd_course_chapters.route('/green_digitalization_course/haugesund', methods=['GET', 'POST'])
def gd_course_chapters_haugesund(): 
    return render_template('gd_course/chapters/haugesund.html', title='Green Digitalization Course, haugesund') 
