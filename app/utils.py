from datetime import date, timedelta

from app.models import Subscription


def count_active_subscriptions():
    return Subscription.query.filter_by(status="Active").count()

def calculate_estimated_monthly_cost():
    subscriptions = Subscription.query.filter_by(status="Active").all()

    total = 0

    for subscription in subscriptions:

        if subscription.billing_frequency == "Weekly":
            total += (subscription.amount * 52) / 12

        elif subscription.billing_frequency == "Monthly":
            total += subscription.amount

        elif subscription.billing_frequency == "Every 3 Months":
            total += subscription.amount / 3

        elif subscription.billing_frequency == "Every 6 Months":
            total += subscription.amount / 6

        elif subscription.billing_frequency == "Yearly":
            total += subscription.amount / 12

    return round(total, 2)


def count_renewing_soon():
    today = date.today()
    seven_days_from_now = today + timedelta(days=7)

    return Subscription.query.filter(
        Subscription.status == "Active",
        Subscription.next_renewal_date >= today,
        Subscription.next_renewal_date <= seven_days_from_now,
    ).count()