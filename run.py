from datetime import datetime
from decimal import Decimal

from flask import Flask, redirect, render_template, request, url_for

from app.models import Subscription, db

from app.utils import count_active_subscriptions

app = Flask(
    __name__, 
    template_folder="app/templates", 
    static_folder="app/static"
    )

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///subscriptions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/dashboard")
def dashboard():
    subscriptions = Subscription.query.all()

    active_subscriptions = count_active_subscriptions()

    return render_template(
        "dashboard.html",
        subscriptions=subscriptions,
        active_count=active_subscriptions,
    )



@app.route("/add_subscription", methods=["GET", "POST"])
def add_subscription():
    if request.method == "POST":
        subscription = Subscription(
            name=request.form["subscription_name"],
            category=request.form["category"],
            amount=Decimal(request.form["amount"]),
            billing_frequency=request.form["billing_frequency"],
            start_date=datetime.strptime(
                request.form["start_date"], "%Y-%m-%d"
            ).date(),
            next_renewal_date=datetime.strptime(
                request.form["next_renewal_date"], "%Y-%m-%d"
            ).date(),
            status=request.form["status"],
        )

        db.session.add(subscription)
        db.session.commit()

        return redirect(url_for("dashboard"))

    return render_template("add_subscription.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
