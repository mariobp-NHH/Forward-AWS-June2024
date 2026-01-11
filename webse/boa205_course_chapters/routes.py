from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

""" Forms """
""" chapter 1 """
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch1_q1, ModulsForm_boa205_ch1_q2, ModulsForm_boa205_ch1_q3, ModulsForm_boa205_ch1_q4, ModulsForm_boa205_ch1_q5, ModulsForm_boa205_ch1_q6,TableForm_boa205_ch1_t1
""" chapter 2a """
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch2_q1, ModulsForm_boa205_ch2_q2, ModulsForm_boa205_ch2_q3, ModulsForm_boa205_ch2_q4, TableForm_boa205_ch2_t1, TableForm_boa205_ch2_t2
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch2_q5, ModulsForm_boa205_ch2_q6, ModulsForm_boa205_ch2_q7, ModulsForm_boa205_ch2_q8, ModulsForm_boa205_ch2_q9, ModulsForm_boa205_ch2_q10
""" chapter 2b """
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch2b_q1, ModulsForm_boa205_ch2b_q2, ModulsForm_boa205_ch2b_q3, ModulsForm_boa205_ch2b_q4
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch2b_q5, ModulsForm_boa205_ch2b_q6, TableForm_boa205_ch2b_t1, TableForm_boa205_ch2b_t2
""" chapter 3 """
from webse.boa205_course_chapters.forms import TableForm_boa205_ch3_t1, TableForm_boa205_ch3_t2,TableForm_boa205_ch3_t3,TableForm_boa205_ch3_t4, ModulsForm_boa205_ch3_q1
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch3_q2, ModulsForm_boa205_ch3_q3, ModulsForm_boa205_ch3_q4, ModulsForm_boa205_ch3_q5, ModulsForm_boa205_ch3_q6
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch3_q7, ModulsForm_boa205_ch3_q8, ModulsForm_boa205_ch3_q9, ModulsForm_boa205_ch3_q10

""" Functions """
""" chapter 2a """
from webse.boa205_course_chapters.functions import normal, virkelig, dekningsdiff, produksjonresultat_normal, avvik, produktresultat_selv, virkelig_selv, dekningsdiff_produksjonresultat_selv
from webse.boa205_course_chapters.functions import produktresultat_bidra
""" chapter 2b """
from webse.boa205_course_chapters.functions import ch2a_selv,ch2a_bidra
""" chapter 3 """
from webse.boa205_course_chapters.functions import ch3_materialregnskap, ch3_lonnregnskap, ch3_standard_selv_table,ch3_selvksot_table,ch3_bidrakost_table,ch3_differanse_table
from webse.boa205_course_chapters.functions import ch3_virkelige_t4

boa205_course_chapters= Blueprint('boa205_course_chapters', __name__)

