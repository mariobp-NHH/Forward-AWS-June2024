import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt, DBVAR
from webse.models import  ModulsGD, User, ChatGD
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func, distinct, and_, or_, intersect, select
from webse.boa205_course_statistics.statistics_functions import (current_user_all_questions_time_user_first_entry_and_first_correct_per_question,
current_user_all_questions_first_entry_average, current_user_all_questions_first_and_global_correct_avg,
_format_seconds, current_user_all_questions_last_entry_correct_incorrect, attempts_vs_average_chart_time_range,
delete_entries, current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new)

boa205_course_statistics = Blueprint('boa205_course_statistics', __name__)

""" Only to test """
from webse.boa205_course_statistics.test import (time_user_first_entry_and_first_correct,first_entry_student,
    user_first_entry_and_first_correct_with_global, attempts_until_correct, all_entries,
    date_constraint_time_user_first_entry_and_first_correct,  all_questions_date_constraint_time_user_first_entry_and_first_correct)

""" Delete """
START_DATE_DELETE = datetime(2025, 9, 25)
END_DATE_DELETE = datetime(2025, 12, 31)

""" Information about the dates for each chapter """
START_DATE_TEST = datetime(2025, 1, 1)
END_DATE_TEST = datetime(2026, 12, 30)
START_CHAPTER1 = datetime(2025, 10, 1)
END_CHAPTER1 = datetime(2026, 10, 30)

""" Chapter 2a """
START_CHAPTER2a = datetime(2025, 1, 12)
END_CHAPTER2a = datetime(2026, 1, 22)

""" Chapter 2b """
START_CHAPTER2b = datetime(2026, 1, 19)
END_CHAPTER2b = datetime(2026, 1, 29)

""" Chapter 3 """
START_CHAPTER3 = datetime(2026, 1, 26)
END_CHAPTER3 = datetime(2026, 2, 5)

""" Chapter 4 """
START_CHAPTER4 = datetime(2025, 2, 2)
END_CHAPTER4 = datetime(2026, 2, 12)

