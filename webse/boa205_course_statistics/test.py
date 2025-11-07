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


""" Functions that can be useful, but that I have not used in this chatper """
""" Function to delete all the entries except the first and the last one """
def keep_first_and_last(author, title_mo, title_ch, question_num):
    answers = (
        ModulsGD.query
        .filter_by(author=author)
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.date_exercise.asc())
        .all()
    )

    if len(answers) <= 2:
        return  # nothing to delete

    first_id = answers[0].id
    last_id = answers[-1].id

    (
        ModulsGD.query
        .filter_by(author=author)
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .filter(ModulsGD.id.notin_([first_id, last_id]))
        .delete(synchronize_session=False)
    )

    db.session.commit()

""" Q1: First result in the first attemp """
def result_first_attemp(author, title_mo, title_ch, question_num):
    result = (
        ModulsGD.query
        .filter_by(author=author)
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.date_exercise.asc())
        .first()
    )
    if result is None:
        return None  # or you could return 0, "No result", etc.
    
    return result.question_result

""" Q3: Number of attemps until get a correct answer (1) """
def count_zeros_until_one(results):
    count = 0
    for r in results:
        if r == 1:
            break
        count += 1
    return count

""" Q4: Result in the last attemp """
def result_last_attemp(author, title_mo, title_ch, question_num):
    result = (
        ModulsGD.query
        .filter_by(author=author)
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.date_exercise.desc())
        .first()
    )
    if result is None:
        return None  # or you could return 0, "No result", etc.
    
    return result.question_result

""" This other functions are in line with the ones that I am using in the chapter, but that I have not used """
""" *FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
def time_user_first_entry_and_first_correct(title_mo, title_ch, question_num):
    """
    Returns a list of dictionaries with:
    - username
    - user_id
    - question_num
    - question_result
    - date of the first entry per user
    - date of the first correct among first entries
    - time difference between user's first entry and first correct answer (if correct)
    """

    # Step 1: first entry per user
    first_entry_subq = (
        db.session.query(
            ModulsGD.user_id,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .group_by(ModulsGD.user_id)
        .subquery()
    )

    # Step 2: join ModulsGD with the subquery to get details of the first entries
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
                ModulsGD.user_id == first_entry_subq.c.user_id,
                ModulsGD.date_exercise == first_entry_subq.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.user_id)
    )

    first_entries = first_entries_query.all()

    # Step 3: among those first entries, find the first correct one (if any)
    first_correct_date = None
    for r in first_entries:
        if r.question_result == 1:
            if first_correct_date is None or r.first_date < first_correct_date:
                first_correct_date = r.first_date

    # Step 4: build dictionary and compute time difference
    data = []
    for r in first_entries:
        user = db.session.query(User).filter(User.id == r.user_id).first()
        username = user.username if user else "Unknown"

        # Compute time difference only when the answer is correct
        if r.question_result == 1 and first_correct_date:
            diff = r.first_date - first_correct_date

            # Remove microseconds (no milliseconds)
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
            "First Correct Among First Entries": first_correct_date,
            "Time Difference Your Answer and First Correct Answer": diff_hms
        })

    return data

""" *ALL QUESTIONS. DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
def all_questions_date_constraint_time_user_first_entry_and_first_correct(title_mo, title_ch, start_date, end_date):
    """
    Returns a list of dictionaries with:
    - username
    - user_id
    - question_num
    - question_result
    - date of the first entry per user per question
    - date of the first correct entry per question (global per question_num)
    - time difference between user's first entry and the first correct (if correct)

    Only entries within the date range are considered.
    """

    # Step 1: first entry per user per question
    first_entry_subq = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .group_by(ModulsGD.user_id, ModulsGD.question_num)
        .subquery()
    )

    # Step 2: join ModulsGD with the subquery to get details of the first entries
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
                ModulsGD.user_id == first_entry_subq.c.user_id,
                ModulsGD.question_num == first_entry_subq.c.question_num,
                ModulsGD.date_exercise == first_entry_subq.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .order_by(ModulsGD.question_num, ModulsGD.user_id)
    )

    first_entries = first_entries_query.all()

    # Step 3: find the first correct entry date per question_num
    first_correct_by_question = {}
    for r in first_entries:
        if r.question_result == 1:
            qnum = r.question_num
            if qnum not in first_correct_by_question or r.first_date < first_correct_by_question[qnum]:
                first_correct_by_question[qnum] = r.first_date

    # Step 4: build the data with per-question first correct and time differences
    data = []
    for r in first_entries:
        user = db.session.query(User).filter(User.id == r.user_id).first()
        username = user.username if user else "Unknown"

        # Retrieve the first correct date for that question
        first_correct_date = first_correct_by_question.get(r.question_num)

        # Step 5: compute the time difference only if the user’s first entry is correct
        if r.question_result == 1 and first_correct_date:
            diff = r.first_date - first_correct_date

            # Convert to days, hours, minutes, seconds (no milliseconds)
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
            "First Correct Entry (This Question)": first_correct_date,
            "Time Difference vs First Correct": diff_hms
        })

    return data