#Chapter 1
@boa205_course_chapters.route('/boa205_course/kapitel1', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch1():
    form_boa205_ch1_q1 = ModulsForm_boa205_ch1_q1()
    form_boa205_ch1_q2 = ModulsForm_boa205_ch1_q2()
    form_boa205_ch1_q3 = ModulsForm_boa205_ch1_q3()
    form_boa205_ch1_q4 = ModulsForm_boa205_ch1_q4()
    form_boa205_ch1_q5 = ModulsForm_boa205_ch1_q5()
    form_boa205_ch1_q6 = ModulsForm_boa205_ch1_q6()
    form_boa205_ch1_t1=TableForm_boa205_ch1_t1()
    
    if form_boa205_ch1_q1.validate_on_submit():
        number_answers_by_author_q1=ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'boa205_ch1'). \
            filter(ModulsGD.title_ch == 'Kapitel 1. Hva er et driftsregnskap?'). \
            filter(ModulsGD.question_num == 1).count()
        moduls = ModulsGD(question_str=form_boa205_ch1_q1.type.data, author=current_user)
        if moduls.question_str == 'kr -20 000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch1'
        moduls.title_ch = 'Kapitel 1. Hva er et driftsregnskap?'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch1'       
        db.session.add(moduls)
        db.session.commit()
        """ keep_first_and_last(
            author=current_user,
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            question_num=1
        ) """
        return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4, 
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6, form_boa205_ch1_t1=form_boa205_ch1_t1, 
                           legend='Variabler', anchor="ch1_q1_q2",
                           number_answers_by_author_q1=number_answers_by_author_q1)
    
    if form_boa205_ch1_q2.validate_on_submit():
        """ ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'boa205_ch1'). \
            filter(ModulsGD.title_ch == 'Kapitel 1. Hva er et driftsregnskap?'). \
            filter(ModulsGD.question_num == 2).delete()
        db.session.commit() """
        moduls = ModulsGD(question_str=form_boa205_ch1_q2.type.data, author=current_user)
        if moduls.question_str == 'Mindre enn kr 5 000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch1'
        moduls.title_ch = 'Kapitel 1. Hva er et driftsregnskap?'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch1'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4,
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6,
                           form_boa205_ch1_t1=form_boa205_ch1_t1, 
                           legend='Variabler', anchor="ch1_q1_q2")
    
    if form_boa205_ch1_q3.validate_on_submit():
        """ ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'boa205_ch1'). \
            filter(ModulsGD.title_ch == 'Kapitel 1. Hva er et driftsregnskap?'). \
            filter(ModulsGD.question_num == 3).delete()
        db.session.commit() """
        moduls = ModulsGD(question_str=form_boa205_ch1_q3.type.data, author=current_user)
        if moduls.question_str == 'kr -169 000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch1'
        moduls.title_ch = 'Kapitel 1. Hva er et driftsregnskap?'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch1'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4, 
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6, form_boa205_ch1_t1=form_boa205_ch1_t1, 
                           legend='Variabler', anchor="ch1_q3_q4")
    
    if form_boa205_ch1_q4.validate_on_submit():
        """ ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'boa205_ch1'). \
            filter(ModulsGD.title_ch == 'Kapitel 1. Hva er et driftsregnskap?'). \
            filter(ModulsGD.question_num == 4).delete()
        db.session.commit() """
        moduls = ModulsGD(question_str=form_boa205_ch1_q4.type.data, author=current_user)
        if moduls.question_str == 'kr -45 000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch1'
        moduls.title_ch = 'Kapitel 1. Hva er et driftsregnskap?'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch1'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4, 
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6, form_boa205_ch1_t1=form_boa205_ch1_t1, 
                           legend='Variabler', anchor="ch1_q3_q4")
    
    if form_boa205_ch1_q5.validate_on_submit():
        """ ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'boa205_ch1'). \
            filter(ModulsGD.title_ch == 'Kapitel 1. Hva er et driftsregnskap?'). \
            filter(ModulsGD.question_num == 5).delete()
        db.session.commit() """
        moduls = ModulsGD(question_str=form_boa205_ch1_q5.type.data, author=current_user)
        if moduls.question_str == 'kr -134 998':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch1'
        moduls.title_ch = 'Kapitel 1. Hva er et driftsregnskap?'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch1'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4, 
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6, form_boa205_ch1_t1=form_boa205_ch1_t1, 
                           legend='Variabler', anchor="ch1_q5_q6")
    
    if form_boa205_ch1_q6.validate_on_submit():
        """ ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'boa205_ch1'). \
            filter(ModulsGD.title_ch == 'Kapitel 1. Hva er et driftsregnskap?'). \
            filter(ModulsGD.question_num == 6).delete()
        db.session.commit() """
        moduls = ModulsGD(question_str=form_boa205_ch1_q5.type.data, author=current_user)
        if moduls.question_str == 'kr 23 000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch1'
        moduls.title_ch = 'Kapitel 1. Hva er et driftsregnskap?'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch1'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4, 
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6, form_boa205_ch1_t1=form_boa205_ch1_t1, 
                           legend='Variabler', anchor="ch1_q5_q6")
    
    if form_boa205_ch1_t1.validate_on_submit():
        """ Constants """
        inntekter_taxi1=800000
        inntekter_taxi2=900000
        inntekter_taxi3=1000000
        inntekter_taxi_sum=2700000

        drivstoff_taxi1=165000
        drivstoff_taxi2=175000
        drivstoff_taxi3=200000
        drivstoff_taxi_sum=540000

        lønn_taxi1=320000
        lønn_taxi2=360000
        lønn_taxi3=0
        lønn_taxi_sum=680000

        service_taxi1=45000
        service_taxi2=50000
        service_taxi3=65000
        service_taxi_sum=160000

        garasjeleie_taxi1=25000
        garasjeleie_taxi2=25000
        garasjeleie_taxi3=25000
        garasjeleie_taxi_sum=75000

        bilvask_taxi1=10000
        bilvask_taxi2=10000
        bilvask_taxi3=10000
        bilvask_taxi_sum=30000

        forsikringer_taxi1=55000
        forsikringer_taxi2=55000
        forsikringer_taxi3=55000
        forsikringer_taxi_sum=165000

        diverse_taxi1=5000
        diverse_taxi2=5000
        diverse_taxi3=5000
        diverse_taxi_sum=15000

        """ Variables """
        renter = form_boa205_ch1_t1.renter.data
        eierlonn = form_boa205_ch1_t1.eierlonn.data
        salgsverdi = form_boa205_ch1_t1.salgsverdi.data
        ar = form_boa205_ch1_t1.ar.data

        """ Kalkulatoriske koster """
        kalkulatoriske_avskrvning= int((520000-float(salgsverdi))/float(ar))
        kalkulatoriske_renter = int(1200000*float(renter)/3)
        kalkulatoriske_lonn= int(float(eierlonn))
        
        kalkulatoriske_avskrvning_sum= 3*kalkulatoriske_avskrvning
        kalkulatoriske_renter_sum = 3*kalkulatoriske_renter

        """ Sum kostnader """
        sum_kostnader_taxi1=drivstoff_taxi1+lønn_taxi1+service_taxi1+garasjeleie_taxi1+bilvask_taxi1+forsikringer_taxi1+diverse_taxi1+kalkulatoriske_avskrvning+kalkulatoriske_renter
        sum_kostnader_taxi2=drivstoff_taxi2+lønn_taxi2+service_taxi2+garasjeleie_taxi2+bilvask_taxi2+forsikringer_taxi2+diverse_taxi2+kalkulatoriske_avskrvning+kalkulatoriske_renter
        sum_kostnader_taxi3=drivstoff_taxi3+lønn_taxi3+service_taxi3+garasjeleie_taxi3+bilvask_taxi3+forsikringer_taxi3+diverse_taxi3+kalkulatoriske_avskrvning+kalkulatoriske_renter+kalkulatoriske_lonn
        sum_kostnader_taxi_sum=drivstoff_taxi_sum+lønn_taxi_sum+service_taxi_sum+garasjeleie_taxi_sum+bilvask_taxi_sum+forsikringer_taxi_sum+diverse_taxi_sum+kalkulatoriske_avskrvning_sum+kalkulatoriske_renter_sum+kalkulatoriske_lonn
        
        """ Driftsresultat """
        driftsresultat_taxi1=inntekter_taxi1-sum_kostnader_taxi1
        driftsresultat_taxi2=inntekter_taxi2-sum_kostnader_taxi2
        driftsresultat_taxi3=inntekter_taxi3-sum_kostnader_taxi3
        driftsresultat_taxi_sum=inntekter_taxi_sum-sum_kostnader_taxi_sum

        """ Form information """
        form_boa205_ch1_t1.renter.data = renter
        form_boa205_ch1_t1.eierlonn.data = eierlonn
        form_boa205_ch1_t1.salgsverdi.data = salgsverdi
        form_boa205_ch1_t1.ar.data = ar

        """ Table 2 """
        restultat_eksternregnskap=735000
        avskrivning_eksternregnskap=300000
        resultat_internregnskap= restultat_eksternregnskap+avskrivning_eksternregnskap-kalkulatoriske_avskrvning_sum-kalkulatoriske_renter_sum-kalkulatoriske_lonn

        return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4, 
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6,form_boa205_ch1_t1=form_boa205_ch1_t1, 
                           renter=renter, salgsverdi=salgsverdi, eierlonn=eierlonn, ar=ar,
                           kalkulatoriske_avskrvning=kalkulatoriske_avskrvning, kalkulatoriske_renter=kalkulatoriske_renter,
                           kalkulatoriske_lonn=kalkulatoriske_lonn, kalkulatoriske_avskrvning_sum=kalkulatoriske_avskrvning_sum, 
                           kalkulatoriske_renter_sum=kalkulatoriske_renter_sum, 
                           sum_kostnader_taxi1=sum_kostnader_taxi1, sum_kostnader_taxi2=sum_kostnader_taxi2, sum_kostnader_taxi3=sum_kostnader_taxi3,
                           sum_kostnader_taxi_sum=sum_kostnader_taxi_sum,
                           driftsresultat_taxi1=driftsresultat_taxi1, driftsresultat_taxi2=driftsresultat_taxi2, 
                           driftsresultat_taxi3=driftsresultat_taxi3, driftsresultat_taxi_sum=driftsresultat_taxi_sum, 
                           resultat_internregnskap=resultat_internregnskap,
                           legend='Variabler', anchor="table1")

    return render_template('boa205_course/chapters/ch1.html', title='BØA205 Økonomistyring, kapittel 1',
                           form_boa205_ch1_q1=form_boa205_ch1_q1, form_boa205_ch1_q2=form_boa205_ch1_q2, 
                           form_boa205_ch1_q3=form_boa205_ch1_q3, form_boa205_ch1_q4=form_boa205_ch1_q4,
                           form_boa205_ch1_q5=form_boa205_ch1_q5, form_boa205_ch1_q6=form_boa205_ch1_q6,
                           form_boa205_ch1_t1=form_boa205_ch1_t1, legend='Variabler')