""" Only to test """
@boa205_course_statistics.route('/boa205_course/statistics_test_web', methods=['GET', 'POST'])
@login_required
def statistics_test_web():

    question_number_test=2
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=datetime(2025, 10, 14)
    end_date_test=datetime(2025, 10, 25)

    """ *FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    time_user_first_entry_and_first_correct_call=time_user_first_entry_and_first_correct(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            question_num=question_number_test
        )
    
    """ *FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
    first_entry_student_call=first_entry_student(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            question_num=question_number_test
        )
    
    """ *FIRST ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER: Query to work out the date of the first entry per student, the average of the date of the first entry """
    user_first_entry_and_first_correct_with_global_call=user_first_entry_and_first_correct_with_global(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            question_num=question_number_test
        )
    
    """ *ATTEMPTS: ATTEMPTS UNTIL CORRECT. Number of attempts until correct, and average number of attempts """
    attempts_until_correct_call=attempts_until_correct(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            question_num=question_number_test
        )
    
    """ *ALL THE ENTRIES: Query to work out all the entries per student """
    (all_entries_call_results,all_entries_call_answers) =all_entries(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            question_num=question_number_test
        )

    """ *DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    date_constraint_time_user_first_entry_and_first_correct_call=date_constraint_time_user_first_entry_and_first_correct(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            question_num=question_number_test,
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    """ *ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    all_questions_date_constraint_time_user_first_entry_and_first_correct_call=all_questions_date_constraint_time_user_first_entry_and_first_correct(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
   

    return render_template('boa205_course/statistics/statistics_test_web.html', 
                           title_mo_test=title_mo_test, title_ch_test=title_ch_test, question_number_test=question_number_test,
                           first_entry_student_call=first_entry_student_call,
                           all_entries_call_results=all_entries_call_results, all_entries_call_answers=all_entries_call_answers,
                           user_first_entry_and_first_correct_with_global_call=user_first_entry_and_first_correct_with_global_call,
                           time_user_first_entry_and_first_correct_call=time_user_first_entry_and_first_correct_call,
                           attempts_until_correct_call=attempts_until_correct_call,
                           date_constraint_time_user_first_entry_and_first_correct_call=date_constraint_time_user_first_entry_and_first_correct_call,
                           all_questions_date_constraint_time_user_first_entry_and_first_correct_call=all_questions_date_constraint_time_user_first_entry_and_first_correct_call)

@boa205_course_statistics.route('/boa205_course/delete_entries_web')
@login_required
def delete_entries_web():
    title_mo_delete = 'boa205_ch2b'
    title_ch_delete = 'Kapitel 2b. Hva er normalkostregnskap?'
    start_date_delete = START_DATE_DELETE
    end_date_delete = END_DATE_DELETE

    # Direct delete query
    ModulsGD.query.filter(
        ModulsGD.title_mo == title_mo_delete,
        ModulsGD.title_ch == title_ch_delete,
        ModulsGD.date_exercise >= start_date_delete,
        ModulsGD.date_exercise <= end_date_delete
    ).delete(synchronize_session=False)

    db.session.commit()
    return render_template('boa205_course/statistics/delete.html')


###############################
####   Block  Statistics   ####
###############################

@boa205_course_statistics.route('/boa205_course/statistics', methods=['GET', 'POST'])
@login_required
def statistics():
    return render_template('boa205_course/statistics/statistics.html')

@boa205_course_statistics.route('/boa205_course/statistics/ch1', methods=['GET', 'POST'])
@login_required
def statistics_ch1():
    return render_template('boa205_course/statistics/statistics_ch1.html')

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY """
@boa205_course_statistics.route('/boa205_course/statistics/ch1/first_entry_time_week', methods=['GET', 'POST'])
@login_required
def statistics_ch1_first_entry_time_week():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_CHAPTER1
    end_date_test=END_CHAPTER1

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch1/first_entry_time_year', methods=['GET', 'POST'])
@login_required
def statistics_ch1_first_entry_time_year():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
@boa205_course_statistics.route('/boa205_course/statistics/ch1/first_entry_average_week', methods=['GET', 'POST'])
@login_required
def statistics_ch1_first_entry_average_week():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_CHAPTER1
    end_date_test=END_CHAPTER1

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch1/first_entry_average_year', methods=['GET', 'POST'])
@login_required
def statistics_ch1_first_entry_average_year():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST CORRECT ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER """
@boa205_course_statistics.route('/boa205_course/statistics/ch1/first_answer_week', methods=['GET', 'POST'])
@login_required
def statistics_ch1_first_answer_week():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_CHAPTER1
    end_date_test=END_CHAPTER1

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch1/first_answer_year', methods=['GET', 'POST'])
@login_required
def statistics_ch1_first_answer_year():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. ATTEMPTS UNTIL CORRECT. """
@boa205_course_statistics.route('/boa205_course/statistics/ch1/attempts_week', methods=['GET', 'POST'])
@login_required
def statistics_ch1_attempts_week():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_CHAPTER1
    end_date_test=END_CHAPTER1

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch1/attempts_year', methods=['GET', 'POST'])
@login_required
def statistics_ch1_attempts_year():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. LAST ENTRY"""
@boa205_course_statistics.route('/boa205_course/statistics/ch1/last_entry_week', methods=['GET', 'POST'])
@login_required
def statistics_ch1_last_entry_week():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_CHAPTER1
    end_date_test=END_CHAPTER1

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch1/last_entry_year', methods=['GET', 'POST'])
@login_required
def statistics_ch1_last_entry_year():
    title_mo_test='boa205_ch1'
    title_ch_test='Kapitel 1. Hva er et driftsregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch1',
            title_ch='Kapitel 1. Hva er et driftsregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/statistics_ch1_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

""" Chapter 2a """
@boa205_course_statistics.route('/boa205_course/statistics/ch2a', methods=['GET', 'POST'])
@login_required
def statistics_ch2a():
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a.html')

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY """
@boa205_course_statistics.route('/boa205_course/statistics/ch2a/first_entry_time_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_first_entry_time_week():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2a
    end_date_test=END_CHAPTER2a

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch2a/first_entry_time_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_first_entry_time_year():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
@boa205_course_statistics.route('/boa205_course/statistics/ch2a/first_entry_average_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_first_entry_average_week():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2a
    end_date_test=END_CHAPTER2a

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch2a/first_entry_average_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_first_entry_average_year():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST CORRECT ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER """
@boa205_course_statistics.route('/boa205_course/statistics/ch2a/first_answer_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_first_answer_week():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2a
    end_date_test=END_CHAPTER2a

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch2a/first_answer_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_first_answer_year():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. ATTEMPTS UNTIL CORRECT. """
@boa205_course_statistics.route('/boa205_course/statistics/ch2a/attempts_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_attempts_week():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2a
    end_date_test=END_CHAPTER2a

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch2a/attempts_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_attempts_year():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. LAST ENTRY"""
@boa205_course_statistics.route('/boa205_course/statistics/ch2a/last_entry_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_last_entry_week():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2a
    end_date_test=END_CHAPTER2a

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch2a/last_entry_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2a_last_entry_year():
    title_mo_test='boa205_ch2'
    title_ch_test='Kapitel 2. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch2',
            title_ch='Kapitel 2. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2a/statistics_ch2a_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

""" Chapter 2b """
@boa205_course_statistics.route('/boa205_course/statistics/ch2b', methods=['GET', 'POST'])
@login_required
def statistics_ch2b():
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b.html')

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY """
@boa205_course_statistics.route('/boa205_course/statistics/ch2b/first_entry_time_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_first_entry_time_week():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2b
    end_date_test=END_CHAPTER2b

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch2b/first_entry_time_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_first_entry_time_year():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
@boa205_course_statistics.route('/boa205_course/statistics/ch2b/first_entry_average_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_first_entry_average_week():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2b
    end_date_test=END_CHAPTER2b

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch2b/first_entry_average_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_first_entry_average_year():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST CORRECT ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER """
@boa205_course_statistics.route('/boa205_course/statistics/ch2b/first_answer_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_first_answer_week():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2b
    end_date_test=END_CHAPTER2b

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch2b/first_answer_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_first_answer_year():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. ATTEMPTS UNTIL CORRECT. """
@boa205_course_statistics.route('/boa205_course/statistics/ch2b/attempts_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_attempts_week():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2b
    end_date_test=END_CHAPTER2b

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch2b/attempts_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_attempts_year():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. LAST ENTRY"""
@boa205_course_statistics.route('/boa205_course/statistics/ch2b/last_entry_week', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_last_entry_week():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_CHAPTER2b
    end_date_test=END_CHAPTER2b

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch2b/last_entry_year', methods=['GET', 'POST'])
@login_required
def statistics_ch2b_last_entry_year():
    title_mo_test='boa205_ch2b'
    title_ch_test='Kapitel 2b. Hva er normalkostregnskap?'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch2b',
            title_ch='Kapitel 2b. Hva er normalkostregnskap?',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch2b/statistics_ch2b_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

""" Chapter 3 """
@boa205_course_statistics.route('/boa205_course/statistics/ch3', methods=['GET', 'POST'])
@login_required
def statistics_ch3():
    return render_template('boa205_course/statistics/ch3/statistics_ch3.html')

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY """
@boa205_course_statistics.route('/boa205_course/statistics/ch3/first_entry_time_week', methods=['GET', 'POST'])
@login_required
def statistics_ch3_first_entry_time_week():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_CHAPTER3
    end_date_test=END_CHAPTER3

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch3/first_entry_time_year', methods=['GET', 'POST'])
@login_required
def statistics_ch3_first_entry_time_year():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
@boa205_course_statistics.route('/boa205_course/statistics/ch3/first_entry_average_week', methods=['GET', 'POST'])
@login_required
def statistics_ch3_first_entry_average_week():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_CHAPTER3
    end_date_test=END_CHAPTER3

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch3/first_entry_average_year', methods=['GET', 'POST'])
@login_required
def statistics_ch3_first_entry_average_year():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST CORRECT ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER """
@boa205_course_statistics.route('/boa205_course/statistics/ch3/first_answer_week', methods=['GET', 'POST'])
@login_required
def statistics_ch3_first_answer_week():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_CHAPTER3
    end_date_test=END_CHAPTER3

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch3/first_answer_year', methods=['GET', 'POST'])
@login_required
def statistics_ch3_first_answer_year():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. ATTEMPTS UNTIL CORRECT. """
@boa205_course_statistics.route('/boa205_course/statistics/ch3/attempts_week', methods=['GET', 'POST'])
@login_required
def statistics_ch3_attempts_week():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_CHAPTER3
    end_date_test=END_CHAPTER3

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch3/attempts_year', methods=['GET', 'POST'])
@login_required
def statistics_ch3_attempts_year():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. LAST ENTRY"""
@boa205_course_statistics.route('/boa205_course/statistics/ch3/last_entry_week', methods=['GET', 'POST'])
@login_required
def statistics_ch3_last_entry_week():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_CHAPTER3
    end_date_test=END_CHAPTER3

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch3/last_entry_year', methods=['GET', 'POST'])
@login_required
def statistics_ch3_last_entry_year():
    title_mo_test='boa205_ch3'
    title_ch_test='Kapitel 3. Standardkost'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch3',
            title_ch='Kapitel 3. Standardkost',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch3/statistics_ch3_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

""" Chapter 4 """
@boa205_course_statistics.route('/boa205_course/statistics/ch4', methods=['GET', 'POST'])
@login_required
def statistics_ch4():
    return render_template('boa205_course/statistics/ch4/statistics_ch4.html')

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY """
@boa205_course_statistics.route('/boa205_course/statistics/ch4/first_entry_time_week', methods=['GET', 'POST'])
@login_required
def statistics_ch4_first_entry_time_week():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_CHAPTER4
    end_date_test=END_CHAPTER4

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch4/first_entry_time_year', methods=['GET', 'POST'])
@login_required
def statistics_ch4_first_entry_time_year():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    """ *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
    current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call, correct, incorrect=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_first_entry_time.html', 
                           current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call=current_user_all_questions_time_user_first_entry_and_first_correct_per_question_call,
                           correct=correct, incorrect=incorrect)

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
@boa205_course_statistics.route('/boa205_course/statistics/ch4/first_entry_average_week', methods=['GET', 'POST'])
@login_required
def statistics_ch4_first_entry_average_week():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_CHAPTER4
    end_date_test=END_CHAPTER4

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch4/first_entry_average_year', methods=['GET', 'POST'])
@login_required
def statistics_ch4_first_entry_average_year():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_entry_average(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_first_entry_average.html', 
                           current_user_all_questions_first_entry_average_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST CORRECT ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER """
@boa205_course_statistics.route('/boa205_course/statistics/ch4/first_answer_week', methods=['GET', 'POST'])
@login_required
def statistics_ch4_first_answer_week():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_CHAPTER4
    end_date_test=END_CHAPTER4

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch4/first_answer_year', methods=['GET', 'POST'])
@login_required
def statistics_ch4_first_answer_year():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    table_data, chart_data=current_user_all_questions_first_and_global_correct_avg(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_first_answer.html', 
                           current_user_all_questions_first_and_global_correct_avg_call=table_data,
        chart_labels=chart_data["labels"],
        chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. ATTEMPTS UNTIL CORRECT. """
@boa205_course_statistics.route('/boa205_course/statistics/ch4/attempts_week', methods=['GET', 'POST'])
@login_required
def statistics_ch4_attempts_week():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_CHAPTER4
    end_date_test=END_CHAPTER4

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

@boa205_course_statistics.route('/boa205_course/statistics/ch4/attempts_year', methods=['GET', 'POST'])
@login_required
def statistics_ch4_attempts_year():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    attempts_vs_average_chart_time_range_call, chart_data=attempts_vs_average_chart_time_range(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_attempts.html', 
            attempts_vs_average_chart_time_range_call=attempts_vs_average_chart_time_range_call,
            chart_labels=chart_data["labels"],
            chart_values=chart_data["values"])

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. LAST ENTRY"""
@boa205_course_statistics.route('/boa205_course/statistics/ch4/last_entry_week', methods=['GET', 'POST'])
@login_required
def statistics_ch4_last_entry_week():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_CHAPTER4
    end_date_test=END_CHAPTER4

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

@boa205_course_statistics.route('/boa205_course/statistics/ch4/last_entry_year', methods=['GET', 'POST'])
@login_required
def statistics_ch4_last_entry_year():
    title_mo_test='boa205_ch4'
    title_ch_test='Kapitel 4. Salgets resultatavvik'
    start_date_test=START_DATE_TEST
    end_date_test=END_DATE_TEST

    current_user_all_questions_last_entry_correct_incorrect_call, correct, incorrect, chart=current_user_all_questions_last_entry_correct_incorrect(
            title_mo='boa205_ch4',
            title_ch='Kapitel 4. Salgets resultatavvik',
            start_date=start_date_test,
            end_date=end_date_test
        )
    
    return render_template('boa205_course/statistics/ch4/statistics_ch4_last_entry.html', 
            current_user_all_questions_last_entry_correct_incorrect_call=current_user_all_questions_last_entry_correct_incorrect_call,
            correct=correct, incorrect=incorrect)

