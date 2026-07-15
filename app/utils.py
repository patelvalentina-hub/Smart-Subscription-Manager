from app.models import Subscription


def count_active_subscriptions():
    return Subscription.query.filter_by(status="Active").count()