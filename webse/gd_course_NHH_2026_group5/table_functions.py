from webse.models import Transport_NHH_2026_g5
from webse import db
from datetime import timedelta, datetime
from sqlalchemy import func


def get_entries(user_id, user_type, days=5):
    start_date = datetime.now() - timedelta(days=days)

    return (
        Transport_NHH_2026_g5.query
        .filter_by(user_id=user_id, user_type=user_type)
        .filter(Transport_NHH_2026_g5.created_at > start_date)
        .order_by(Transport_NHH_2026_g5.created_at.desc(), Transport_NHH_2026_g5.transport.asc())
        .all()
    )
    
    
def get_latest_entry(user_id, user_type):
    return (
        Transport_NHH_2026_g5.query
        .filter_by(user_id=user_id, user_type=user_type)
        .order_by(Transport_NHH_2026_g5.created_at.desc())
        .first()
    )

def format_entries_for_table(entries):
    formatted = []

    for entry in entries:
        formatted.append({
            "id": entry.id,
            "date": entry.created_at.strftime("%Y-%m-%d"),
            "user_type": entry.user_type,
            "transport": entry.transport,
            "fuel": entry.fuel or "-",
            "kms": entry.kms or "-",
            "co2": entry.co2
        })

    return formatted


def get_emissions_by_transport(user_id, user_type, days=5):
    start_date = datetime.now() - timedelta(days=days)

    return (
        db.session.query(func.sum(Transport_NHH_2026_g5.co2), Transport_NHH_2026_g5.transport)
        .filter(Transport_NHH_2026_g5.user_id == user_id)
        .filter(Transport_NHH_2026_g5.user_type == user_type)
        .filter(Transport_NHH_2026_g5.created_at > start_date)
        .group_by(Transport_NHH_2026_g5.transport)
        .order_by(Transport_NHH_2026_g5.transport.asc())
        .all()
    )


def get_kms_by_transport(user_id, user_type, days=5):
    start_date = datetime.now() - timedelta(days=days)

    return (
        db.session.query(func.sum(Transport_NHH_2026_g5.kms), Transport_NHH_2026_g5.transport)
        .filter(Transport_NHH_2026_g5.user_id == user_id)
        .filter(Transport_NHH_2026_g5.user_type == user_type)
        .filter(Transport_NHH_2026_g5.created_at > start_date)
        .group_by(Transport_NHH_2026_g5.transport)
        .order_by(Transport_NHH_2026_g5.transport.asc())
        .all()
    )


def get_emissions_by_date(user_id, user_type, days=5):
    start_date = datetime.now() - timedelta(days=days)

    return (
        db.session.query(func.sum(Transport_NHH_2026_g5.co2), func.date(Transport_NHH_2026_g5.created_at))
        .filter(Transport_NHH_2026_g5.user_id == user_id)
        .filter(Transport_NHH_2026_g5.user_type == user_type)
        .filter(Transport_NHH_2026_g5.created_at > start_date)
        .group_by(func.date(Transport_NHH_2026_g5.created_at))
        .order_by(func.date(Transport_NHH_2026_g5.created_at).asc())
        .all()
    )


def get_kms_by_date(user_id, user_type, days=5):
    start_date = datetime.now() - timedelta(days=days)

    return (
        db.session.query(func.sum(Transport_NHH_2026_g5.kms), func.date(Transport_NHH_2026_g5.created_at))
        .filter(Transport_NHH_2026_g5.user_id == user_id)
        .filter(Transport_NHH_2026_g5.user_type == user_type)
        .filter(Transport_NHH_2026_g5.created_at > start_date)
        .group_by(func.date(Transport_NHH_2026_g5.created_at))
        .order_by(func.date(Transport_NHH_2026_g5.created_at).asc())
        .all()
    )