#Chapter 2a
@boa205_course_chapters.route('/boa205_course/kapitel2a', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch2():
    form_boa205_ch2_q1 = ModulsForm_boa205_ch2_q1()
    form_boa205_ch2_q2 = ModulsForm_boa205_ch2_q2()
    form_boa205_ch2_q3 = ModulsForm_boa205_ch2_q3()
    form_boa205_ch2_q4 = ModulsForm_boa205_ch2_q4()
    form_boa205_ch2_q5 = ModulsForm_boa205_ch2_q5()
    form_boa205_ch2_q6 = ModulsForm_boa205_ch2_q6()
    form_boa205_ch2_q7 = ModulsForm_boa205_ch2_q7()
    form_boa205_ch2_q8 = ModulsForm_boa205_ch2_q8()
    form_boa205_ch2_q9 = ModulsForm_boa205_ch2_q9()
    form_boa205_ch2_q10 = ModulsForm_boa205_ch2_q10()
    form_boa205_ch2_t1=TableForm_boa205_ch2_t1()
    form_boa205_ch2_t2=TableForm_boa205_ch2_t2()
    
    if form_boa205_ch2_q1.validate_on_submit():
        number_answers_by_author_q1=ModulsGD.query.filter_by(author=current_user). \
            filter(ModulsGD.title_mo == 'boa205_ch2'). \
            filter(ModulsGD.title_ch == 'Kapitel 2. Hva er normalkostregnskap?'). \
            filter(ModulsGD.question_num == 1).count()
        moduls = ModulsGD(question_str=form_boa205_ch2_q1.type.data, author=current_user)
        if moduls.question_str == 'generelle kostnader i husleie':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2,
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q1_q2")
    
    if form_boa205_ch2_q2.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q2.type.data, author=current_user)
        if moduls.question_str == 'trevirke for møbler, stål for sykler, eller gummi for dekk':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q1_q2")
    
    if form_boa205_ch2_q3.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q3.type.data, author=current_user)
        if moduls.question_str == '875 kr per time':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q3_q4")
    
    if form_boa205_ch2_q4.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q4.type.data, author=current_user)
        if moduls.question_str == 'selvkostmetoden tar hensyn til alle direkte og indirekte kostnader':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q3_q4")
    
    if form_boa205_ch2_q5.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q5.type.data, author=current_user)
        if moduls.question_str == '-37000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q5_q6")
    
    if form_boa205_ch2_q6.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q6.type.data, author=current_user)
        if moduls.question_str == '-10000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q5_q6")
    
    if form_boa205_ch2_q7.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q7.type.data, author=current_user)
        if moduls.question_str == '-5000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 7
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q7_q8")
    
    if form_boa205_ch2_q8.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q8.type.data, author=current_user)
        if moduls.question_str == '-6000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 8
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q7_q8")
    
    if form_boa205_ch2_q9.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q9.type.data, author=current_user)
        if moduls.question_str == '73700000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 9
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q9_q10")
    
    if form_boa205_ch2_q10.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2_q10.type.data, author=current_user)
        if moduls.question_str == '74800000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2'
        moduls.title_ch = 'Kapitel 2. Hva er normalkostregnskap?'
        moduls.question_num = 10
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="ch2_q9_q10")

    if form_boa205_ch2_t1.validate_on_submit():
        """ Constants """
        salgsinntekt_normal= 900000
        direkte_lonn_normal=110000

        salgsinntekt_virkelig= 900000
        direkte_material_virkelig=300000
        direkte_lonn_virkelig=110000

        faste_tilvirknings_budsjett=25000
        faste_administrasjon_budsjett=38000

        indirekte_materialkostnader_variable_normalsatser=0.1
        indirekte_materialkostnader_totale_normalsatser=0.18
        indirekte_tilvirkningskostnader_variable_normalsatser=0.4
        indirekte_tilvirkningskostnader_totale_normalsatser=0.6
        indirekte_administrasjon_faste_normalsatser=0.05
        indirekte_administrasjon_variable_normalsatser=0.05
        indirekte_administrasjon_totale_normalsatser=0.1

        indirekte_materialkostnader_variable_virkelig=40000
        indirekte_materialkostnader_faste_virkelig=30000
        indirekte_tilvirkningskostnader_variable_virkelig=55000
        indirekte_tilvirkningskostnader_faste_virkelig=20000
        indirekte_administrasjon_variable_virkelig=35000
        indirekte_administrasjon_faste_virkelig=30000

        """ Variables """
        direkte_material_normal = form_boa205_ch2_t1.direkte_material_normal.data
        faste_material_budsjett = form_boa205_ch2_t1.faste_material_budsjett.data
        indirekte_materialkostnader_faste_normalsatser = form_boa205_ch2_t1.indirekte_materialkostnader_faste_normalsatser.data
        indirekte_tilvirkningskostnader_faste_normalsatser = form_boa205_ch2_t1.indirekte_tilvirkningskostnader_faste_normalsatser.data

        """ Normal """
        IVMn, IFMn,IVTn,IFTn,Tn,IVAn,IFAn,selvkost_n, produktresultat_n= normal(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, indirekte_materialkostnader_variable_normalsatser,
                indirekte_materialkostnader_faste_normalsatser ,indirekte_tilvirkningskostnader_variable_normalsatser, 
                indirekte_tilvirkningskostnader_faste_normalsatser, indirekte_administrasjon_variable_normalsatser, 
                indirekte_administrasjon_faste_normalsatser)
        
        """ Virkelig """
        Tv,selvkost_v, produksjonresultat_v= virkelig(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal)
        
        """ Dekningsdiff """
        IVMD,IFMD,IVTD,IFTD,IVAD,IFAD,dekningsdifferanser,produktresultat_n= dekningsdiff(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, indirekte_materialkostnader_variable_normalsatser,
                indirekte_materialkostnader_faste_normalsatser ,indirekte_tilvirkningskostnader_variable_normalsatser, 
                indirekte_tilvirkningskostnader_faste_normalsatser, indirekte_administrasjon_variable_normalsatser, 
                indirekte_administrasjon_faste_normalsatser)
        
        """ Produksjonresultat_normal """
        produksjonresultat_n =produksjonresultat_normal(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, indirekte_materialkostnader_variable_normalsatser,
                indirekte_materialkostnader_faste_normalsatser ,indirekte_tilvirkningskostnader_variable_normalsatser, 
                indirekte_tilvirkningskostnader_faste_normalsatser, indirekte_administrasjon_variable_normalsatser, 
                indirekte_administrasjon_faste_normalsatser)
        
        """ Avvik """
        IVMn,forbruk_avvik_m_v,volumn_avvik_m_f,forbruk_avvik_m_f,total_avvik_m_f=avvik(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, indirekte_materialkostnader_variable_normalsatser,
                indirekte_materialkostnader_faste_normalsatser ,indirekte_tilvirkningskostnader_variable_normalsatser, 
                indirekte_tilvirkningskostnader_faste_normalsatser, indirekte_administrasjon_variable_normalsatser, 
                indirekte_administrasjon_faste_normalsatser, faste_material_budsjett)
        
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10, 
                form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="table1",
                salgsinntekt_normal=salgsinntekt_normal, direkte_lonn_normal= direkte_lonn_normal,
                direkte_material_normal=direkte_material_normal, 
                indirekte_materialkostnader_variable_normalsatser=indirekte_materialkostnader_variable_normalsatser,
                indirekte_materialkostnader_faste_normalsatser=indirekte_materialkostnader_faste_normalsatser,
                indirekte_tilvirkningskostnader_variable_normalsatser=indirekte_tilvirkningskostnader_variable_normalsatser, 
                indirekte_tilvirkningskostnader_faste_normalsatser=indirekte_tilvirkningskostnader_faste_normalsatser, 
                indirekte_administrasjon_variable_normalsatser=indirekte_administrasjon_variable_normalsatser, 
                indirekte_administrasjon_faste_normalsatser=indirekte_administrasjon_faste_normalsatser, 
                IVMn=IVMn, IFMn=IFMn, IVTn=IVTn,IFTn=IFTn,Tn=Tn,IVAn=IVAn,IFAn=IFAn,selvkost_n=selvkost_n, 
                produktresultat_n=produktresultat_n,
                faste_material_budsjett=faste_material_budsjett,
                Tv=Tv,selvkost_v=selvkost_v, produksjonresultat_v=produksjonresultat_v,
                IVMD=IVMD,IFMD=IFMD,IVTD=IVTD,IFTD=IFTD,IVAD=IVAD,IFAD=IFAD,dekningsdifferanser=dekningsdifferanser,
                produksjonresultat_n=produksjonresultat_n,
                forbruk_avvik_m_v=forbruk_avvik_m_v,volumn_avvik_m_f=volumn_avvik_m_f,
                forbruk_avvik_m_f=forbruk_avvik_m_f,total_avvik_m_f=total_avvik_m_f)
    
    if form_boa205_ch2_t2.validate_on_submit():
        """ Constants """
        salgsinntekt_normal= 81000000
        direkte_material_normal=17000000
        direkte_lonn_normal=27000000
        indirekte_materialkostnader_variable=1000000
        indirekte_materialkostnader_faste=2500000
        indirekte_tilvirkningskostnader_variable=8000000
        indirekte_tilvirkningskostnader_faste=11500000
        indirekte_administrasjon_faste=6850000

        indirekte_materialkostnader_faste_normalsatser=0.15
        indirekte_materialkostnader_variable_normalsatser=0.05
        indirekte_materialkostnader_totale_normalsatser=0.2
        indirekte_tilvirkningskostnader_faste_normalsatser=0.45
        indirekte_tilvirkningskostnader_variable_normalsatser=0.3
        indirekte_tilvirkningskostnader_totale_normalsatser=0.75
        indirekte_administrasjon_faste_normalsatser=0.1
        indirekte_administrasjon_variable_normalsatser=0
        indirekte_administrasjon_totale_normalsatser=0.1

        """ Variables """
        lagerreduksjon_selv = form_boa205_ch2_t2.lagerreduksjon_selv.data
        ferdigvaren_selv = form_boa205_ch2_t2.ferdigvaren_selv.data
        lagerreduksjon_bidra = form_boa205_ch2_t2.lagerreduksjon_bidra.data
        ferdigvaren_bidra = form_boa205_ch2_t2.ferdigvaren_bidra.data

        """ Produktresultat selv """
        ITMs,ITTs,Ts, T_ferdiger_s, T_salgte_s, ITAs,selvkost_s, produktresultat_s= produktresultat_selv(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, indirekte_materialkostnader_totale_normalsatser,
                indirekte_tilvirkningskostnader_totale_normalsatser, indirekte_administrasjon_totale_normalsatser, 
                lagerreduksjon_selv, ferdigvaren_selv)
        
        """ virkelig_selv """
        Tv,T_ferdiger_v,T_salgte_v,selvkost_v, produksjonresultat_v=virkelig_selv(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, lagerreduksjon_selv, ferdigvaren_selv)
        
        """ dekningsdiff_produksjonresultat_selv """
        DM_s,DT_s,DA_s,D_s,produksjonresultat_s=dekningsdiff_produksjonresultat_selv(salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, indirekte_materialkostnader_totale_normalsatser,
                indirekte_tilvirkningskostnader_totale_normalsatser, indirekte_administrasjon_totale_normalsatser, 
                lagerreduksjon_selv, ferdigvaren_selv)
        
        (IVMb, IVTb,Tb,T_ferdiger_b, T_salgte_b,IVAb,salgmerkost_b,kalkulert_dekningsbidra_b, 
         DVM_b,DVT_b,DVA_b,sumDV_b,virkelig_dekningsbidrag_b,IFM_b,IFT_b,IFA_b,DFM_b,DFT_b,DFA_b,
         sumDF_b,produktresultat_b,T_v_b,T_ferdiger_v_b,T_salgte_v_b,virkelig_dekningsbidrag_v_b,produktresultat_v_b) = produktresultat_bidra(
             salgsinntekt_normal,
                direkte_material_normal,direkte_lonn_normal, indirekte_materialkostnader_variable_normalsatser,
                indirekte_materialkostnader_faste_normalsatser,
                indirekte_tilvirkningskostnader_variable_normalsatser, indirekte_tilvirkningskostnader_faste_normalsatser, 
                indirekte_administrasjon_variable_normalsatser, indirekte_administrasjon_faste_normalsatser, 
                lagerreduksjon_bidra, ferdigvaren_bidra)
        
        return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4, 
                form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler', anchor="table2",
                salgsinntekt_normal=salgsinntekt_normal, direkte_lonn_normal= direkte_lonn_normal,
                direkte_material_normal=direkte_material_normal,
                indirekte_materialkostnader_totale_normalsatser=indirekte_materialkostnader_totale_normalsatser,
                indirekte_materialkostnader_variable_normalsatser=indirekte_materialkostnader_variable_normalsatser,
                indirekte_materialkostnader_faste_normalsatser=indirekte_materialkostnader_faste_normalsatser,
                indirekte_tilvirkningskostnader_totale_normalsatser=indirekte_tilvirkningskostnader_totale_normalsatser, 
                indirekte_tilvirkningskostnader_variable_normalsatser=indirekte_tilvirkningskostnader_variable_normalsatser, 
                indirekte_tilvirkningskostnader_faste_normalsatser=indirekte_tilvirkningskostnader_faste_normalsatser, 
                indirekte_administrasjon_totale_normalsatser=indirekte_administrasjon_totale_normalsatser, 
                indirekte_administrasjon_variable_normalsatser=indirekte_administrasjon_variable_normalsatser, 
                indirekte_administrasjon_faste_normalsatser=indirekte_administrasjon_faste_normalsatser, 
                lagerreduksjon_selv=lagerreduksjon_selv, ferdigvaren_selv=ferdigvaren_selv,
                lagerreduksjon_bidra =lagerreduksjon_bidra, ferdigvaren_bidra=ferdigvaren_bidra,
                ITMs=ITMs,ITTs=ITTs,Ts=Ts, T_ferdiger_s=T_ferdiger_s, T_salgte_s=T_salgte_s, ITAs=ITAs,
                selvkost_s=selvkost_s, produktresultat_s=produktresultat_s,
                Tv=Tv,T_ferdiger_v=T_ferdiger_v,T_salgte_v=T_salgte_v,selvkost_v=selvkost_v, produksjonresultat_v=produksjonresultat_v,
                DM_s=DM_s,DT_s=DT_s,DA_s=DA_s,D_s=D_s,produksjonresultat_s=produksjonresultat_s,
                IVMb=IVMb, IVTb=IVTb,Tb=Tb,T_ferdiger_b=T_ferdiger_b, T_salgte_b=T_salgte_b,
                IVAb=IVAb,salgmerkost_b=salgmerkost_b,kalkulert_dekningsbidra_b=kalkulert_dekningsbidra_b, 
                DVM_b=DVM_b,DVT_b=DVT_b,DVA_b=DVA_b,sumDV_b=sumDV_b,virkelig_dekningsbidrag_b=virkelig_dekningsbidrag_b,
                IFM_b=IFM_b,IFT_b=IFT_b,IFA_b=IFA_b,DFM_b=DFM_b,DFT_b=DFT_b,DFA_b=DFA_b,
                sumDF_b=sumDF_b,produktresultat_b=produktresultat_b,T_v_b=T_v_b,T_ferdiger_v_b=T_ferdiger_v_b,
                T_salgte_v_b=T_salgte_v_b,virkelig_dekningsbidrag_v_b=virkelig_dekningsbidrag_v_b,produktresultat_v_b=produktresultat_v_b)
    
    return render_template('boa205_course/chapters/ch2.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2_q1=form_boa205_ch2_q1, form_boa205_ch2_q2=form_boa205_ch2_q2, 
                           form_boa205_ch2_q3=form_boa205_ch2_q3, form_boa205_ch2_q4=form_boa205_ch2_q4,
                           form_boa205_ch2_q5=form_boa205_ch2_q5, form_boa205_ch2_q6=form_boa205_ch2_q6,
                           form_boa205_ch2_q7=form_boa205_ch2_q7, form_boa205_ch2_q8=form_boa205_ch2_q8,
                           form_boa205_ch2_q9=form_boa205_ch2_q9, form_boa205_ch2_q10=form_boa205_ch2_q10,
                           form_boa205_ch2_t1=form_boa205_ch2_t1, form_boa205_ch2_t2=form_boa205_ch2_t2, legend='Variabler')

