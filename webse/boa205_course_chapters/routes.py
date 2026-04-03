from flask import render_template, url_for, Blueprint, flash, redirect, request
from webse import application, db, bcrypt
from webse.models import User, ChatGD, ModulsGD
from flask_login import login_user, current_user, logout_user, login_required
from webse.forward_users.utils import read_image

boa205_course_chapters= Blueprint('boa205_course_chapters', __name__)

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
""" chapter 4 """
from webse.boa205_course_chapters.forms import TableForm_boa205_ch4_t1,TableForm_boa205_ch4_t2,TableForm_boa205_ch4_t3
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch4_q1,ModulsForm_boa205_ch4_q2,ModulsForm_boa205_ch4_q3,ModulsForm_boa205_ch4_q4
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch4_q5,ModulsForm_boa205_ch4_q6,ModulsForm_boa205_ch4_q7,ModulsForm_boa205_ch4_q8
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch4_q9,ModulsForm_boa205_ch4_q10
""" chapter 5 """
from webse.boa205_course_chapters.forms import TableForm_boa205_ch5_t1, TableForm_boa205_ch5_t2, ModulsForm_boa205_ch5_q1, ModulsForm_boa205_ch5_q2
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch5_q3, ModulsForm_boa205_ch5_q4, ModulsForm_boa205_ch5_q5
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch5_q6, ModulsForm_boa205_ch5_q7, ModulsForm_boa205_ch5_q8
""" chapter 6 """
from webse.boa205_course_chapters.forms import TableForm_boa205_ch6_t1, TableForm_boa205_ch6_t2, ModulsForm_boa205_ch6_q1, ModulsForm_boa205_ch6_q2
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch6_q3, ModulsForm_boa205_ch6_q4, ModulsForm_boa205_ch6_q5
from webse.boa205_course_chapters.forms import ModulsForm_boa205_ch6_q6, ModulsForm_boa205_ch6_q7, ModulsForm_boa205_ch6_q8
""" Arbeidkrav 1 """
from webse.boa205_course_chapters.forms import TableForm_boa205_ak1_t1, TableForm_boa205_ak1_t2,TableForm_boa205_ak1_t3,TableForm_boa205_ak1_t4

