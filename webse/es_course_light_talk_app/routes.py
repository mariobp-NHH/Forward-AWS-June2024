from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from webse.models import SentenceES
from webse import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from webse.es_course_light_talk_app.forms import AddForm, SelectForm, VerifyForm1, VerifyForm2One, VerifyForm2Two, VerifyForm2Three, YourSentencesForm
from sqlalchemy.sql.expression import func
import random


from sqlalchemy.sql.expression import func
import random

es_course_light_talk_app=Blueprint('es_course_light_talk_app',__name__)


#Light Talk app, main page
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app')
@login_required
def es_course_light_talk_app_home():
    return render_template('es_course/es_course_light_talk_app/light_talk_app.html', title='es_course_light_talk_app')


#Add a new sentence
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app/añadir_frase', methods=['GET','POST'])
@login_required
def add_sentence():
    form = AddForm()
    if form.validate_on_submit():
        incorrect_sentence = form.incorrect_sentence.data
        correct_sentence_one = form.correct_sentence_one.data
        correct_sentence_two = form.correct_sentence_two.data
        correct_sentence_three = form.correct_sentence_three.data
        your_sentence = "none"
        objective = form.objective.data
        source = form.source.data
        result_string = "none"
        result_num= "nan"
        group = 'general'
        university = 'University of Salamanca'
        year = 2024
 
        sentence = SentenceES(incorrect_sentence=incorrect_sentence, correct_sentence_one=correct_sentence_one, correct_sentence_two=correct_sentence_two, correct_sentence_three=correct_sentence_three, correct_sentence_four="none", your_sentence=your_sentence, objective=objective, source=source, result_string=result_string, result_num=result_num,  group=group, university=university, year=year, author=current_user)
        db.session.add(sentence)
        db.session.commit()
        return redirect(url_for('es_course_light_talk_app.es_course_light_talk_app_home'))
    return render_template('es_course/es_course_light_talk_app/add_sentence.html', title='add sentence', form=form)

#Select a sentence
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app/selecciona_frase', methods=['GET','POST'])
@login_required
def select_sentence():
    form = SelectForm()
    if form.validate_on_submit():
        objective = form.objective.data
        source = form.source.data
        #Sentence
        sentence = SentenceES.query.filter_by(author=current_user). \
            filter(SentenceES.objective == objective).\
            filter(SentenceES.source == source).\
            order_by(func.random()).first()
        if sentence is None:
            session["incorrect_sentence"]="none"
            session["correct_sentence_one"]="none"
            session["correct_sentence_two"]="none"
            session["correct_sentence_three"]="none"
            session["objective"]=objective
            session["source"]=source 
            session["message"]="No has añadido ninguna frase con ese objetivo y fuente. Por favor, añade una frase con ese objetivo y fuente para continuar."
        else:
            session["incorrect_sentence"]=sentence.incorrect_sentence 
            session["correct_sentence_one"]=sentence.correct_sentence_one
            session["correct_sentence_two"]=sentence.correct_sentence_two
            session["correct_sentence_three"]=sentence.correct_sentence_three
            session["objective"]=sentence.objective
            session["source"]=sentence.source   
            session["message"]="Hay frases añadidas con ese objetivo y fuente"         
        return redirect(url_for('es_course_light_talk_app.check_sentence'))
    return render_template('es_course/es_course_light_talk_app/select_sentence.html', title='select sentence', form=form)

#Correct sentence
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app/tu_respuesta', methods=['GET','POST'])
@login_required
def check_sentence():
    form=VerifyForm1()
    incorrect_sentence=session["incorrect_sentence"]
    correct_sentence_one=session["correct_sentence_one"]
    correct_sentence_two=session["correct_sentence_two"]
    correct_sentence_three=session["correct_sentence_three"]
    objective=session["objective"]
    source=session["source"]
    message=session["message"]
    form.incorrect_sentence.data=incorrect_sentence
    form.objective.data=objective
    form.source.data=source
    if form.validate_on_submit():
        SentenceES.query.filter_by(author=current_user). \
            filter(SentenceES.incorrect_sentence == incorrect_sentence).delete()
        db.session.commit()
        if form.your_sentence.data==correct_sentence_one or form.your_sentence.data==correct_sentence_two or form.your_sentence.data==correct_sentence_three:
            your_sentence=form.your_sentence.data
            result_string = "Correcto"
            result_num= 1
            group = 'general'
            university = 'University of Salamanca'
            year = 2024

            session["your_sentence"]=your_sentence
            session["result_string"]=result_string
            session["result_num"]=result_num

            sentence = SentenceES(incorrect_sentence=incorrect_sentence, correct_sentence_one=correct_sentence_one, correct_sentence_two=correct_sentence_two, correct_sentence_three=correct_sentence_three, correct_sentence_four="none", your_sentence=your_sentence, objective=objective, source=source, result_string=result_string, result_num=result_num,  group=group, university=university, year=year, author=current_user)
            db.session.add(sentence)
            db.session.commit()
        else:
            your_sentence=form.your_sentence.data
            result_string = "Incorrecto"
            result_num= 0
            group = 'general'
            university = 'University of Salamanca'
            year = 2024

            session["your_sentence"]=your_sentence
            session["result_string"]=result_string
            session["result_num"]=result_num

            sentence = SentenceES(incorrect_sentence=incorrect_sentence, correct_sentence_one=correct_sentence_one, correct_sentence_two=correct_sentence_two, correct_sentence_three=correct_sentence_three, correct_sentence_four="none", your_sentence=your_sentence, objective=objective, source=source, result_string=result_string, result_num=result_num,  group=group, university=university, year=year, author=current_user)
            db.session.add(sentence)
            db.session.commit()
        return redirect(url_for('es_course_light_talk_app.result_sentence'))
    return render_template('es_course/es_course_light_talk_app/your_solution.html', form=form, message=message, objective=objective, source=source)