#Chapter 2b
@boa205_course_chapters.route('/boa205_course/kapitel2b', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch2b():
    form_boa205_ch2b_q1 = ModulsForm_boa205_ch2b_q1()
    form_boa205_ch2b_q2 = ModulsForm_boa205_ch2b_q2()
    form_boa205_ch2b_q3 = ModulsForm_boa205_ch2b_q3()
    form_boa205_ch2b_q4 = ModulsForm_boa205_ch2b_q4()
    form_boa205_ch2b_q5 = ModulsForm_boa205_ch2b_q5()
    form_boa205_ch2b_q6 = ModulsForm_boa205_ch2b_q6()
    form_boa205_ch2b_t1=TableForm_boa205_ch2b_t1()
    form_boa205_ch2b_t2=TableForm_boa205_ch2b_t2()

    if form_boa205_ch2b_q1.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2b_q1.type.data, author=current_user)
        if moduls.question_str == 'januar':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2b'
        moduls.title_ch = 'Kapitel 2b. Hva er normalkostregnskap?'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2b'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
                           form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
                           form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
                           form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, 
                           legend='Variabler', anchor="ch2b_q1_q2")
    
    if form_boa205_ch2b_q2.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2b_q2.type.data, author=current_user)
        if moduls.question_str == 'bare januar':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2b'
        moduls.title_ch = 'Kapitel 2b. Hva er normalkostregnskap?'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2b'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
                           form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
                           form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
                           form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, 
                           legend='Variabler', anchor="ch2b_q1_q2")
    
    if form_boa205_ch2b_q3.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2b_q3.type.data, author=current_user)
        if moduls.question_str == 'februar':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2b'
        moduls.title_ch = 'Kapitel 2b. Hva er normalkostregnskap?'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2b'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
                           form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
                           form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
                           form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, 
                           legend='Variabler', anchor="ch2b_q1_q2")
    
    if form_boa205_ch2b_q4.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2b_q4.type.data, author=current_user)
        if moduls.question_str == '-17629':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2b'
        moduls.title_ch = 'Kapitel 2b. Hva er normalkostregnskap?'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2b'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
                           form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
                           form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
                           form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, 
                           legend='Variabler', anchor="ch2b_q1_q2")
    
    if form_boa205_ch2b_q5.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2b_q5.type.data, author=current_user)
        if moduls.question_str == '2500':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2b'
        moduls.title_ch = 'Kapitel 2b. Hva er normalkostregnskap?'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2b'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
                           form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
                           form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
                           form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, 
                           legend='Variabler', anchor="ch2b_q1_q2")
    
    if form_boa205_ch2b_q6.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch2b_q6.type.data, author=current_user)
        if moduls.question_str == '-5335':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch2b'
        moduls.title_ch = 'Kapitel 2b. Hva er normalkostregnskap?'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch2b'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2',
                           form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
                           form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
                           form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
                           form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, 
                           legend='Variabler', anchor="ch2b_q1_q2")

    if form_boa205_ch2b_t1.validate_on_submit():
        """ Variables """
        endring_varer_i_arbeid_102_selv = form_boa205_ch2b_t1.endring_varer_i_arbeid_102.data
        endring_ferdige_varer_101_selv = form_boa205_ch2b_t1.endring_ferdige_varer_101.data

        (im_102_s,im_103_s,im_104_s,im_sum_s,dm_s,il1_102_s,il1_103_s,il1_104_s,il1_sum_s,dl1_s,il2_102_s,il2_103_s,il2_104_s,il2_sum_s,
           dl2_s,kalkulert_tilv_102_s,kalkulert_tilv_103_s,kalkulert_tilv_104_s,kalkulert_tilv_sum_s,
           kalkulert_tilv_ferdig_102_s,kalkulert_tilv_ferdig_103_s,kalkulert_tilv_ferdig_104_s,kalkulert_tilv_ferdig_sum_s,
           kalkulert_tilv_ferdig_virkelige_s,endring_ferdige_varer_s,
           kalkulert_tilv_solgte_101_s,kalkulert_tilv_solgte_102_s,kalkulert_tilv_solgte_103_s,
           kalkulert_tilv_solgte_104_s,kalkulert_tilv_solgte_sum_s,kalkulert_tilv_solgte_virkelige_s,
           salgs_adm_101_s,salgs_adm_102_s,salgs_adm_103_s,salgs_adm_104_s,salgs_adm_sum_s,d_salgs_adm_s,
           kalkulert_selvkost_101_s,kalkulert_selvkost_102_s,kalkulert_selvkost_103_s,
           kalkulert_selvkost_104_s,kalkulert_selvkost_sum_s,kalkulert_selvkost_virkelige_s,
           produktresultat_101_s,produktresultat_102_s,produktresultat_103_s,produktresultat_104_s,
           produktresultat_sum_s,d_sum_s,produksjonresultat_s,produksjonresultat_virkelige_s) = ch2a_selv(endring_varer_i_arbeid_102_selv, endring_ferdige_varer_101_selv)

        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2', 
            form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
            form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
            form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
            form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2,legend='Variabler',anchor="table1",
            endring_varer_i_arbeid_102_selv=endring_varer_i_arbeid_102_selv, endring_ferdige_varer_101_selv=endring_ferdige_varer_101_selv,
            im_102_s=im_102_s,im_103_s=im_103_s,im_104_s=im_104_s,im_sum_s=im_sum_s,dm_s=dm_s,il1_102_s=il1_102_s,
            il1_103_s=il1_103_s,il1_104_s=il1_104_s,il1_sum_s=il1_sum_s,dl1_s=dl1_s,il2_102_s=il2_102_s,il2_103_s=il2_103_s,
            il2_104_s=il2_104_s,il2_sum_s=il2_sum_s,dl2_s=dl2_s,kalkulert_tilv_102_s=kalkulert_tilv_102_s,
            kalkulert_tilv_103_s=kalkulert_tilv_103_s,kalkulert_tilv_104_s=kalkulert_tilv_104_s,kalkulert_tilv_sum_s=kalkulert_tilv_sum_s,
            kalkulert_tilv_ferdig_102_s=kalkulert_tilv_ferdig_102_s,kalkulert_tilv_ferdig_103_s=kalkulert_tilv_ferdig_103_s,
            kalkulert_tilv_ferdig_104_s=kalkulert_tilv_ferdig_104_s,kalkulert_tilv_ferdig_sum_s=kalkulert_tilv_ferdig_sum_s,
            kalkulert_tilv_ferdig_virkelige_s=kalkulert_tilv_ferdig_virkelige_s,endring_ferdige_varer_s=endring_ferdige_varer_s,
            kalkulert_tilv_solgte_101_s=kalkulert_tilv_solgte_101_s,kalkulert_tilv_solgte_102_s=kalkulert_tilv_solgte_102_s,
            kalkulert_tilv_solgte_103_s=kalkulert_tilv_solgte_103_s,kalkulert_tilv_solgte_104_s=kalkulert_tilv_solgte_104_s,
            kalkulert_tilv_solgte_sum_s=kalkulert_tilv_solgte_sum_s,kalkulert_tilv_solgte_virkelige_s=kalkulert_tilv_solgte_virkelige_s,
            salgs_adm_101_s=salgs_adm_101_s,salgs_adm_102_s=salgs_adm_102_s,salgs_adm_103_s=salgs_adm_103_s,
            salgs_adm_104_s=salgs_adm_104_s,salgs_adm_sum_s=salgs_adm_sum_s,d_salgs_adm_s=d_salgs_adm_s,
            kalkulert_selvkost_101_s=kalkulert_selvkost_101_s,kalkulert_selvkost_102_s=kalkulert_selvkost_102_s,
            kalkulert_selvkost_103_s=kalkulert_selvkost_103_s,kalkulert_selvkost_104_s=kalkulert_selvkost_104_s,
            kalkulert_selvkost_sum_s=kalkulert_selvkost_sum_s,kalkulert_selvkost_virkelige_s=kalkulert_selvkost_virkelige_s,
            produktresultat_101_s=produktresultat_101_s,produktresultat_102_s=produktresultat_102_s,
            produktresultat_103_s=produktresultat_103_s,produktresultat_104_s=produktresultat_104_s,
            produktresultat_sum_s=produktresultat_sum_s,d_sum_s=d_sum_s,produksjonresultat_s=produksjonresultat_s,
            produksjonresultat_virkelige_s=produksjonresultat_virkelige_s)
    
    if form_boa205_ch2b_t2.validate_on_submit():
        """ Variables """
        endring_varer_i_arbeid_102_bidra = form_boa205_ch2b_t2.endring_varer_i_arbeid_102.data
        endring_ferdige_varer_101_bidra = form_boa205_ch2b_t2.endring_ferdige_varer_101.data

        (im_102_b,im_103_b,im_104_b,im_sum_b,dm_b,il1_102_b,il1_103_b,il1_104_b,il1_sum_b,dl1_b,il2_102_b,il2_103_b,il2_104_b,il2_sum_b,
           dl2_b,kalkulert_tilv_102_b,kalkulert_tilv_103_b,kalkulert_tilv_104_b,kalkulert_tilv_sum_b,
           kalkulert_tilv_ferdig_102_b,kalkulert_tilv_ferdig_103_b,kalkulert_tilv_ferdig_104_b,kalkulert_tilv_ferdig_sum_b,
           kalkulert_tilv_ferdig_virkelige_b,endring_ferdige_varer_b,
           kalkulert_tilv_solgte_101_b,kalkulert_tilv_solgte_102_b,kalkulert_tilv_solgte_103_b,
           kalkulert_tilv_solgte_104_b,kalkulert_tilv_solgte_sum_b,kalkulert_tilv_solgte_virkelige_b,
           merkost_solgte_varer_101_b,merkost_solgte_varer_102_b,merkost_solgte_varer_103_b,merkost_solgte_varer_104_b,
           merkost_solgte_varer_sum_b,merkost_solgte_varer_virkelige_b,
           kalkulert_dekningsbidrag_101_b,
           kalkulert_dekningsbidrag_102_b,kalkulert_dekningsbidrag_103_b,kalkulert_dekningsbidrag_104_b,
           kalkulert_dekningsbidrag_sum_b,d_total_b,
           virkelig_dekningsbidrag_b,virkelig_dekningsbidrag_virkelige_b,
           produksjonresultat_virkelige_b)=ch2a_bidra(endring_varer_i_arbeid_102_bidra, endring_ferdige_varer_101_bidra)

        
        return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2', 
            form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
            form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
            form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
            form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, legend='Variabler',anchor="table2",
            endring_varer_i_arbeid_102_bidra=endring_varer_i_arbeid_102_bidra, endring_ferdige_varer_101_bidra=endring_ferdige_varer_101_bidra,
            im_102_b=im_102_b,im_103_b=im_103_b,im_104_b=im_104_b,im_sum_b=im_sum_b,dm_b=dm_b,il1_102_b=il1_102_b,
            il1_103_b=il1_103_b,il1_104_b=il1_104_b,il1_sum_b=il1_sum_b,dl1_b=dl1_b,il2_102_b=il2_102_b,
            il2_103_b=il2_103_b,il2_104_b=il2_104_b,il2_sum_b=il2_sum_b,
            dl2_b=dl2_b,kalkulert_tilv_102_b=kalkulert_tilv_102_b,kalkulert_tilv_103_b=kalkulert_tilv_103_b,kalkulert_tilv_104_b=kalkulert_tilv_104_b,
            kalkulert_tilv_sum_b=kalkulert_tilv_sum_b,
            kalkulert_tilv_ferdig_102_b=kalkulert_tilv_ferdig_102_b,kalkulert_tilv_ferdig_103_b=kalkulert_tilv_ferdig_103_b,
            kalkulert_tilv_ferdig_104_b=kalkulert_tilv_ferdig_104_b,kalkulert_tilv_ferdig_sum_b=kalkulert_tilv_ferdig_sum_b,
            kalkulert_tilv_ferdig_virkelige_b=kalkulert_tilv_ferdig_virkelige_b,endring_ferdige_varer_b=endring_ferdige_varer_b,
            kalkulert_tilv_solgte_101_b=kalkulert_tilv_solgte_101_b,kalkulert_tilv_solgte_102_b=kalkulert_tilv_solgte_102_b,
            kalkulert_tilv_solgte_103_b=kalkulert_tilv_solgte_103_b,
            kalkulert_tilv_solgte_104_b=kalkulert_tilv_solgte_104_b,kalkulert_tilv_solgte_sum_b=kalkulert_tilv_solgte_sum_b,
            kalkulert_tilv_solgte_virkelige_b=kalkulert_tilv_solgte_virkelige_b, merkost_solgte_varer_101_b=merkost_solgte_varer_101_b,
            merkost_solgte_varer_102_b=merkost_solgte_varer_102_b,merkost_solgte_varer_103_b=merkost_solgte_varer_103_b,
            merkost_solgte_varer_104_b=merkost_solgte_varer_104_b,merkost_solgte_varer_sum_b=merkost_solgte_varer_sum_b,
            merkost_solgte_varer_virkelige_b=merkost_solgte_varer_virkelige_b,kalkulert_dekningsbidrag_101_b=kalkulert_dekningsbidrag_101_b,
            kalkulert_dekningsbidrag_102_b=kalkulert_dekningsbidrag_102_b,kalkulert_dekningsbidrag_103_b=kalkulert_dekningsbidrag_103_b,
            kalkulert_dekningsbidrag_104_b=kalkulert_dekningsbidrag_104_b,kalkulert_dekningsbidrag_sum_b=kalkulert_dekningsbidrag_sum_b,
            d_total_b=d_total_b,virkelig_dekningsbidrag_b=virkelig_dekningsbidrag_b,
            virkelig_dekningsbidrag_virkelige_b=virkelig_dekningsbidrag_virkelige_b,produksjonresultat_virkelige_b=produksjonresultat_virkelige_b)


    return render_template('boa205_course/chapters/ch2b.html', title='BØA205 Økonomistyring, kapittel 2',
            form_boa205_ch2b_q1=form_boa205_ch2b_q1, form_boa205_ch2b_q2=form_boa205_ch2b_q2,
            form_boa205_ch2b_q3=form_boa205_ch2b_q3, form_boa205_ch2b_q4=form_boa205_ch2b_q4,
            form_boa205_ch2b_q5=form_boa205_ch2b_q5, form_boa205_ch2b_q6=form_boa205_ch2b_q6,
            form_boa205_ch2b_t1=form_boa205_ch2b_t1, form_boa205_ch2b_t2=form_boa205_ch2b_t2, legend='Variabler')