""" Functions """
""" chapter 2a """
from webse.boa205_course_chapters.functions import normal, virkelig, dekningsdiff, produksjonresultat_normal, avvik, produktresultat_selv, virkelig_selv, dekningsdiff_produksjonresultat_selv
from webse.boa205_course_chapters.functions import produktresultat_bidra
""" chapter 2b """
from webse.boa205_course_chapters.functions import ch2a_selv,ch2a_bidra
""" chapter 3 """
from webse.boa205_course_chapters.functions import ch3_materialregnskap, ch3_lonnregnskap, ch3_standard_selv_table,ch3_selvksot_table,ch3_bidrakost_table,ch3_differanse_table
from webse.boa205_course_chapters.functions import ch3_virkelige_t4
""" Chapter 4 """
from webse.boa205_course_chapters.functions import ch4_t1_budsjett, ch4_t1_virkelige, ch4_t1_salgspris,ch4_t1_deknigsbidrag
from webse.boa205_course_chapters.functions import ch4_t1_volumavvik,ch4_t1_resultatavvik,ch4_t2_resultatavvik
from webse.boa205_course_chapters.functions import ch4_t3_virkelig_budsjettert,ch4_t3_salgsprisavvik,ch4_t3_volumsavvik,ch4_t3_salgetsavvik
""" Chapter 5 """
from webse.boa205_course_chapters.functions import ch5_t1_direkte_lonn, ch5_t1_direkte_arbeidstimer, ch5_t1_tilleggssatsen
from webse.boa205_course_chapters.functions import ch5_t1_kost_tradisjonell, ch5_t1_kost_ABC, ch5_t1_sammenlign
from webse.boa205_course_chapters.functions import ch5_t2_enheter_totalt, ch5_t2_enhetskostnad
""" Chapter 6 """
from webse.boa205_course_chapters.functions import ch6_t1_foregaende_ar, ch6_t1_maned_budsjett, ch6_t1_likviditetsbudsjett
from webse.boa205_course_chapters.functions import ch6_t2_budsjett_2020, ch6_t2_maned_2020, ch6_t2_utbetal_2020
from webse.boa205_course_chapters.functions import ch6_t2_lik_2020, ch6_t2_pavirke
""" Arbeidkrav1 """
from webse.boa205_course_chapters.functions import ak1_t1,ak1_t2,ak1_t3,ak1_t4

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
    form_boa205_ak1_t1=TableForm_boa205_ak1_t1() 
    form_boa205_ak1_t2=TableForm_boa205_ak1_t2() 
    form_boa205_ak1_t3=TableForm_boa205_ak1_t3()
    form_boa205_ak1_t4=TableForm_boa205_ak1_t4()

    if form_boa205_ak1_t1.validate_on_submit():
        """ Variables """
        fakturpris = form_boa205_ak1_t1.fakturpris.data
        indirekte_kostnader = form_boa205_ak1_t1.indirekte_kostnader.data
        fortjeneste = form_boa205_ak1_t1.fortjeneste.data
        konkurrent = form_boa205_ak1_t1.konkurrent.data

        (fakturpris_sett,intakskost_hele,intakskost_sett,faste_hele,
        faste_sett,selvkost_hele,selvkost_sett,fortjeneste_hele,
        fortjeneste_sett,salgspris_hele,salgspris_sett,mva_hele,
        mva_sett,salgspris_mva_hele,salgspris_mva_sett,
        avanse,avanse_persent,pris_konkurrent,ny_forjeneste,
        ny_forjeneste_persent)=ak1_t1(fakturpris, 
        indirekte_kostnader, fortjeneste, konkurrent)

        return render_template('boa205_course/chapters/arbeidskrav1.html', 
        title='BØA205 Økonomistyring, arbeidskrav1',
        form_boa205_ak1_t1=form_boa205_ak1_t1, 
        form_boa205_ak1_t2=form_boa205_ak1_t2, 
        form_boa205_ak1_t3=form_boa205_ak1_t3,
        form_boa205_ak1_t4=form_boa205_ak1_t4,legend='Variabler',anchor="table1",
        fakturpris=fakturpris, indirekte_kostnader=indirekte_kostnader,
        fortjeneste=fortjeneste, konkurrent=konkurrent,
        fakturpris_sett=fakturpris_sett,
        intakskost_hele=intakskost_hele,
        intakskost_sett=intakskost_sett,faste_hele=faste_hele,
        faste_sett=faste_sett,selvkost_hele=selvkost_hele,
        selvkost_sett=selvkost_sett,fortjeneste_hele=fortjeneste_hele,
        fortjeneste_sett=fortjeneste_sett,salgspris_hele=salgspris_hele,
        salgspris_sett=salgspris_sett,mva_hele=mva_hele,
        mva_sett=mva_sett,salgspris_mva_hele=salgspris_mva_hele,
        salgspris_mva_sett=salgspris_mva_sett,
        avanse=avanse,avanse_persent=avanse_persent,
        pris_konkurrent=pris_konkurrent,ny_forjeneste=ny_forjeneste,
        ny_forjeneste_persent=ny_forjeneste_persent)
    
    if form_boa205_ak1_t2.validate_on_submit():
        """ Variables """
        materiale = form_boa205_ak1_t2.materiale.data
        lonn = form_boa205_ak1_t2.lonn.data
        arbeid = form_boa205_ak1_t2.arbeid.data
        ferdig = form_boa205_ak1_t2.ferdig.data

        (endring_arbeid,endring_ferdig,endring_arbeid_table,
        endring_ferdig_table,indirekte_material,
        dekning_indirekte_material,indirekte_lonn,
        dekning_indirekte_lonn,periodens_tilv_kal,periodens_tilv_virk,
        tilv_ferdig_kal,tilv_ferdig_virk,tilv_solgte_kal,
        tilv_solgte_virk,indirekte_adm_kal,indirekte_adm_virk,
        dekning_indirekte_adm,selvkost_kal,selvkost_virk,
        produkt_resultat_kal,dekning,produksjonresultat_kal,
        produksjonresultat_virk)=ak1_t2(materiale,lonn,arbeid,ferdig)

        return render_template('boa205_course/chapters/arbeidskrav1.html', 
        title='BØA205 Økonomistyring, arbeidskrav1',
        form_boa205_ak1_t1=form_boa205_ak1_t1, 
        form_boa205_ak1_t2=form_boa205_ak1_t2,
        form_boa205_ak1_t3=form_boa205_ak1_t3, 
        form_boa205_ak1_t4=form_boa205_ak1_t4,legend='Variabler',anchor="table2",
        materiale=materiale,lonn=lonn,arbeid=arbeid,ferdig=ferdig,
        endring_arbeid=endring_arbeid,
        endring_ferdig=endring_ferdig,
        endring_arbeid_table=endring_arbeid_table,
        endring_ferdig_table=endring_ferdig_table,
        indirekte_material=indirekte_material,
        dekning_indirekte_material=dekning_indirekte_material,
        indirekte_lonn=indirekte_lonn,
        dekning_indirekte_lonn=dekning_indirekte_lonn,
        periodens_tilv_kal=periodens_tilv_kal,
        periodens_tilv_virk=periodens_tilv_virk,
        tilv_ferdig_kal=tilv_ferdig_kal,
        tilv_ferdig_virk=tilv_ferdig_virk,
        tilv_solgte_kal=tilv_solgte_kal,
        tilv_solgte_virk=tilv_solgte_virk,
        indirekte_adm_kal=indirekte_adm_kal,
        indirekte_adm_virk=indirekte_adm_virk,
        dekning_indirekte_adm=dekning_indirekte_adm,
        selvkost_kal=selvkost_kal,
        selvkost_virk=selvkost_virk,
        produkt_resultat_kal=produkt_resultat_kal,
        dekning=dekning,
        produksjonresultat_kal=produksjonresultat_kal,
        produksjonresultat_virk=produksjonresultat_virk)
    
    if form_boa205_ak1_t3.validate_on_submit():
        """ Variables """
        kjop = form_boa205_ak1_t3.kjop.data
        produksjon = form_boa205_ak1_t3.produksjon.data
        dm_240 = form_boa205_ak1_t3.dm_240.data
        dm_241 = form_boa205_ak1_t3.dm_241.data

        (kjop_sat,produksjon_sat,tilvkost_a,adm_sat,
        selvkost_a,indirek_mat_240,indirek_mat_241,
        tilvkost_240,tilvkost_241,
        av_kjop_241,av_kjop_242,av_kjop_243,
        av_kjop_sum,av_kjop_dek,
        av_produksjon_241,av_produksjon_242,av_produksjon_243,
        av_produksjon_sum,av_produksjon_dek,
        til_perioden_241,til_perioden_242,
        til_perioden_243,til_perioden_sum,
        til_ferd_241,til_ferd_242,til_ferd_243,
        til_ferd_sum,til_ferd_virk,
        behold_fv_242,behold_fv_sum,
        til_solgte_sum,til_solgte_virk,
        indirekt_adm_240,indirekt_adm_241,indirekt_adm_243,
        indirekt_adm_sum,indirekt_adm_dek,
        selv_240,selv_241,selv_243,selv_sum,selv_virk,
        resul_240,resul_241,resul_243,resul_sum,sum_dek,
        resultat_sum,resultat_virk)=ak1_t3(kjop,produksjon,dm_240,dm_241)

        return render_template('boa205_course/chapters/arbeidskrav1.html', 
        title='BØA205 Økonomistyring, arbeidskrav1',
        form_boa205_ak1_t1=form_boa205_ak1_t1, 
        form_boa205_ak1_t2=form_boa205_ak1_t2, 
        form_boa205_ak1_t3=form_boa205_ak1_t3,
        form_boa205_ak1_t4=form_boa205_ak1_t4,legend='Variabler',anchor="table3",
        kjop=kjop, produksjon=produksjon,dm_240=dm_240, dm_241=dm_241,
        kjop_sat=kjop_sat,
        produksjon_sat=produksjon_sat,
        tilvkost_a=tilvkost_a,
        adm_sat=adm_sat,
        selvkost_a=selvkost_a,
        indirek_mat_240=indirek_mat_240,
        indirek_mat_241=indirek_mat_241,
        tilvkost_240=tilvkost_240,
        tilvkost_241=tilvkost_241,
        av_kjop_241=av_kjop_241,
        av_kjop_242=av_kjop_242,
        av_kjop_243=av_kjop_243,
        av_kjop_sum=av_kjop_sum,
        av_kjop_dek=av_kjop_dek,
        av_produksjon_241=av_produksjon_241,
        av_produksjon_242=av_produksjon_242,
        av_produksjon_243=av_produksjon_243,
        av_produksjon_sum=av_produksjon_sum,
        av_produksjon_dek=av_produksjon_dek,
        til_perioden_241=til_perioden_241,
        til_perioden_242=til_perioden_242,
        til_perioden_243=til_perioden_243,
        til_perioden_sum=til_perioden_sum,
        til_ferd_241=til_ferd_241,
        til_ferd_242=til_ferd_242,
        til_ferd_243=til_ferd_243,
        til_ferd_sum=til_ferd_sum,
        til_ferd_virk=til_ferd_virk,
        behold_fv_242=behold_fv_242,
        behold_fv_sum=behold_fv_sum,
        til_solgte_sum=til_solgte_sum,
        til_solgte_virk=til_solgte_virk,
        indirekt_adm_240=indirekt_adm_240,
        indirekt_adm_241=indirekt_adm_241,
        indirekt_adm_243=indirekt_adm_243,
        indirekt_adm_sum=indirekt_adm_sum,
        indirekt_adm_dek=indirekt_adm_dek,
        selv_240=selv_240,
        selv_241=selv_241,
        selv_243=selv_243,
        selv_sum=selv_sum,
        selv_virk=selv_virk,
        resul_240=resul_240,
        resul_241=resul_241,
        resul_243=resul_243,
        resul_sum=resul_sum,
        sum_dek=sum_dek,
        resultat_sum=resultat_sum,
        resultat_virk=resultat_virk)
    
    if form_boa205_ak1_t4.validate_on_submit():
        """ Variables """
        var_adm = form_boa205_ak1_t4.var_adm.data
        enhet = form_boa205_ak1_t4.enhet.data
        faste_til = form_boa205_ak1_t4.faste_til.data
        faste_adm = form_boa205_ak1_t4.faste_adm.data

        (ts,iv_admin,minkost,kal_dek,
        vir_dek,vir_dek_vir,
        fast_til_dek,fast_adm_dek,
        fore,fast_avvik,produk_std,produk_vir,
        ls_ts,one_two,one_three)=ak1_t4(var_adm,enhet,faste_til,faste_adm)

        return render_template('boa205_course/chapters/arbeidskrav1.html', 
        title='BØA205 Økonomistyring, arbeidskrav1',
        form_boa205_ak1_t1=form_boa205_ak1_t1, 
        form_boa205_ak1_t2=form_boa205_ak1_t2, 
        form_boa205_ak1_t3=form_boa205_ak1_t3,
        form_boa205_ak1_t4=form_boa205_ak1_t4,
        legend='Variabler',anchor="table4",
        var_adm=var_adm,enhet=enhet,faste_til=faste_til,faste_adm=faste_adm,
        ts=ts, iv_admin=iv_admin,minkost=minkost,kal_dek=kal_dek,
        vir_dek=vir_dek,vir_dek_vir=vir_dek_vir,
        fast_til_dek=fast_til_dek,fast_adm_dek=fast_adm_dek,
        fore=fore,fast_avvik=fast_avvik,
        produk_std=produk_std,produk_vir=produk_vir,
        ls_ts=ls_ts,one_two=one_two,one_three=one_three)

    return render_template('boa205_course/chapters/arbeidskrav1.html', 
        title='BØA205 Økonomistyring, arbeidskrav1',
        form_boa205_ak1_t1=form_boa205_ak1_t1,
        form_boa205_ak1_t2=form_boa205_ak1_t2,
        form_boa205_ak1_t3=form_boa205_ak1_t3,
        form_boa205_ak1_t4=form_boa205_ak1_t4)