#Correct sentence
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app/tu_resultado', methods=['GET','POST'])
@login_required
def result_sentence():
    correct_sentence_one=session["correct_sentence_one"]
    correct_sentence_two=session["correct_sentence_two"]
    correct_sentence_three=session["correct_sentence_three"]
    if correct_sentence_one != "none" and correct_sentence_two == "none" and correct_sentence_three == "none":
        form1=1
        form2=0
        form3=0
        form=VerifyForm2One() 
        form.incorrect_sentence.data=session["incorrect_sentence"]
        form.correct_sentence_one.data=session["correct_sentence_one"]
        form.your_sentence.data=session["your_sentence"]
        form.result_string.data=session["result_string"]
        form.objective.data=session["objective"]
        form.source.data=session["source"]
    elif correct_sentence_one != "none" and correct_sentence_two != "none" and correct_sentence_three == "none":
        form1=0
        form2=1
        form3=0
        form=VerifyForm2Two() 
        form.incorrect_sentence.data=session["incorrect_sentence"]
        form.correct_sentence_one.data=session["correct_sentence_one"]
        form.correct_sentence_two.data=session["correct_sentence_two"]
        form.your_sentence.data=session["your_sentence"]
        form.result_string.data=session["result_string"]
        form.objective.data=session["objective"]
        form.source.data=session["source"]
    else:
        form1=0
        form2=0
        form3=1
        form=VerifyForm2Three() 
        form.incorrect_sentence.data=session["incorrect_sentence"]
        form.correct_sentence_one.data=session["correct_sentence_one"]
        form.correct_sentence_two.data=session["correct_sentence_two"]
        form.correct_sentence_three.data=session["correct_sentence_three"]
        form.your_sentence.data=session["your_sentence"]
        form.result_string.data=session["result_string"]
        form.objective.data=session["objective"]
        form.source.data=session["source"]
    return render_template('es_course/es_course_light_talk_app/your_result.html', form=form, form1=form1, form2=form2, form3=form3)


#Select your sentences
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app/selecciona_tus_frases', methods=['GET','POST'])
@login_required
def select_your_sentences():
    form = YourSentencesForm()
    if form.validate_on_submit():
        objective = form.objective.data
        source = form.source.data
        session["objective"]=objective
        session["source"]=source
        return redirect(url_for('es_course_light_talk_app.your_sentences'))
    return render_template('es_course/es_course_light_talk_app/select_your_sentences.html', title='select your sentences', form=form)

#Select your sentences
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app/tus_frases', methods=['GET','POST'])
@login_required
def your_sentences():
    form = YourSentencesForm()
    objective=session["objective"]
    source=session["source"]
    form.objective.data=session["objective"]
    form.source.data=session["source"]
    if objective != "Todos" and source != "Todas":
        sentences = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.objective == objective).\
                filter(SentenceES.source == source).\
                order_by(SentenceES.date.desc()).all()
        incorrect = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 0).\
                filter(SentenceES.objective == objective).\
                filter(SentenceES.source == source).\
                order_by(SentenceES.date.desc()).count()
        correct = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 1).\
                filter(SentenceES.objective == objective).\
                filter(SentenceES.source == source).\
                order_by(SentenceES.date.desc()).count()
    elif objective != "Todos" and source == "Todas":
        sentences = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.objective == objective).\
                filter(SentenceES.source != source).\
                order_by(SentenceES.date.desc()).all()
        incorrect = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 0).\
                filter(SentenceES.objective == objective).\
                filter(SentenceES.source != source).\
                order_by(SentenceES.date.desc()).count()
        correct = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 1).\
                filter(SentenceES.objective == objective).\
                filter(SentenceES.source != source).\
                order_by(SentenceES.date.desc()).count()
    elif objective == "Todos" and source != "Todas":
        sentences = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.objective != objective).\
                filter(SentenceES.source == source).\
                order_by(SentenceES.date.desc()).all()
        incorrect = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 0).\
                filter(SentenceES.objective != objective).\
                filter(SentenceES.source == source).\
                order_by(SentenceES.date.desc()).count()
        correct = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 1).\
                filter(SentenceES.objective != objective).\
                filter(SentenceES.source == source).\
                order_by(SentenceES.date.desc()).count()
    else:
        sentences = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.objective != objective).\
                filter(SentenceES.source != source).\
                order_by(SentenceES.date.desc()).all()
        incorrect = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 0).\
                filter(SentenceES.objective != objective).\
                filter(SentenceES.source != source).\
                order_by(SentenceES.date.desc()).count()
        correct = SentenceES.query.filter_by(author=current_user). \
                filter(SentenceES.result_num == 1).\
                filter(SentenceES.objective != objective).\
                filter(SentenceES.source != source).\
                order_by(SentenceES.date.desc()).count()

    
    return render_template('es_course/es_course_light_talk_app/your_sentences.html', title='select your sentences', form=form, sentences=sentences, correct=correct, incorrect=incorrect)

#Delete sentence
@es_course_light_talk_app.route('/economías_del_español_curso/light_talk_app/elimina_frase/<int:sentence_id>')
def delete_sentence(sentence_id):
    sentence = SentenceES.query.get_or_404(int(sentence_id))
    db.session.delete(sentence)
    db.session.commit()
    flash("Frase eliminada", "success")
    return redirect(url_for('es_course_light_talk_app.your_sentences'))




    
  