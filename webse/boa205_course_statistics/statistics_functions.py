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


""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
def current_user_all_questions_time_user_first_entry_and_first_correct_per_question(title_mo, title_ch, start_date, end_date):
    """
    Returns a list of dictionaries for the current logged-in user with:
    - username
    - user_id
    - question_num
    - question_result
    - date of the first entry per question
    - date of the first correct entry per question (global per question_num, formatted without milliseconds)
    - time difference between user's first entry and the first correct entry (if correct)

    Only entries within the date range are considered.
    """

    # Step 1: first entry per question for the current user
    first_entry_subq = (
        db.session.query(
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .group_by(ModulsGD.question_num)
        .subquery()
    )

    # Step 2: join to get full details for those first entries
    first_entries_query = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            ModulsGD.question_result,
            first_entry_subq.c.first_date
        )
        .join(
            first_entry_subq,
            and_(
                ModulsGD.question_num == first_entry_subq.c.question_num,
                ModulsGD.date_exercise == first_entry_subq.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .order_by(ModulsGD.question_num)
    )

    first_entries = first_entries_query.all()

    # Step 3: find the first correct entry per question (global, across all users)
    first_correct_by_question = {}
    global_corrects = (
        db.session.query(
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_correct_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_result == 1)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .group_by(ModulsGD.question_num)
        .all()
    )

    for row in global_corrects:
        first_correct_by_question[row.question_num] = row.first_correct_date

    # Step 4: build dictionary and compute time difference for the current user
    data = []
    correct = 0
    incorrect = 0
    for r in first_entries:
        username = getattr(current_user, "username", "Unknown")
        first_correct_date = first_correct_by_question.get(r.question_num)

        # Format date without milliseconds (if not None)
        formatted_correct_date = (
            first_correct_date.strftime("%Y-%m-%d %H:%M:%S")
            if first_correct_date else None
        )

        # Count correct/incorrect
        if r.question_result == 1:
            correct += 1
        else:
            incorrect += 1

        # Compute time difference only if the user's first entry is correct
        if r.question_result == 1 and first_correct_date:
            diff = r.first_date - first_correct_date
            total_seconds = int(diff.total_seconds())
            days, remainder = divmod(total_seconds, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            if days > 0:
                diff_hms = f"{days}d {hours:02}:{minutes:02}:{seconds:02}"
            else:
                diff_hms = f"{hours:02}:{minutes:02}:{seconds:02}"
        else:
            diff_hms = None

        data.append({
            "username": username,
            "user_id": r.user_id,
            "question_num": r.question_num,
            "question_result": r.question_result,
            "Date First Entry": r.first_date,
            "First Correct Entry (This Question)": formatted_correct_date,  # ✅ formatted version
            "Time Difference vs First Correct": diff_hms
        })

    return data, correct, incorrect

def current_user_all_questions_time_user_first_entry_and_first_correct_per_question_new(title_mo, title_ch, start_date, end_date):
    """
    Returns a list of dictionaries for the current logged-in user with:
    - username
    - user_id
    - question_num
    - question_result (of user's first attempt)
    - date of the user's first entry per question
    - date of the first global correct entry that was correct in the first attempt
    - time difference between user's first correct (if correct in first attempt) 
      and global first correct (first attempt), but set to zero if user's correct came first.

    Only considers answers within the date range.
    """

    # Step 1: get first entry per question for the current user
    first_entry_subq = (
        db.session.query(
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .group_by(ModulsGD.question_num)
        .subquery()
    )

    # Step 2: join to get current user's first entries
    first_entries_query = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            ModulsGD.question_result,
            first_entry_subq.c.first_date
        )
        .join(
            first_entry_subq,
            and_(
                ModulsGD.question_num == first_entry_subq.c.question_num,
                ModulsGD.date_exercise == first_entry_subq.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .order_by(ModulsGD.question_num)
    )

    first_entries = first_entries_query.all()

    # Step 3: find the first globally correct entry per question,
    #         but only if that correct entry was in the first attempt for that user.
    first_attempt_subq = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_attempt_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .group_by(ModulsGD.user_id, ModulsGD.question_num)
        .subquery()
    )

    first_attempt_corrects = (
        db.session.query(
            ModulsGD.question_num,
            first_attempt_subq.c.first_attempt_date.label("date_exercise")
        )
        .join(
            first_attempt_subq,
            and_(
                ModulsGD.user_id == first_attempt_subq.c.user_id,
                ModulsGD.question_num == first_attempt_subq.c.question_num,
                ModulsGD.date_exercise == first_attempt_subq.c.first_attempt_date
            )
        )
        .filter(ModulsGD.question_result == 1)
        .all()
    )

    first_correct_by_question = {}
    for row in first_attempt_corrects:
        qn = row.question_num
        if qn not in first_correct_by_question or row.date_exercise < first_correct_by_question[qn]:
            first_correct_by_question[qn] = row.date_exercise

    # Step 4: build dictionary and compute time difference for current user
    data = []
    correct = 0
    incorrect = 0
    for r in first_entries:
        username = getattr(current_user, "username", "Unknown")
        first_correct_date = first_correct_by_question.get(r.question_num)

        formatted_correct_date = (
            first_correct_date.strftime("%Y-%m-%d %H:%M:%S")
            if first_correct_date else None
        )

        if r.question_result == 1:
            correct += 1
        else:
            incorrect += 1

        # Compute time difference only if user got it correct in first attempt
        if r.question_result == 1 and first_correct_date:
            if r.first_date <= first_correct_date:
                # User answered correctly before the global first-correct (first attempt)
                diff_hms = "00:00:00"
            else:
                diff = r.first_date - first_correct_date
                total_seconds = int(diff.total_seconds())
                days, remainder = divmod(total_seconds, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)
                if days > 0:
                    diff_hms = f"{days}d {hours:02}:{minutes:02}:{seconds:02}"
                else:
                    diff_hms = f"{hours:02}:{minutes:02}:{seconds:02}"
        else:
            diff_hms = None

        data.append({
            "username": username,
            "user_id": r.user_id,
            "question_num": r.question_num,
            "question_result": r.question_result,
            "Date First Entry": r.first_date,
            "First Correct Entry (First Attempt Global)": formatted_correct_date,
            "Time Difference vs First Correct (First Attempt)": diff_hms
        })

    return data, correct, incorrect


""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
def current_user_all_questions_first_entry_average(title_mo, title_ch, start_date, end_date):
    """
    Returns:
    - data: list of dicts for Jinja table
    - chart_data: dict with labels (Q1, Q2, ...) and averages for Chart.js
    """

    # Step 1: subquery – first entry per question for each user
    subquery = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise.between(start_date, end_date))
        .group_by(ModulsGD.user_id, ModulsGD.question_num)
        .subquery()
    )

    # Step 2: get current user's first entries
    user_entries = (
        db.session.query(ModulsGD)
        .join(
            subquery,
            and_(
                ModulsGD.user_id == subquery.c.user_id,
                ModulsGD.question_num == subquery.c.question_num,
                ModulsGD.date_exercise == subquery.c.first_date
            )
        )
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise.between(start_date, end_date))
        .order_by(ModulsGD.question_num)
        .all()
    )

    # Step 3: compute mean per question (for all users)
    mean_per_question = dict(
        db.session.query(
            ModulsGD.question_num,
            func.avg(ModulsGD.question_result)
        )
        .join(
            subquery,
            and_(
                ModulsGD.user_id == subquery.c.user_id,
                ModulsGD.question_num == subquery.c.question_num,
                ModulsGD.date_exercise == subquery.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise.between(start_date, end_date))
        .group_by(ModulsGD.question_num)
        .all()
    )

    # Step 4: prepare table data
    data = []
    for entry in user_entries:
        data.append({
            "username": current_user.username,
            "question_num": entry.question_num,
            "question_result": entry.question_result,
            "mean_per_question": round(mean_per_question.get(entry.question_num, 0), 2)
        })

    # Step 5: prepare Chart.js data
    chart_labels = [f"Q{q}" for q in sorted(mean_per_question.keys())]
    chart_values = [round(v, 2) for _, v in sorted(mean_per_question.items())]

    chart_data = {
        "labels": chart_labels,
        "values": chart_values
    }

    return data, chart_data

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. FIRST CORRECT ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER: Query to work out the date of the first entry per student, the average of the date of the first entry """
def current_user_all_questions_first_and_global_correct_avg(title_mo, title_ch, start_date, end_date):
    """
    Returns:
      - detailed data list (for table)
      - chart_data dict: {"labels": [...question_nums...], "values": [...avg_diff_seconds...]}
    """

    # --- Step 1: first entry per question for the current user ---
    first_entry_subq = (
        db.session.query(
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise.between(start_date, end_date))
        .group_by(ModulsGD.question_num)
        .subquery()
    )

    # --- Step 2: first correct per question for all users ---
    all_users_first_correct = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_correct_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_result == 1)
        .filter(ModulsGD.date_exercise.between(start_date, end_date))
        .group_by(ModulsGD.user_id, ModulsGD.question_num)
        .subquery()
    )

    # --- Step 3: global first correct per question ---
    global_first_correct = dict(
        db.session.query(
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("global_first_correct_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_result == 1)
        .filter(ModulsGD.date_exercise.between(start_date, end_date))
        .group_by(ModulsGD.question_num)
        .all()
    )

    # --- Step 4: compute average time differences per question ---
    avg_diff_per_question = {}
    avg_diff_seconds = {}   # also store numeric seconds for Chart.js
    for q_num, global_date in global_first_correct.items():
        if not global_date:
            continue

        # remove microseconds from the global date
        global_date = global_date.replace(microsecond=0)

        user_diffs = []
        first_corrects = (
            db.session.query(all_users_first_correct.c.first_correct_date)
            .filter(all_users_first_correct.c.question_num == q_num)
            .all()
        )

        for (user_date,) in first_corrects:
            if user_date:
                user_date = user_date.replace(microsecond=0)
                diff_seconds = (user_date - global_date).total_seconds()
                if diff_seconds >= 0:
                    user_diffs.append(diff_seconds)

        if user_diffs:
            avg_seconds = sum(user_diffs) / len(user_diffs)
            avg_diff_per_question[q_num] = str(_format_seconds(avg_seconds))
            avg_diff_seconds[q_num] = avg_seconds
        else:
            avg_diff_per_question[q_num] = None
            avg_diff_seconds[q_num] = 0

        # update back into dictionary to keep the truncated version
        global_first_correct[q_num] = global_date

    # --- Step 5: join data for current user ---
    query = (
        db.session.query(
            ModulsGD.question_num,
            ModulsGD.question_result,
            first_entry_subq.c.first_date,
            all_users_first_correct.c.first_correct_date
        )
        .join(
            first_entry_subq,
            and_(
                ModulsGD.question_num == first_entry_subq.c.question_num,
                ModulsGD.date_exercise == first_entry_subq.c.first_date
            )
        )
        .outerjoin(
            all_users_first_correct,
            and_(
                ModulsGD.user_id == all_users_first_correct.c.user_id,
                ModulsGD.question_num == all_users_first_correct.c.question_num
            )
        )
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise.between(start_date, end_date))
        .order_by(ModulsGD.question_num)
        .all()
    )

    # --- Step 6: compute diffs for current user ---
    data = []
    for r in query:
        q_num = r.question_num
        global_correct_date = global_first_correct.get(q_num)
        avg_diff_hms = avg_diff_per_question.get(q_num)

        if r.first_correct_date and global_correct_date:
            first_correct_date = r.first_correct_date.replace(microsecond=0)
            diff = first_correct_date - global_correct_date
            total_seconds = int(diff.total_seconds())
            diff_hms = _format_seconds(total_seconds)
        else:
            first_correct_date = None
            diff_hms = None

        data.append({
            "username": current_user.username,
            "question_num": q_num,
            "question_result": r.question_result,
            "Date First Entry": r.first_date.replace(microsecond=0) if r.first_date else None,
            "Date First Correct Answer": first_correct_date,
            "Global First Correct Date": global_correct_date,
            "Time Difference vs Global First Correct": diff_hms,
            "Average Time Difference (All Users)": avg_diff_hms
        })

    # --- Step 7: prepare chart data ---
    chart_data = {
        "labels": sorted(avg_diff_seconds.keys()),
        "values": [avg_diff_seconds[q] / 60 for q in sorted(avg_diff_seconds.keys())]  # convert to minutes
    }

    return data, chart_data

def _format_seconds(total_seconds):
    """Convert seconds into a 'Xd HH:MM:SS' string."""
    days, remainder = divmod(int(total_seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    if days > 0:
        return f"{days}d {hours:02}:{minutes:02}:{seconds:02}"
    else:
        return f"{hours:02}:{minutes:02}:{seconds:02}"

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. LAST ENTRY: Correct and incorrect answers """
def current_user_all_questions_last_entry_correct_incorrect(title_mo, title_ch, start_date, end_date):
    """
    Returns for the current_user:
      - the last entry per question within the date range
      - whether each last entry is correct or incorrect
      - totals of correct and incorrect answers
      - suitable for Chart.js plotting
    """

    # Step 1: last entry per question for the current user
    last_entry_subq = (
        db.session.query(
            ModulsGD.question_num,
            func.max(ModulsGD.date_exercise).label("last_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.user_id == current_user.id)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .group_by(ModulsGD.question_num)
        .subquery()
    )

    # Step 2: join to get full details for those last entries
    last_entries_query = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            ModulsGD.question_result,
            last_entry_subq.c.last_date
        )
        .join(
            last_entry_subq,
            and_(
                ModulsGD.question_num == last_entry_subq.c.question_num,
                ModulsGD.date_exercise == last_entry_subq.c.last_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.user_id == current_user.id)
        .order_by(ModulsGD.question_num)
    )

    last_entries = last_entries_query.all()

    # Step 3: count correct/incorrect
    correct = sum(1 for r in last_entries if r.question_result == 1)
    incorrect = sum(1 for r in last_entries if r.question_result != 1)

    # Step 4: build dictionary list for table display
    data = []
    username = getattr(current_user, "username", "Unknown")
    for r in last_entries:
        data.append({
            "username": username,
            "user_id": r.user_id,
            "question_num": r.question_num,
            "question_result": r.question_result,
            "Date Last Entry": r.last_date,
        })

    # Step 5: prepare Chart.js data
    chart_data = {
        "labels": ["Riktig", "Feil"],
        "values": [correct, incorrect],
    }

    return data, correct, incorrect, chart_data

""" *CURRENT USER. ALL QUESTIONS. DATE CONSTRAINT. ATTEMPTS UNTIL CORRECT. """
def attempts_vs_average_chart_time_range(title_mo, title_ch, start_date, end_date):
    """
    Returns:
    - A list of dictionaries for Jinja display:
        - question_num
        - Attempts Current User
        - Average Attempts (All Users)
    - Chart.js data:
        - labels: ["Q1", "Q2", ...]
        - values: [average_attempts_for_Q1, average_attempts_for_Q2, ...]
    Only considers answers within the date range [start_date, end_date].
    """

    from collections import defaultdict
    from sqlalchemy import and_

    # Step 1: Retrieve all answers within date range
    answers = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            ModulsGD.question_result,
            ModulsGD.date_exercise
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .order_by(ModulsGD.user_id, ModulsGD.question_num, ModulsGD.date_exercise.asc())
        .all()
    )

    # ✅ Return consistent structure when no data found
    if not answers:
        print("No answers found in the given date range.")
        return [], {"labels": [], "values": []}

    # Step 2: Group results by user and question
    user_question_results = defaultdict(lambda: defaultdict(list))
    for ans in answers:
        user_question_results[ans.user_id][ans.question_num].append(ans.question_result)

    # Step 3: Compute attempts until correct for all users
    question_attempts_all_users = defaultdict(list)
    for user_id, questions in user_question_results.items():
        for q_num, results in questions.items():
            attempts = 0
            found_correct = False
            for r in results:
                attempts += 1
                if r == 1:
                    found_correct = True
                    break
            if found_correct:
                question_attempts_all_users[q_num].append(attempts)

    # Step 4: Compute attempts until correct for current user and prepare Chart.js data
    data = []
    labels = []
    chart_data = []

    current_user_questions = user_question_results.get(current_user.id, {})
    all_question_nums = sorted(question_attempts_all_users.keys())

    for q_num in all_question_nums:
        # Current user attempts
        results = current_user_questions.get(q_num, [])
        attempts_user = None
        attempts_count = 0
        for r in results:
            attempts_count += 1
            if r == 1:
                attempts_user = attempts_count
                break

        # Average attempts across all users
        attempts_list = question_attempts_all_users[q_num]
        avg_attempts = round(sum(attempts_list) / len(attempts_list), 2) if attempts_list else None

        data.append({
            "question_num": q_num,
            "Attempts Current User": attempts_user,
            "Average Attempts (All Users)": avg_attempts
        })

        # Chart.js info
        labels.append(f"Q{q_num}")
        chart_data.append(avg_attempts)

    chart_js_data = {
        "labels": labels,
        "values": chart_data
    }

    return data, chart_js_data

""" Delete entries all users, for the variables specified in the inputs """
def delete_entries(title_mo, title_ch, start_date, end_date):
    # Step 1: Retrieve all answers within date range
    entries = ModulsGD.query\
        .filter(ModulsGD.title_mo == title_mo)\
        .filter(ModulsGD.title_ch == title_ch)\
        .filter(ModulsGD.date_exercise >= start_date)\
        .filter(ModulsGD.date_exercise <= end_date)\
        .order_by(ModulsGD.user_id, ModulsGD.question_num, ModulsGD.date_exercise.asc())\
        .all()
    return entries