#Chapter 4
@boa205_course_chapters.route('/boa205_course/kapitel4', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch4():
    form_boa205_ch4_t1=TableForm_boa205_ch4_t1()
    form_boa205_ch4_t2=TableForm_boa205_ch4_t2()
    form_boa205_ch4_t3=TableForm_boa205_ch4_t3()
    form_boa205_ch4_q1 = ModulsForm_boa205_ch4_q1()
    form_boa205_ch4_q2 = ModulsForm_boa205_ch4_q2()
    form_boa205_ch4_q3 = ModulsForm_boa205_ch4_q3()
    form_boa205_ch4_q4 = ModulsForm_boa205_ch4_q4()
    form_boa205_ch4_q5 = ModulsForm_boa205_ch4_q5()
    form_boa205_ch4_q6 = ModulsForm_boa205_ch4_q6()
    form_boa205_ch4_q7 = ModulsForm_boa205_ch4_q7()
    form_boa205_ch4_q8 = ModulsForm_boa205_ch4_q8()
    form_boa205_ch4_q9 = ModulsForm_boa205_ch4_q9()
    form_boa205_ch4_q10 = ModulsForm_boa205_ch4_q10()

    if form_boa205_ch4_t1.validate_on_submit():
        """ Variables """
        budsjettert_pris_produkt_alfa = form_boa205_ch4_t1.budsjettert_pris_produkt_alfa.data
        budsjettert_pris_produkt_omega = form_boa205_ch4_t1.budsjettert_pris_produkt_omega.data
        virkelig_salg_i_enheter_alfa = form_boa205_ch4_t1.virkelig_salg_i_enheter_alfa.data
        virkelig_salg_i_enheter_omega = form_boa205_ch4_t1.virkelig_salg_i_enheter_omega.data

        (inntekter_alfa,inntekter_omega,inntekter_totalt)=ch4_t1_budsjett(budsjettert_pris_produkt_alfa,budsjettert_pris_produkt_omega)

        (virkelige_pris_alfa,virkelige_pris_omega,virkelige_DB_alfa,
         virkelige_DB_omega)=ch4_t1_virkelige(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)
        
        (salgsprisavvik_alfa,salgsprisavvik_omega,salgsprisavvik_total)=ch4_t1_salgspris(budsjettert_pris_produkt_alfa,budsjettert_pris_produkt_omega,
                                                                    virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)

        (deknigsbidragavvik_alfa,deknigsbidragavvik_omega,
         deknigsbidragavvik_total)=ch4_t1_deknigsbidrag(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)
        
        (volumavvik_alfa,volumavvik_omega,volumavvik_total)=ch4_t1_volumavvik(virkelig_salg_i_enheter_alfa,
            virkelig_salg_i_enheter_omega)
        
        (salgets_resultatavvik_alfa,salgets_resultatavvik_omega,
         salgets_resultatavvik_total)=ch4_t1_resultatavvik(budsjettert_pris_produkt_alfa,budsjettert_pris_produkt_omega,
            virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)

        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="table1",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10,
        budsjettert_pris_produkt_alfa=budsjettert_pris_produkt_alfa,
        budsjettert_pris_produkt_omega=budsjettert_pris_produkt_omega,
        virkelig_salg_i_enheter_alfa=virkelig_salg_i_enheter_alfa,
        virkelig_salg_i_enheter_omega=virkelig_salg_i_enheter_omega,
        inntekter_alfa=inntekter_alfa,inntekter_omega=inntekter_omega,inntekter_totalt=inntekter_totalt,
        virkelige_pris_alfa=virkelige_pris_alfa,virkelige_pris_omega=virkelige_pris_omega,
        virkelige_DB_alfa=virkelige_DB_alfa,virkelige_DB_omega=virkelige_DB_omega,
        salgsprisavvik_alfa=salgsprisavvik_alfa,salgsprisavvik_omega=salgsprisavvik_omega,
        salgsprisavvik_total=salgsprisavvik_total,deknigsbidragavvik_alfa=deknigsbidragavvik_alfa,
        deknigsbidragavvik_omega=deknigsbidragavvik_omega,deknigsbidragavvik_total=deknigsbidragavvik_total,
        volumavvik_alfa=volumavvik_alfa,volumavvik_omega=volumavvik_omega,volumavvik_total=volumavvik_total,
        salgets_resultatavvik_alfa=salgets_resultatavvik_alfa,salgets_resultatavvik_omega=salgets_resultatavvik_omega,
        salgets_resultatavvik_total=salgets_resultatavvik_total)
    
    if form_boa205_ch4_t2.validate_on_submit():
        """ Variables """
        budsjettert_pris_tex = form_boa205_ch4_t2.budsjettert_pris_tex.data
        budsjettert_pris_mex = form_boa205_ch4_t2.budsjettert_pris_mex.data
        budsjettert_DB_tex = form_boa205_ch4_t2.budsjettert_DB_tex.data
        budsjettert_DB_mex = form_boa205_ch4_t2.budsjettert_DB_mex.data

        (prisavvik_tex,prisavvik_mex,prisavvik_total,volumavvik_tex,volumavvik_mex,
           volumavvik_total,salgets_resultatavvik_tex,salgets_resultatavvik_mex,
           salgets_resultatavvik_total)=ch4_t2_resultatavvik(budsjettert_pris_tex,budsjettert_pris_mex,
           budsjettert_DB_tex,budsjettert_DB_mex)
        
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="table2",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10,
        budsjettert_pris_tex=budsjettert_pris_tex, budsjettert_pris_mex=budsjettert_pris_mex,
        budsjettert_DB_tex=budsjettert_DB_tex, budsjettert_DB_mex=budsjettert_DB_mex,
        prisavvik_tex=prisavvik_tex,prisavvik_mex=prisavvik_mex,prisavvik_total=prisavvik_total,
        volumavvik_tex=volumavvik_tex,volumavvik_mex=volumavvik_mex,volumavvik_total=volumavvik_total,
        salgets_resultatavvik_tex=salgets_resultatavvik_tex,salgets_resultatavvik_mex=salgets_resultatavvik_mex,
        salgets_resultatavvik_total=salgets_resultatavvik_total)
    
    if form_boa205_ch4_t3.validate_on_submit():
        """ Variables """
        virkelig_salgsvolum_3031 = form_boa205_ch4_t3.virkelig_salgsvolum_3031.data
        virkelig_salgsvolum_3032 = form_boa205_ch4_t3.virkelig_salgsvolum_3032.data
        db_3031 = form_boa205_ch4_t3.db_3031.data
        db_3032 = form_boa205_ch4_t3.db_3032.data

        (virkelig_pris_3031,virkelig_pris_3032)=ch4_t3_virkelig_budsjettert(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032)
        (salgsprisavvik_3031,salgsprisavvik_3032,salgsprisavvik_total)=ch4_t3_salgsprisavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032)
        (volumavvik_3031,volumavvik_3032,volumavvik_total)=ch4_t3_volumsavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032,db_3031,db_3032)
        (salgets_3031,salgets_3032,salgets_total)=ch4_t3_salgetsavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032,db_3031,db_3032)

        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="table3",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10,
        virkelig_salgsvolum_3031=virkelig_salgsvolum_3031, virkelig_salgsvolum_3032=virkelig_salgsvolum_3032,
        db_3031=db_3031,db_3032=db_3032,virkelig_pris_3031=virkelig_pris_3031,virkelig_pris_3032=virkelig_pris_3032,
        salgsprisavvik_3031=salgsprisavvik_3031,salgsprisavvik_3032=salgsprisavvik_3032,salgsprisavvik_total=salgsprisavvik_total,
        volumavvik_3031=volumavvik_3031,volumavvik_3032=volumavvik_3032,volumavvik_total=volumavvik_total,
        salgets_3031=salgets_3031,salgets_3032=salgets_3032,salgets_total=salgets_total)

    
    if form_boa205_ch4_q1.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q1.type.data, author=current_user)
        if moduls.question_str == '-6000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q1_q2",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q2.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q2.type.data, author=current_user)
        if moduls.question_str == '6654':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q1_q2",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q3.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q3.type.data, author=current_user)
        if moduls.question_str == '8.1':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q3_q4",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q4.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q4.type.data, author=current_user)
        if moduls.question_str == '-2146':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q3_q4",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q5.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q5.type.data, author=current_user)
        if moduls.question_str == '-1000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q5_q6",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q6.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q6.type.data, author=current_user)
        if moduls.question_str == '13000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q5_q6",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q7.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q7.type.data, author=current_user)
        if moduls.question_str == '-1750':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 7
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q7_q8",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q8.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q8.type.data, author=current_user)
        if moduls.question_str == '6720':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 8
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q7_q8",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
        
    if form_boa205_ch4_q9.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q9.type.data, author=current_user)
        if moduls.question_str == '14440':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 9
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q9_q10",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)
    
    if form_boa205_ch4_q10.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch4_q10.type.data, author=current_user)
        if moduls.question_str == '-7450':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch4'
        moduls.title_ch = 'Kapitel 4. Salgets resultatavvik'
        moduls.question_num = 10
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch4'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',anchor="ch4_q9_q10",
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)

    return render_template('boa205_course/chapters/ch4.html', title='BØA205 Økonomistyring, kapittel 4',
        form_boa205_ch4_t1=form_boa205_ch4_t1, form_boa205_ch4_t2=form_boa205_ch4_t2, 
        form_boa205_ch4_t3=form_boa205_ch4_t3, legend='Variabler',
        form_boa205_ch4_q1=form_boa205_ch4_q1, form_boa205_ch4_q2=form_boa205_ch4_q2,
        form_boa205_ch4_q3=form_boa205_ch4_q3, form_boa205_ch4_q4=form_boa205_ch4_q4,
        form_boa205_ch4_q5=form_boa205_ch4_q5, form_boa205_ch4_q6=form_boa205_ch4_q6,
        form_boa205_ch4_q7=form_boa205_ch4_q7, form_boa205_ch4_q8=form_boa205_ch4_q8,
        form_boa205_ch4_q9=form_boa205_ch4_q9, form_boa205_ch4_q10=form_boa205_ch4_q10)

