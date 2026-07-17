from datetime import date, timedelta

from dateutil.relativedelta import relativedelta

from app.models import Subscription

def calculate_next_renewal_date(start_date, billing_frequency):
    """
    Calculate the expected next renewal date.
    """

    if billing_frequency == "Weekly":
        return start_date + timedelta(weeks=1)

    if billing_frequency == "Monthly":
        return start_date + relativedelta(months=1)

    if billing_frequency == "Every 3 Months":
        return start_date + relativedelta(months=3)

    if billing_frequency == "Every 6 Months":
        return start_date + relativedelta(months=6)

    if billing_frequency == "Yearly":
        return start_date + relativedelta(years=1)

    return None



def is_valid_renewal_date(
    start_date,
    billing_frequency,
    next_renewal_date,
    tolerance_days=0,
):
    """
    Check whether the renewal date is close to the expected billing date.
    """

    expected_date = calculate_next_renewal_date(
        start_date,
        billing_frequency,
    )

    if expected_date is None:
        return False

    difference = abs((next_renewal_date - expected_date).days)

    return difference <= tolerance_days

            
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