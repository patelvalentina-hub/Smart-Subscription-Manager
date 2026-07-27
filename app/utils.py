from datetime import date, timedelta

from dateutil.relativedelta import relativedelta

from app.models import Subscription


def calculate_next_renewal_date(current_date, billing_frequency):
    """
    Calculate one billing interval after the supplied date.
    """

    frequency_offsets = {
        "Weekly": relativedelta(weeks=1),
        "Monthly": relativedelta(months=1),
        "Every 3 Months": relativedelta(months=3),
        "Every 6 Months": relativedelta(months=6),
        "Yearly": relativedelta(years=1),
    }

    offset = frequency_offsets.get(billing_frequency)

    if offset is None:
        return None

    return current_date + offset


def calculate_renewal_date_for_cycle(
    start_date,
    billing_frequency,
    cycle_number,
):
    """
    Calculate a scheduled renewal date using the original
    subscription start date as the fixed billing anchor.
    """

    if billing_frequency == "Weekly":
        return start_date + relativedelta(weeks=cycle_number)

    if billing_frequency == "Monthly":
        return start_date + relativedelta(months=cycle_number)

    if billing_frequency == "Every 3 Months":
        return start_date + relativedelta(
            months=3 * cycle_number
        )

    if billing_frequency == "Every 6 Months":
        return start_date + relativedelta(
            months=6 * cycle_number
        )

    if billing_frequency == "Yearly":
        return start_date + relativedelta(years=cycle_number)

    return None


def is_valid_renewal_date(
    start_date,
    billing_frequency,
    next_renewal_date,
):
    """
    Validate the first renewal date for a subscription that has
    never been renewed.
    """

    if not start_date or not next_renewal_date:
        return False

    expected_date = calculate_next_renewal_date(
        start_date,
        billing_frequency,
    )

    if expected_date is None:
        return False

    return next_renewal_date == expected_date


def calculate_days_remaining(renewal_date):
    """
    Returns the number of days until the renewal date.

    Returns:
        > 0 : Renewal is in the future
        = 0 : Renewal is due today
        < 0 : Renewal is overdue
    """
    today = date.today()
    return (renewal_date - today).days


def count_active_subscriptions():
    return Subscription.query.filter_by(status="Active").count()


def get_monthly_cost(subscription):
    if subscription.billing_frequency == "Weekly":
        return (subscription.amount * 52) / 12

    elif subscription.billing_frequency == "Monthly":
        return subscription.amount

    elif subscription.billing_frequency == "Every 3 Months":
        return subscription.amount / 3

    elif subscription.billing_frequency == "Every 6 Months":
        return subscription.amount / 6

    elif subscription.billing_frequency == "Yearly":
        return subscription.amount / 12

    return 0


def calculate_estimated_monthly_cost():
    subscriptions = Subscription.query.filter_by(status="Active").all()

    total = 0

    for subscription in subscriptions:
        total += get_monthly_cost(subscription)

    return round(total, 2)



def count_renewing_soon():
    today = date.today()
    seven_days_from_now = today + timedelta(days=7)

    return Subscription.query.filter(
        Subscription.status == "Active",
        Subscription.next_renewal_date >= today,
        Subscription.next_renewal_date <= seven_days_from_now,
    ).count()



def calculate_yearly_cost():
    """
    Estimate total yearly subscription cost.
    """


    total = 0

    subscriptions = Subscription.query.filter_by(
        status="Active"
    ).all()

    for subscription in subscriptions:
        
        if subscription.billing_frequency == "Weekly":
            total += float(subscription.amount) * 52

        elif subscription.billing_frequency == "Monthly":
            total += float(subscription.amount) * 12

        elif subscription.billing_frequency == "Every 3 Months":
            total += float(subscription.amount) * 4

        elif subscription.billing_frequency == "Every 6 Months":
            total += float(subscription.amount) * 2

        elif subscription.billing_frequency == "Yearly":
            total += float(subscription.amount)
    
    return round(total, 2)



def get_most_expensive_subscription():
    """
    Return the active subscription with the highest monthly cost.
    """

    subscriptions = Subscription.query.filter_by(
        status="Active"
    ).all()

    if not subscriptions:
        return None

    def monthly_cost(subscription):
        if subscription.billing_frequency == "Weekly":
            return float(subscription.amount) * 52 / 12

        elif subscription.billing_frequency == "Monthly":
            return float(subscription.amount)

        elif subscription.billing_frequency == "Every 3 Months":
            return float(subscription.amount) / 3

        elif subscription.billing_frequency == "Every 6 Months":
            return float(subscription.amount) / 6

        elif subscription.billing_frequency == "Yearly":
            return float(subscription.amount) / 12

        return 0

    return max(subscriptions, key=monthly_cost)



def get_cheapest_subscription():
    """
    Return the active subscription with the lowest monthly cost.
    """

    subscriptions = Subscription.query.filter_by(
        status="Active"
    ).all()

    if not subscriptions:
        return None

    def monthly_cost(subscription):

        if subscription.billing_frequency == "Weekly":
            return float(subscription.amount) * 52 / 12

        elif subscription.billing_frequency == "Monthly":
            return float(subscription.amount)

        elif subscription.billing_frequency == "Every 3 Months":
            return float(subscription.amount) / 3

        elif subscription.billing_frequency == "Every 6 Months":
            return float(subscription.amount) / 6

        elif subscription.billing_frequency == "Yearly":
            return float(subscription.amount) / 12

        return 0

    return min(subscriptions, key=monthly_cost)



def calculate_spending_by_category():
    """
    Return estimated monthly spending grouped by category.
    """

    subscriptions = Subscription.query.filter_by(
        status="Active"
    ).all()

    category_totals = {}

    for subscription in subscriptions:
        if subscription.billing_frequency == "Weekly":
            monthly_cost = float(subscription.amount) * 52 / 12

        elif subscription.billing_frequency == "Monthly":
            monthly_cost = float(subscription.amount)

        elif subscription.billing_frequency == "Every 3 Months":
            monthly_cost = float(subscription.amount) / 3

        elif subscription.billing_frequency == "Every 6 Months":
            monthly_cost = float(subscription.amount) / 6

        elif subscription.billing_frequency == "Yearly":
            monthly_cost = float(subscription.amount) / 12

        else:
            monthly_cost = 0

        category_totals[subscription.category] = (
            category_totals.get(subscription.category, 0) 
            + monthly_cost
        )
    return {
        category: round(total, 2)
        for category, total in category_totals.items()
    }



def get_upcoming_renewals(days=7):
    """
    Return active subscriptions renewing within the next
    specified number of days.
    """

    today = date.today()
    end_date = today + timedelta(days=days)

    return (
        Subscription.query.filter(
            Subscription.status == "Active",
            Subscription.next_renewal_date >= today,
            Subscription.next_renewal_date <= end_date,
        )
        .order_by(Subscription.next_renewal_date.asc())
        .all()
    )