#Chapter 5
@boa205_course_chapters.route('/boa205_course/kapitel5', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch5():
    form_boa205_ch5_t1=TableForm_boa205_ch5_t1()
    form_boa205_ch5_t2=TableForm_boa205_ch5_t2()
    form_boa205_ch5_q1 = ModulsForm_boa205_ch5_q1()
    form_boa205_ch5_q2 = ModulsForm_boa205_ch5_q2()
    form_boa205_ch5_q3 = ModulsForm_boa205_ch5_q3()
    form_boa205_ch5_q4 = ModulsForm_boa205_ch5_q4()
    form_boa205_ch5_q5 = ModulsForm_boa205_ch5_q5()
    form_boa205_ch5_q6 = ModulsForm_boa205_ch5_q6()
    form_boa205_ch5_q7 = ModulsForm_boa205_ch5_q7()
    form_boa205_ch5_q8 = ModulsForm_boa205_ch5_q8()

    if form_boa205_ch5_t1.validate_on_submit():
        """ Variables """
        enheter_alfa = form_boa205_ch5_t1.enheter_alfa.data
        enheter_beta = form_boa205_ch5_t1.enheter_beta.data
        timer_alfa = form_boa205_ch5_t1.timer_alfa.data
        timer_beta = form_boa205_ch5_t1.timer_beta.data

        (direkte_lonn_alfa,direkte_lonn_beta)=ch5_t1_direkte_lonn(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)
        
        (direkte_arbeidstimer_alfa,direkte_arbeidstimer_beta,
         direkte_arbeidstimer_totalt)=ch5_t1_direkte_arbeidstimer(enheter_alfa, enheter_beta, 
        timer_alfa, timer_beta)

        (tilleggssatsen_indirekte_lonn,tilleggssatsen_indirekte_lonn_tekst)=ch5_t1_tilleggssatsen(enheter_alfa, enheter_beta, timer_alfa, timer_beta)

        (kost_tradisjonell_indirekte_tilv_kostnad_alfa, kost_tradisjonell_indirekte_tilv_kostnad_beta,
        kost_tradisjonell_enhetkost_alfa, kost_tradisjonell_enhetkost_beta)=ch5_t1_kost_tradisjonell(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)

        (kost_ABC_indirekte_lonn_alfa,kost_ABC_indirekte_lonn_beta,
        kost_ABC_alfa,kost_ABC_beta,kost_ABC_indirekte_alfa,
        kost_ABC_indirekte_beta,kost_ABC_enhetskost_alfa,kost_ABC_enhetskost_beta)=ch5_t1_kost_ABC(enheter_alfa, enheter_beta, 
        timer_alfa, timer_beta)

        (sammenlign_differese_alfa,sammenlign_differese_beta,sammenlign_totalt_alfa,
        sammenlign_totalt_beta)=ch5_t1_sammenlign(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)

        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="table1",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8,
        direkte_lonn_alfa=direkte_lonn_alfa, direkte_lonn_beta=direkte_lonn_beta,
        timer_alfa=timer_alfa, timer_beta=timer_beta,enheter_alfa=enheter_alfa, enheter_beta=enheter_beta,
        direkte_arbeidstimer_alfa=direkte_arbeidstimer_alfa, direkte_arbeidstimer_beta=direkte_arbeidstimer_beta,
        direkte_arbeidstimer_totalt=direkte_arbeidstimer_totalt,
        tilleggssatsen_indirekte_lonn=tilleggssatsen_indirekte_lonn,
        kost_tradisjonell_indirekte_tilv_kostnad_alfa=kost_tradisjonell_indirekte_tilv_kostnad_alfa, 
        kost_tradisjonell_indirekte_tilv_kostnad_beta=kost_tradisjonell_indirekte_tilv_kostnad_beta,
        kost_tradisjonell_enhetkost_alfa=kost_tradisjonell_enhetkost_alfa,
        kost_tradisjonell_enhetkost_beta=kost_tradisjonell_enhetkost_beta,
        kost_ABC_indirekte_lonn_alfa=kost_ABC_indirekte_lonn_alfa,
        kost_ABC_indirekte_lonn_beta=kost_ABC_indirekte_lonn_beta,
        kost_ABC_alfa=kost_ABC_alfa,kost_ABC_beta=kost_ABC_beta,
        kost_ABC_indirekte_alfa=kost_ABC_indirekte_alfa,
        kost_ABC_indirekte_beta=kost_ABC_indirekte_beta,
        kost_ABC_enhetskost_alfa=kost_ABC_enhetskost_alfa,
        kost_ABC_enhetskost_beta=kost_ABC_enhetskost_beta,
        sammenlign_differese_alfa=sammenlign_differese_alfa,
        sammenlign_differese_beta=sammenlign_differese_beta,
        sammenlign_totalt_alfa=sammenlign_totalt_alfa,
        sammenlign_totalt_beta=sammenlign_totalt_beta,
        tilleggssatsen_indirekte_lonn_tekst=tilleggssatsen_indirekte_lonn_tekst)
    
    if form_boa205_ch5_t2.validate_on_submit():
        """ Variables """
        enheter_a = form_boa205_ch5_t2.enheter_a.data
        enheter_b = form_boa205_ch5_t2.enheter_b.data
        timer_a = form_boa205_ch5_t2.timer_a.data
        timer_b = form_boa205_ch5_t2.timer_b.data

        enheter_totalt=ch5_t2_enheter_totalt(enheter_a, enheter_b, timer_a, timer_b)

        (maskinering_aktivitet_a,maskinering_kostnad_a,
        sum_indirekte_kostnad_a,indirekte_kostnader_per_enhet_a, enhetskostnad_a,
        maskinering_aktivitet_b,maskinering_kostnad_b,
        sum_indirekte_kostnad_b,indirekte_kostnader_per_enhet_b, 
        enhetskostnad_b)=ch5_t2_enhetskostnad(enheter_a, enheter_b, timer_a, timer_b)

        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
            form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
            legend='Variabler',anchor="table2",
            form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
            form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
            form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
            form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8,
            enheter_a=enheter_a, enheter_b=enheter_b,
            timer_a=timer_a, timer_b=timer_b,
            enheter_totalt=enheter_totalt,
            maskinering_aktivitet_a=maskinering_aktivitet_a,
            maskinering_kostnad_a=maskinering_kostnad_a,
            sum_indirekte_kostnad_a=sum_indirekte_kostnad_a,
            indirekte_kostnader_per_enhet_a=indirekte_kostnader_per_enhet_a, 
            enhetskostnad_a=enhetskostnad_a,
            maskinering_aktivitet_b=maskinering_aktivitet_b,
            maskinering_kostnad_b=maskinering_kostnad_b,
            sum_indirekte_kostnad_b=sum_indirekte_kostnad_b,
            indirekte_kostnader_per_enhet_b=indirekte_kostnader_per_enhet_b, 
            enhetskostnad_b=enhetskostnad_b)
    
    if form_boa205_ch5_q1.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q1.type.data, author=current_user)
        if moduls.question_str == '3752000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q1_q2",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)
    
    if form_boa205_ch5_q2.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q2.type.data, author=current_user)
        if moduls.question_str == '3790':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q1_q2",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)
    
    if form_boa205_ch5_q3.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q3.type.data, author=current_user)
        if moduls.question_str == '3607':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q3_q4",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)
    
    if form_boa205_ch5_q4.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q4.type.data, author=current_user)
        if moduls.question_str == '5393':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q3_q4",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)
    
    if form_boa205_ch5_q5.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q5.type.data, author=current_user)
        if moduls.question_str == '27392000':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q5_q6",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)
    
    if form_boa205_ch5_q6.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q6.type.data, author=current_user)
        if moduls.question_str == '3113.8':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q5_q6",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)
    
    if form_boa205_ch5_q7.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q7.type.data, author=current_user)
        if moduls.question_str == '935.1':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 7
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q7_q8",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)

    if form_boa205_ch5_q8.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch5_q8.type.data, author=current_user)
        if moduls.question_str == '3652.8':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch5'
        moduls.title_ch = 'Kapitel 5. Aktivitetsbasert kalkulasjon'
        moduls.question_num = 8
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch5'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
        legend='Variabler',anchor="ch5_q7_q8",
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)

    return render_template('boa205_course/chapters/ch5.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch5_t1=form_boa205_ch5_t1, form_boa205_ch5_t2=form_boa205_ch5_t2,
          legend='Variabler',
        form_boa205_ch5_q1=form_boa205_ch5_q1, form_boa205_ch5_q2=form_boa205_ch5_q2,
        form_boa205_ch5_q3=form_boa205_ch5_q3, form_boa205_ch5_q4=form_boa205_ch5_q4,
        form_boa205_ch5_q5=form_boa205_ch5_q5, form_boa205_ch5_q6=form_boa205_ch5_q6,
        form_boa205_ch5_q7=form_boa205_ch5_q7, form_boa205_ch5_q8=form_boa205_ch5_q8)

