from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    billing_frequency = db.Column(db.String(30), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    last_renewal_date = db.Column(db.Date, nullable=True)
    next_renewal_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    renewal_history = db.relationship(
        "RenewalHistory",
        back_populates="subscription",
        cascade="all, delete-orphan",
        lazy=True
    )

class RenewalHistory(db.Model):
    __tablename__ = "renewal_history"

    id = db.Column(db.Integer, primary_key=True)

    subscription_id = db.Column(
        db.Integer,
        db.ForeignKey("subscriptions.id"),
        nullable=False
    )

    renewed_on = db.Column(db.Date, nullable=False)

    amount_paid = db.Column(db.Numeric(10, 2), nullable=False)

    notes = db.Column(db.Text, nullable=True)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )


    subscription = db.relationship(
        "Subscription",
        back_populates="renewal_history"
    )