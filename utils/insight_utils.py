from datetime import datetime
from utils.database import get_db_connection


def get_current_month_range():
    today = datetime.now().date()
    current_month_start = today.replace(day=1)

    if current_month_start.month == 12:
        next_month_start = current_month_start.replace(
            year=current_month_start.year + 1,
            month=1
        )
    else:
        next_month_start = current_month_start.replace(
            month=current_month_start.month + 1
        )

    return today, current_month_start, next_month_start


def get_highest_spending_category(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    today, current_month_start, next_month_start = get_current_month_range()
    cursor.execute("""
    SELECT category, SUM(amount) AS total
    FROM expenses
    WHERE user_id = %s
      AND date >= %s
      AND date < %s
    GROUP BY category
    ORDER BY total DESC
    LIMIT 1
""", (user_id,current_month_start.isoformat(),next_month_start.isoformat()))

    
    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row:
        return {
            "category": row["category"],
            "amount": row["total"]
        }

    return None


def get_monthly_spending_comparison(
    user_id,
    current_month_start,
    next_month_start,
    previous_month_start
):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Current month total
    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0) AS total
        FROM expenses
        WHERE user_id = %s
        AND date >= %s
        AND date < %s
    """, (user_id, current_month_start, next_month_start))

    current_total = cursor.fetchone()["total"]

    # Previous month total
    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0) AS total
        FROM expenses
        WHERE user_id = %s
        AND date >= %s
        AND date < %s
    """, (user_id, previous_month_start, current_month_start))

    previous_total = cursor.fetchone()["total"]

    cursor.close()
    connection.close()

    return {
        "current_total": current_total,
        "previous_total": previous_total
    }


def get_current_month_expenses(
    user_id,
    current_month_start,
    next_month_start
):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT amount, category, date
        FROM expenses
        WHERE user_id = %s
        AND date >= %s
        AND date < %s
    """, (user_id, current_month_start, next_month_start))

    expenses = [dict(row) for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return expenses


def get_small_expenses(
    user_id,
    current_month_start,
    next_month_start
):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS count,
               COALESCE(SUM(amount), 0) AS total
        FROM expenses
        WHERE user_id = %s
        AND date >= %s
        AND date < %s
        AND amount < 200
    """, (user_id, current_month_start, next_month_start))

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    return {
        "count": row["count"],
        "total": row["total"]
    }


def get_spending_days(
    user_id,
    current_month_start,
    next_month_start
):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT date) AS spending_days
        FROM expenses
        WHERE user_id = %s
        AND date >= %s
        AND date < %s
    """, (user_id, current_month_start, next_month_start))

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    return row["spending_days"]