@boa205_course_chapters.route('/boa205_course/kapitel6', methods=['GET', 'POST'])
@login_required
def boa205_course_chapters_ch6():
    form_boa205_ch6_t1=TableForm_boa205_ch6_t1()
    form_boa205_ch6_t2=TableForm_boa205_ch6_t2()
    form_boa205_ch6_q1 = ModulsForm_boa205_ch6_q1()
    form_boa205_ch6_q2 = ModulsForm_boa205_ch6_q2()
    form_boa205_ch6_q3 = ModulsForm_boa205_ch6_q3()
    form_boa205_ch6_q4 = ModulsForm_boa205_ch6_q4()
    form_boa205_ch6_q5 = ModulsForm_boa205_ch6_q5()
    form_boa205_ch6_q6 = ModulsForm_boa205_ch6_q6()
    form_boa205_ch6_q7 = ModulsForm_boa205_ch6_q7()
    form_boa205_ch6_q8 = ModulsForm_boa205_ch6_q8()

    if form_boa205_ch6_t1.validate_on_submit():
        """ Variables """
        husleie_21 = form_boa205_ch6_t1.husleie_21.data
        husleie_okning_22 = form_boa205_ch6_t1.husleie_okning_22.data
        bilkostnader_21 = form_boa205_ch6_t1.bilkostnader_21.data
        bilkostnader_okning_22 = form_boa205_ch6_t1.bilkostnader_okning_22.data

        (fa_husleie_percentage_21,fa_husleie_endring,fa_husleie_22,fa_husleie_percentage_22,
        fa_bilkostnader_percentage_21,fa_bilkostnader_endring,fa_bilkostnader_22,fa_bilkostnader_percentage_22,
        fa_sum_drift_21,fa_sum_drift_percentage_21,fa_sum_drift_22,fa_sum_drift_percentage_22,
        fa_driftresultat_21,fa_driftresultat_percentage_21,fa_driftresultat_22,fa_driftresultat_percentage_22,
        fa_resultat_21,
        fa_resultat_percentage_21,fa_resultat_22,fa_resultat_percentage_22)=ch6_t1_foregaende_ar(husleie_21, 
            husleie_okning_22, bilkostnader_21, bilkostnader_okning_22)
        
        (mb_husleie_maned,mb_husleie_kvartal,mb_bilkostnader_maned,mb_bilkostnader_kvartal,
        mb_sum_drift_januar,mb_sum_drift_februar,mb_sum_drift_mars,mb_sum_drift_kvartal,
        mb_driftsresultat_januar,mb_driftsresultat_februar,mb_driftsresultat_mars,mb_driftsresultat_kvartal,
        mb_resultat_januar,mb_resultat_februar,mb_resultat_mars,
        mb_resultat_kvartal)=ch6_t1_maned_budsjett(husleie_21, husleie_okning_22, 
            bilkostnader_21, bilkostnader_okning_22)
        
        (l_husleie_maned,l_husleie_kvartal,l_bilkostnader_maned,l_bilkostnader_kvartal,
        l_sum_utbetalinger_januar,l_sum_utbetalinger_februar,l_sum_utbetalinger_mars, 
        l_sum_utbetalinger_kvartal,l_inn_ut_januar,l_inn_ut_februar,l_inn_ut_mars,
        l_inn_ut_kvartal,
        l_lik_reserveUB_januar,l_lik_reserveUB_februar,l_lik_reserveUB_mars,
        l_lik_reserveIB_februar,l_lik_reserveIB_mars)=ch6_t1_likviditetsbudsjett(husleie_21, husleie_okning_22, 
        bilkostnader_21, bilkostnader_okning_22)

        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="table1",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8,
        husleie_21=husleie_21, husleie_okning_22=husleie_okning_22,
        bilkostnader_21=bilkostnader_21, bilkostnader_okning_22=bilkostnader_okning_22,
        fa_husleie_percentage_21=fa_husleie_percentage_21,
        fa_husleie_endring=fa_husleie_endring,
        fa_husleie_22=fa_husleie_22,fa_husleie_percentage_22=fa_husleie_percentage_22,
        fa_bilkostnader_percentage_21=fa_bilkostnader_percentage_21,
        fa_bilkostnader_endring=fa_bilkostnader_endring,
        fa_bilkostnader_22=fa_bilkostnader_22,
        fa_bilkostnader_percentage_22=fa_bilkostnader_percentage_22,
        fa_sum_drift_21=fa_sum_drift_21,fa_sum_drift_percentage_21=fa_sum_drift_percentage_21,
        fa_sum_drift_22=fa_sum_drift_22,fa_sum_drift_percentage_22=fa_sum_drift_percentage_22,
        fa_driftresultat_21=fa_driftresultat_21,
        fa_driftresultat_percentage_21=fa_driftresultat_percentage_21,
        fa_driftresultat_22=fa_driftresultat_22,
        fa_driftresultat_percentage_22=fa_driftresultat_percentage_22,
        fa_resultat_21=fa_resultat_21,fa_resultat_percentage_21=fa_resultat_percentage_21,
        fa_resultat_22=fa_resultat_22,fa_resultat_percentage_22=fa_resultat_percentage_22,
        mb_husleie_maned=mb_husleie_maned,mb_husleie_kvartal=mb_husleie_kvartal,
        mb_bilkostnader_maned=mb_bilkostnader_maned,mb_bilkostnader_kvartal=mb_bilkostnader_kvartal,
        mb_sum_drift_januar=mb_sum_drift_januar,mb_sum_drift_februar=mb_sum_drift_februar,
        mb_sum_drift_mars=mb_sum_drift_mars,mb_sum_drift_kvartal=mb_sum_drift_kvartal,
        mb_driftsresultat_januar=mb_driftsresultat_januar,
        mb_driftsresultat_februar=mb_driftsresultat_februar,
        mb_driftsresultat_mars=mb_driftsresultat_mars,
        mb_driftsresultat_kvartal=mb_driftsresultat_kvartal,
        mb_resultat_januar=mb_resultat_januar,mb_resultat_februar=mb_resultat_februar,
        mb_resultat_mars=mb_resultat_mars,mb_resultat_kvartal=mb_resultat_kvartal,
        l_husleie_maned=l_husleie_maned,l_husleie_kvartal=l_husleie_kvartal,
        l_bilkostnader_maned=l_bilkostnader_maned,
        l_bilkostnader_kvartal=l_bilkostnader_kvartal,
        l_sum_utbetalinger_januar=l_sum_utbetalinger_januar,
        l_sum_utbetalinger_februar=l_sum_utbetalinger_februar,
        l_sum_utbetalinger_mars=l_sum_utbetalinger_mars, 
        l_sum_utbetalinger_kvartal=l_sum_utbetalinger_kvartal,
        l_inn_ut_januar=l_inn_ut_januar,l_inn_ut_februar=l_inn_ut_februar,
        l_inn_ut_mars=l_inn_ut_mars, l_inn_ut_kvartal=l_inn_ut_kvartal,
        l_lik_reserveUB_januar=l_lik_reserveUB_januar,
        l_lik_reserveUB_februar=l_lik_reserveUB_februar,
        l_lik_reserveUB_mars=l_lik_reserveUB_mars,
        l_lik_reserveIB_februar=l_lik_reserveIB_februar,
        l_lik_reserveIB_mars=l_lik_reserveIB_mars)
    
    if form_boa205_ch6_t2.validate_on_submit():
        """ Variables """
        varekostnad_19= form_boa205_ch6_t2.varekostnad_19.data
        varekostnad_okning_20= form_boa205_ch6_t2.varekostnad_okning_20.data
        lonn_19= form_boa205_ch6_t2.lonn_19.data
        lonn_okning_20= form_boa205_ch6_t2.lonn_okning_20.data

        (b_20_varekostnad_percentage_2019,b_20_varekostnad_2020,
        b_20_lonn_percentage_2019,b_20_lonn_2020,b_20_lonn_percentage_2020,
        b_20_sum_kostnader_2019,b_20_sum_kostnader_percentage_2019,
        b_20_sum_kostnader_2020,b_20_sum_kostnader_percentage_2020,b_20_drit_2019,
        b_20_drit_percentage_2019,b_20_drit_2020,b_20_drit_percentage_2020,
        b_20_resultat_2019,b_20_drit__percentage_2019,b_20_resultat_2020,
        b_20_drit__percentage_2020)=ch6_t2_budsjett_2020(varekostnad_19, varekostnad_okning_20, 
        lonn_19, lonn_okning_20)

        (m_20_varkostnad_maned,m_20_varkostnad_kvartal,
        m_20_lonn_maned,m_20_lonn_kvartal,m_20_sum_kostnader_maned,
        m_20_sum_kostnader_kvartal,m_20_drit_maned,m_20_drit_kvartal,
        m_20_resultat_maned,m_20_resultat_kvartal)=ch6_t2_maned_2020(varekostnad_19, 
        varekostnad_okning_20, lonn_19, lonn_okning_20)

        (u_20_mva_maned,u_20_mva_kvartal,u_20_vare_maned,u_20_vare_kvartal,
        u_20_kjop_maned,u_20_sum_utbetal_januar,
        u_20_totalt_utbetal_kvartal)=ch6_t2_utbetal_2020(varekostnad_19, 
        varekostnad_okning_20, lonn_19, lonn_okning_20)

        (lik_20_lonn_januar,lik_20_lonn_sum, lik_20_sum_utbetaling_januar,
        lik_20_sum_utbetaling_februar,lik_20_sum_utbetaling_mars,lik_20_sum_utbetaling_sum,
        lik_20_inn_ut_januar,lik_20_inn_ut_februar,lik_20_inn_ut_mars,
        lik_20_inn_ut_sum,lik_20_UB_januar,lik_20_UB_februar,
        lik_20_UB_mars)=ch6_t2_lik_2020(varekostnad_19, varekostnad_okning_20, 
        lonn_19, lonn_okning_20)

        (p_varekostnad_maned,p_varekjop_maned,p_mva,
        p_kjop_maned,p_sum_utbetaling_februar,p_sum_utbetaling_mars,
        p_sum_utbetaling_UB,p_total_utbetaling,p_lik)=ch6_t2_pavirke(varekostnad_19, 
        varekostnad_okning_20, lonn_19, lonn_okning_20)


        return render_template('boa205_course/chapters/ch6.html', 
        title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="table2",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8,
        varekostnad_19=varekostnad_19,varekostnad_okning_20=varekostnad_okning_20,
        lonn_19=lonn_19, lonn_okning_20=lonn_okning_20,
        b_20_varekostnad_percentage_2019=b_20_varekostnad_percentage_2019,
        b_20_varekostnad_2020=b_20_varekostnad_2020,
        b_20_lonn_percentage_2019=b_20_lonn_percentage_2019,
        b_20_lonn_2020=b_20_lonn_2020,
        b_20_lonn_percentage_2020=b_20_lonn_percentage_2020,
        b_20_sum_kostnader_2019=b_20_sum_kostnader_2019,
        b_20_sum_kostnader_percentage_2019=b_20_sum_kostnader_percentage_2019,
        b_20_sum_kostnader_2020=b_20_sum_kostnader_2020,
        b_20_sum_kostnader_percentage_2020=b_20_sum_kostnader_percentage_2020,
        b_20_drit_2019=b_20_drit_2019,
        b_20_drit_percentage_2019=b_20_drit_percentage_2019,
        b_20_drit_2020=b_20_drit_2020,b_20_drit_percentage_2020=b_20_drit_percentage_2020,
        b_20_resultat_2019=b_20_resultat_2019,
        b_20_drit__percentage_2019=b_20_drit__percentage_2019,
        b_20_resultat_2020=b_20_resultat_2020,
        b_20_drit__percentage_2020=b_20_drit__percentage_2020,
        m_20_varkostnad_maned=m_20_varkostnad_maned,
        m_20_varkostnad_kvartal=m_20_varkostnad_kvartal,
        m_20_lonn_maned=m_20_lonn_maned,
        m_20_lonn_kvartal=m_20_lonn_kvartal,
        m_20_sum_kostnader_maned=m_20_sum_kostnader_maned,
        m_20_sum_kostnader_kvartal=m_20_sum_kostnader_kvartal,
        m_20_drit_maned=m_20_drit_maned,m_20_drit_kvartal=m_20_drit_kvartal,
        m_20_resultat_maned=m_20_resultat_maned,
        m_20_resultat_kvartal=m_20_resultat_kvartal,
        u_20_mva_maned=u_20_mva_maned,
        u_20_mva_kvartal=u_20_mva_kvartal,
        u_20_vare_maned=u_20_vare_maned,
        u_20_vare_kvartal=u_20_vare_kvartal,
        u_20_kjop_maned=u_20_kjop_maned,
        u_20_sum_utbetal_januar=u_20_sum_utbetal_januar,
        u_20_totalt_utbetal_kvartal=u_20_totalt_utbetal_kvartal,
        lik_20_lonn_januar=lik_20_lonn_januar,
        lik_20_lonn_sum=lik_20_lonn_sum, 
        lik_20_sum_utbetaling_januar=lik_20_sum_utbetaling_januar,
        lik_20_sum_utbetaling_februar=lik_20_sum_utbetaling_februar,
        lik_20_sum_utbetaling_mars=lik_20_sum_utbetaling_mars,
        lik_20_sum_utbetaling_sum=lik_20_sum_utbetaling_sum,
        lik_20_inn_ut_januar=lik_20_inn_ut_januar,
        lik_20_inn_ut_februar=lik_20_inn_ut_februar,
        lik_20_inn_ut_mars=lik_20_inn_ut_mars,
        lik_20_inn_ut_sum=lik_20_inn_ut_sum,
        lik_20_UB_januar=lik_20_UB_januar,
        lik_20_UB_februar=lik_20_UB_februar,
        lik_20_UB_mars=lik_20_UB_mars,
        p_varekostnad_maned=p_varekostnad_maned,
        p_varekjop_maned=p_varekjop_maned,p_mva=p_mva,
        p_kjop_maned=p_kjop_maned,
        p_sum_utbetaling_februar=p_sum_utbetaling_februar,
        p_sum_utbetaling_mars=p_sum_utbetaling_mars,
        p_sum_utbetaling_UB=p_sum_utbetaling_UB,
        p_total_utbetaling=p_total_utbetaling,p_lik=p_lik)
        
    
    if form_boa205_ch6_q1.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q1.type.data, author=current_user)
        if moduls.question_str == '1.22':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 1
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 5',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q1_q2",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
    
    if form_boa205_ch6_q2.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q2.type.data, author=current_user)
        if moduls.question_str == '855032':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 2
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q1_q2",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
    
    if form_boa205_ch6_q3.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q3.type.data, author=current_user)
        if moduls.question_str == '8664.2':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 3
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q3_q4",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
    
    if form_boa205_ch6_q4.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q4.type.data, author=current_user)
        if moduls.question_str == '-56960':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 4
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q3_q4",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
    
    if form_boa205_ch6_q5.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q5.type.data, author=current_user)
        if moduls.question_str == '1605684':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 5
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q5_q6",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
    
    if form_boa205_ch6_q6.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q6.type.data, author=current_user)
        if moduls.question_str == '179687.5':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 6
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q5_q6",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
    
    if form_boa205_ch6_q7.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q7.type.data, author=current_user)
        if moduls.question_str == '683666.1':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 7
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q7_q8",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
    
    if form_boa205_ch6_q8.validate_on_submit():
        moduls = ModulsGD(question_str=form_boa205_ch6_q8.type.data, author=current_user)
        if moduls.question_str == '523437.6':
            moduls.question_result = 1
        else:
            moduls.question_result = 0
        moduls.title_mo = 'boa205_ch6'
        moduls.title_ch = 'Kapitel 6. Budsjettering'
        moduls.question_num = 8
        moduls.question_option = 50 
        moduls.question_section = 'boa205_ch6'       
        db.session.add(moduls)
        db.session.commit()
        return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        legend='Variabler',anchor="ch6_q7_q8",
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)

    return render_template('boa205_course/chapters/ch6.html', title='BØA205 Økonomistyring, kapittel 6',
        form_boa205_ch6_t1=form_boa205_ch6_t1, form_boa205_ch6_t2=form_boa205_ch6_t2,
        form_boa205_ch6_q1=form_boa205_ch6_q1, form_boa205_ch6_q2=form_boa205_ch6_q2,
        form_boa205_ch6_q3=form_boa205_ch6_q3, form_boa205_ch6_q4=form_boa205_ch6_q4,
        form_boa205_ch6_q5=form_boa205_ch6_q5, form_boa205_ch6_q6=form_boa205_ch6_q6,
        form_boa205_ch6_q7=form_boa205_ch6_q7, form_boa205_ch6_q8=form_boa205_ch6_q8)