""" *FIRST ENTRY: FIRST ENTRY PER STUDENT AND AVERAGE FIRST ENTRIES. """
def first_entry_student(title_mo, title_ch, question_num):
    """Return the first entry per student and the mean question_result per user."""

    # Step 1: subquery – find the earliest date per user
    subquery = (
        db.session.query(
            ModulsGD.user_id,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .group_by(ModulsGD.user_id)
        .subquery()
    )

    # Step 2: join to get each user's first entry
    first_entries = (
        db.session.query(ModulsGD)
        .join(
            subquery,
            and_(
                ModulsGD.user_id == subquery.c.user_id,
                ModulsGD.date_exercise == subquery.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.user_id)
        .all()
    )

    # Step 3: compute the average of all first entries
    mean_first_entry = (
        db.session.query(func.avg(ModulsGD.question_result))
        .join(
            subquery,
            and_(
                ModulsGD.user_id == subquery.c.user_id,
                ModulsGD.date_exercise == subquery.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .scalar()
    )

    mean_first_entry = float(mean_first_entry) if mean_first_entry is not None else 0.0

    # Create a dictionary with all data
    result = {
        "entries": first_entries,
        "mean": mean_first_entry
    }

    return result


""" *FIRST CORRECT ANSWER: DATE AND TIME DIFFERENCE FIRST CORRECT ANSWER: Query to work out the date of the first entry per student, the average of the date of the first entry """
def user_first_entry_and_first_correct_with_global(title_mo, title_ch, question_num):
    """
    Returns a list of dictionaries with:
    - First entry date per user
    - First correct answer date per user
    - Global earliest correct answer date
    - Time difference between global first correct and user's first correct
    - Average time difference (same value repeated for all users)
    """

    # Step 1: first entry per user
    first_entry_subq = (
        db.session.query(
            ModulsGD.user_id,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .group_by(ModulsGD.user_id)
        .subquery()
    )

    # Step 2: first correct per user
    first_correct_subq = (
        db.session.query(
            ModulsGD.user_id,
            func.min(ModulsGD.date_exercise).label("first_correct_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .filter(ModulsGD.question_result == 1)
        .group_by(ModulsGD.user_id)
        .subquery()
    )

    # Step 3: global first correct among all users
    global_first_correct = (
        db.session.query(func.min(ModulsGD.date_exercise))
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .filter(ModulsGD.question_result == 1)
        .scalar()
    )

    # Step 4: join both subqueries
    query = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_num,
            ModulsGD.question_result,
            first_entry_subq.c.first_date,
            first_correct_subq.c.first_correct_date
        )
        .join(
            first_entry_subq,
            and_(
                ModulsGD.user_id == first_entry_subq.c.user_id,
                ModulsGD.date_exercise == first_entry_subq.c.first_date
            )
        )
        .outerjoin(
            first_correct_subq,
            ModulsGD.user_id == first_correct_subq.c.user_id
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.user_id)
    )

    results = query.all()

    # Step 5: compute per-user differences
    data = []
    time_differences = []  # store total_seconds for averaging

    for r in results:
        if r.first_correct_date and global_first_correct:
            diff = r.first_correct_date - global_first_correct
            total_seconds = int(diff.total_seconds())
            time_differences.append(total_seconds)

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
            "user_id": r.user_id,
            "question_num": r.question_num,
            "question_result": r.question_result,
            "Date First Entry": r.first_date,
            "Date First Correct Answer": r.first_correct_date,
            "Global First Correct Date": global_first_correct,
            "Time Difference Between Global and User First Correct": diff_hms,
        })

    # Step 6: compute average of all time differences
    if time_differences:
        avg_seconds = sum(time_differences) / len(time_differences)
        avg_seconds = int(avg_seconds)
        days, remainder = divmod(avg_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        if days > 0:
            average_diff_hms = f"{days}d {hours:02}:{minutes:02}:{seconds:02}"
        else:
            average_diff_hms = f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        average_diff_hms = None

    # Step 7: integrate the average into each dictionary entry
    for entry in data:
        entry["Average Time Difference (Global vs Users' First Correct)"] = average_diff_hms

    return data

""" *ATTEMPTS: ATTEMPTS UNTIL CORRECT. Number of attempts until correct, and average number of attempts """
def attempts_until_correct(title_mo, title_ch, question_num):
    """
    Returns:
    - A list of dictionaries with:
        - user_id
        - question_num
        - number of attempts until first correct answer (1)
        - average number of attempts across users who succeeded
    """

    # Step 1: Retrieve all relevant answers
    answers = (
        db.session.query(
            ModulsGD.user_id,
            ModulsGD.question_result,
            ModulsGD.date_exercise
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.user_id, ModulsGD.date_exercise.asc())
        .all()
    )

    if not answers:
        print("No answers found.")
        return [], 0

    # Step 2: Group results by user_id
    from collections import defaultdict
    user_results = defaultdict(list)
    for ans in answers:
        user_results[ans.user_id].append(ans.question_result)

    # Step 3: Compute number of attempts until first correct (1)
    data = []
    attempt_counts = []

    for user_id, results in user_results.items():
        attempts = 0
        found_correct = False

        for r in results:
            attempts += 1
            if r == 1:
                found_correct = True
                break

        if found_correct:
            count_until_correct = attempts
        else:
            count_until_correct = None  # never got it right

        data.append({
            "user_id": user_id,
            "question_num": question_num,
            "Attempts Until Correct": count_until_correct
        })

        if count_until_correct is not None:
            attempt_counts.append(count_until_correct)

    # Step 4: Compute average attempts (only for users who got it right)
    average_attempts = round(sum(attempt_counts) / len(attempt_counts), 2) if attempt_counts else None

    # Step 5: Add the average to each record (for easy Jinja display)
    for record in data:
        record["Average Attempts (Users Who Succeeded)"] = average_attempts

    return data

""" *ALL THE ENTRIES: Query to work out all the entries per student """
def all_entries(title_mo, title_ch, question_num):
    """Return all entries per student for a specific question_num."""
    
    answers = (
        ModulsGD.query
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .order_by(ModulsGD.user_id)
        .order_by(ModulsGD.date_exercise.asc())
        .all()
    )

    # Group results by user_id
    results = {}
    for a in answers:
        if a.user_id not in results:
            results[a.user_id] = []
        results[a.user_id].append({
            "question_num": a.question_num,
            "question_result": a.question_result,
            "date_exercise": a.date_exercise.strftime("%Y-%m-%d %H:%M:%S")
        })

    return (results,answers)

""" *DATE CONSTRAINT. FIRST ENTRY: DATE AND TIME DIFFERENCE FIRST CORRECT ENTRY: Query to work out the time difference between each correct answer and the first correct answer in the first entry """
def date_constraint_time_user_first_entry_and_first_correct(title_mo, title_ch, question_num, start_date, end_date):
    """
    Returns a list of dictionaries with:
    - username
    - user_id
    - question_num
    - question_result
    - date of the first entry per user (within the given date range)
    - date of the first correct among first entries
    - time difference between user's first entry and first correct answer (if correct)

    Parameters
    ----------
    title_mo : str
        Module title
    title_ch : str
        Chapter title
    question_num : int
        Question number
    start_date : datetime
        Start of date filter (inclusive)
    end_date : datetime
        End of date filter (inclusive)
    """

    # Step 1: first entry per user (within date range)
    first_entry_subq = (
        db.session.query(
            ModulsGD.user_id,
            func.min(ModulsGD.date_exercise).label("first_date")
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .group_by(ModulsGD.user_id)
        .subquery()
    )

    # Step 2: join ModulsGD with subquery to get details of first entries
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
                ModulsGD.user_id == first_entry_subq.c.user_id,
                ModulsGD.date_exercise == first_entry_subq.c.first_date
            )
        )
        .filter(ModulsGD.title_mo == title_mo)
        .filter(ModulsGD.title_ch == title_ch)
        .filter(ModulsGD.question_num == question_num)
        .filter(ModulsGD.date_exercise >= start_date)
        .filter(ModulsGD.date_exercise <= end_date)
        .order_by(ModulsGD.user_id)
    )

    first_entries = first_entries_query.all()

    # Step 3: among those first entries, find the first correct one (if any)
    first_correct_date = None
    for r in first_entries:
        if r.question_result == 1:
            if first_correct_date is None or r.first_date < first_correct_date:
                first_correct_date = r.first_date

    # Step 4: build dictionary and compute time difference
    data = []
    for r in first_entries:
        user = db.session.query(User).filter(User.id == r.user_id).first()
        username = user.username if user else "Unknown"

        # Compute time difference only when the answer is correct
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
            "First Correct Among First Entries": first_correct_date,
            "Time Difference Your Answer and First Correct Answer": diff_hms
        })

    return data