#Chapter 3
@boa205_course_chapters.route('/boa205_course/kapitel3', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch3():
    form_boa205_ch3_t1=TableForm_boa205_ch3_t1()
    form_boa205_ch3_t2=TableForm_boa205_ch3_t2()
    form_boa205_ch3_t3=TableForm_boa205_ch3_t3()
    form_boa205_ch3_t4=TableForm_boa205_ch3_t4()
    form_boa205_ch3_q1 = ModulsForm_boa205_ch3_q1()
    form_boa205_ch3_q2 = ModulsForm_boa205_ch3_q2()
    form_boa205_ch3_q3 = ModulsForm_boa205_ch3_q3()
    form_boa205_ch3_q4 = ModulsForm_boa205_ch3_q4()
    form_boa205_ch3_q5 = ModulsForm_boa205_ch3_q5()
    form_boa205_ch3_q6 = ModulsForm_boa205_ch3_q6()
    form_boa205_ch3_q7 = ModulsForm_boa205_ch3_q7()
    form_boa205_ch3_q8 = ModulsForm_boa205_ch3_q8()
    form_boa205_ch3_q9 = ModulsForm_boa205_ch3_q9()
    form_boa205_ch3_q10 = ModulsForm_boa205_ch3_q10()

    if form_boa205_ch3_t1.validate_on_submit():
        """ Variables """
        pris_beholdning_1_januar = form_boa205_ch3_t1.pris_beholdning_1_januar.data
        pris_innkjop_material_i_januar = form_boa205_ch3_t1.pris_innkjop_material_i_januar.data

        (beholdning_material_01_januar_kost,innkjøp_material_i_januar_kost,
         beholdning_material_31_januar_kost,virkelig_forbruk_pris,virkelig_forbruk_kost,
         standard_kostnader,virkelig_forbruk,virkelig_kostnader,
         mengdeavvik,prisavvik,totalavvik)=ch3_materialregnskap(pris_beholdning_1_januar,pris_innkjop_material_i_januar)

        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',anchor="table1",
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,form_boa205_ch3_t3=form_boa205_ch3_t3,
        form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', 
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2, 
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10,
        pris_beholdning_1_januar=pris_beholdning_1_januar,
        pris_innkjop_material_i_januar=pris_innkjop_material_i_januar,
        beholdning_material_01_januar_kost=beholdning_material_01_januar_kost,innkjøp_material_i_januar_kost=innkjøp_material_i_januar_kost,
        beholdning_material_31_januar_kost=beholdning_material_31_januar_kost,virkelig_forbruk_pris=virkelig_forbruk_pris,
        virkelig_forbruk_kost=virkelig_forbruk_kost,standard_kostnader=standard_kostnader,virkelig_forbruk=virkelig_forbruk,
        virkelig_kostnader=virkelig_kostnader,mengdeavvik=mengdeavvik,prisavvik=prisavvik,totalavvik=totalavvik)
    
    if form_boa205_ch3_t2.validate_on_submit():
        """ Variables """
        standard_lonn = form_boa205_ch3_t2.standard_lonn.data
        virkelig_timer = form_boa205_ch3_t2.virkelig_timer.data

        (virkelig_lonn,standard_kostnader,virkelig_forbruk,virkelige_kostnader,
         tidsavvik,lønnssatsavvik,totalavvik,lønnssatsavvik_komentar)=ch3_lonnregnskap(standard_lonn,virkelig_timer)

        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',anchor="table2",
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler',
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10,
        standard_lonn=standard_lonn, virkelig_timer=virkelig_timer,virkelig_lonn=virkelig_lonn,
        standard_kostnader=standard_kostnader,virkelig_forbruk=virkelig_forbruk,virkelige_kostnader=virkelige_kostnader,
        tidsavvik=tidsavvik,lønnssatsavvik=lønnssatsavvik,totalavvik=totalavvik,lønnssatsavvik_komentar=lønnssatsavvik_komentar)
    
    if form_boa205_ch3_t3.validate_on_submit():
        """ Variables """
        sat_faste_indirekte_tilv = form_boa205_ch3_t3.sat_faste_indirekte_tilv.data
        sat_variable_indirekte_tilv = form_boa205_ch3_t3.sat_variable_indirekte_tilv.data
        sat_faste_administrasjon = form_boa205_ch3_t3.sat_faste_administrasjon.data

        (kost_faste_indirekte_tilv,kost_variable_indirekte_tilv,tilv_per_enhet,sat_faste_administrasjon,
           selvkost_enhet,tilv_per_enhet_bidra)=ch3_standard_selv_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon)
        
        (indirekte_tilv_sat_s,indirekte_tilv_kost_s,indirekte_tilv_avvik_s,
         periodens_tilvirkningskostnad_s,endring_ferdige_varer_s,tilv_solgte_s,
         tilv_solgte_virkelig_s,admin_s,admin_avvik_s,selvkost_solgte_s,
           selvkost_solgte_bidra_s,produktresultat_s,avvik_total_s,
           produksjonsresultat_s,produksjonsresultat_bidra_s)=ch3_selvksot_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon)

        (indirekte_tilv_kost_b,indirekte_tilv_avvik_b,periodens_tilvirkningskostnad_b,
           endring_ferdige_varer_b,tilv_solgte_b,tilv_solgte_virkelig_b,
           kalkulert_DB_b,virkelig_dekningsbidrag_b,virkelig_dekningsbidrag_virkelige_b,
           faste_admin_b,avvik_faste_admin_b,avvik_faste_sum_b,
           produksjonsresultat_b,produksjonsresultat_virkelige_b)=ch3_bidrakost_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon)

        (differanse1,differanse2)=ch3_differanse_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon)

        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',anchor="table3",
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler',
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10,
        sat_faste_indirekte_tilv=sat_faste_indirekte_tilv,
        sat_variable_indirekte_tilv=sat_variable_indirekte_tilv,sat_faste_administrasjon=sat_faste_administrasjon,
        kost_faste_indirekte_tilv=kost_faste_indirekte_tilv,kost_variable_indirekte_tilv=kost_variable_indirekte_tilv,
        tilv_per_enhet=tilv_per_enhet,selvkost_enhet=selvkost_enhet,tilv_per_enhet_bidra=tilv_per_enhet_bidra,
        indirekte_tilv_sat_s=indirekte_tilv_sat_s,indirekte_tilv_kost_s=indirekte_tilv_kost_s,indirekte_tilv_avvik_s=indirekte_tilv_avvik_s,
        periodens_tilvirkningskostnad_s=periodens_tilvirkningskostnad_s,endring_ferdige_varer_s=endring_ferdige_varer_s,
        tilv_solgte_s=tilv_solgte_s,tilv_solgte_virkelig_s=tilv_solgte_virkelig_s,admin_s=admin_s,admin_avvik_s=admin_avvik_s,
        selvkost_solgte_s=selvkost_solgte_s,selvkost_solgte_bidra_s=selvkost_solgte_bidra_s,produktresultat_s=produktresultat_s,
        avvik_total_s=avvik_total_s,produksjonsresultat_s=produksjonsresultat_s,produksjonsresultat_bidra_s=produksjonsresultat_bidra_s,
        indirekte_tilv_kost_b=indirekte_tilv_kost_b,indirekte_tilv_avvik_b=indirekte_tilv_avvik_b,
        periodens_tilvirkningskostnad_b=periodens_tilvirkningskostnad_b,endring_ferdige_varer_b=endring_ferdige_varer_b,
        tilv_solgte_b=tilv_solgte_b,tilv_solgte_virkelig_b=tilv_solgte_virkelig_b,kalkulert_DB_b=kalkulert_DB_b,
        virkelig_dekningsbidrag_b=virkelig_dekningsbidrag_b,virkelig_dekningsbidrag_virkelige_b=virkelig_dekningsbidrag_virkelige_b,
        faste_admin_b=faste_admin_b,avvik_faste_admin_b=avvik_faste_admin_b,avvik_faste_sum_b=avvik_faste_sum_b,
        produksjonsresultat_b=produksjonsresultat_b,produksjonsresultat_virkelige_b=produksjonsresultat_virkelige_b,
        differanse1=differanse1,differanse2=differanse2)
    
    if form_boa205_ch3_t4.validate_on_submit():
        """ Variables """
        sat_faste_indirekte_tilv_t4 = form_boa205_ch3_t4.sat_faste_indirekte_tilv_t4.data
        sat_variable_indirekte_tilv_t4 = form_boa205_ch3_t4.sat_variable_indirekte_tilv_t4.data
        sat_faste_administrasjon_t4 = form_boa205_ch3_t4.sat_faste_administrasjon_t4.data

        (standard_kostnad_var,effektivitets_avvik,forbruksavvik_var,totalt_avvik_var,
         standard_kostnad_faste,volumavvik_faste,forbruksavvik_faste,totalt_avvik_faste,
         standard_kostnad_admin,volumavvik_admin,forbruksavvik_admin,totalt_avvik_admin)=ch3_virkelige_t4(sat_faste_indirekte_tilv_t4,sat_variable_indirekte_tilv_t4,sat_faste_administrasjon_t4)

        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',anchor="table4",
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler',
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10,
        sat_variable_indirekte_tilv_t4=sat_variable_indirekte_tilv_t4,sat_faste_indirekte_tilv_t4=sat_faste_indirekte_tilv_t4,
        sat_faste_administrasjon_t4=sat_faste_administrasjon_t4,
        standard_kostnad_var=standard_kostnad_var,effektivitets_avvik=effektivitets_avvik,
        forbruksavvik_var=forbruksavvik_var,totalt_avvik_var=totalt_avvik_var,
        standard_kostnad_faste=standard_kostnad_faste,volumavvik_faste=volumavvik_faste,
        forbruksavvik_faste=forbruksavvik_faste,totalt_avvik_faste=totalt_avvik_faste,
        standard_kostnad_admin=standard_kostnad_admin,volumavvik_admin=volumavvik_admin,
        forbruksavvik_admin=forbruksavvik_admin,totalt_avvik_admin=totalt_avvik_admin)
    
    if form_boa205_ch3_q1.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q1.type.data, author=current_user)
        if moduls.question_str == '-980':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q1_q2",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q2.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q2.type.data, author=current_user)
        if moduls.question_str == '-102':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q1_q2",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q3.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q3.type.data, author=current_user)
        if moduls.question_str == '2400':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q3_q4",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q4.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q4.type.data, author=current_user)
        if moduls.question_str == '-6085':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q3_q4",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q5.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q5.type.data, author=current_user)
        if moduls.question_str == '1688':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q5_q6",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q6.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q6.type.data, author=current_user)
        if moduls.question_str == '-232':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q5_q6",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q7.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q7.type.data, author=current_user)
        if moduls.question_str == '-23120':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 7
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q7_q8",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q8.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q8.type.data, author=current_user)
        if moduls.question_str == '-21200':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 8
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q7_q8",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q9.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q9.type.data, author=current_user)
        if moduls.question_str == '-300':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 9
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q9_q10",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)
    
    if form_boa205_ch3_q10.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch3_q10.type.data, author=current_user)
        if moduls.question_str == '-1000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch3'
        moduls.title_ch = 'Kapitel 3. Standardkost'
        moduls.question_num = 10
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch3'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler', anchor="ch3_q9_q10",
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)

    return render_template('boa205_course/chapters/ch3.html', title='BØA205 Økonomistyring, kapittel 3',
        form_boa205_ch3_t1=form_boa205_ch3_t1, form_boa205_ch3_t2=form_boa205_ch3_t2,
        form_boa205_ch3_t3=form_boa205_ch3_t3,form_boa205_ch3_t4=form_boa205_ch3_t4,legend='Variabler',
        form_boa205_ch3_q1=form_boa205_ch3_q1, form_boa205_ch3_q2=form_boa205_ch3_q2,
        form_boa205_ch3_q3=form_boa205_ch3_q3, form_boa205_ch3_q4=form_boa205_ch3_q4,
        form_boa205_ch3_q5=form_boa205_ch3_q5, form_boa205_ch3_q6=form_boa205_ch3_q6,
        form_boa205_ch3_q7=form_boa205_ch3_q7, form_boa205_ch3_q8=form_boa205_ch3_q8,
        form_boa205_ch3_q9=form_boa205_ch3_q9, form_boa205_ch3_q10=form_boa205_ch3_q10)

#Chapter 3 extra exercise
@boa205_course_chapters.route('/boa205_course/kapitel3/ekstra', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch3_extra():
    return render_template('boa205_course/chapters/ch3_extra.html', title='BØA205 Økonomistyring, kapittel 3, ekstra')

#Arbeidskrav1
@boa205_course_chapters.route('/boa205_course/arbeidskrav1', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_arbeidskrav1():
    return render_template('boa205_course/chapters/arbeidskrav1.html', title='BØA205 Økonomistyring, arbeidskrav1')
