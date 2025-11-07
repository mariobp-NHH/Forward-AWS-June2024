from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch1_q1, ModulsForm_boa205_ch1_q2, ModulsForm_boa205_ch1_q3, ModulsForm_boa205_ch1_q4, ModulsForm_boa205_ch1_q5, ModulsForm_boa205_ch1_q6,TableForm_boa205_ch1_t1

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
        if moduls.question_str == 'kr 20 000':
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

