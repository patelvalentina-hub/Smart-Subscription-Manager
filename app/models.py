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
    next_renewal_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)