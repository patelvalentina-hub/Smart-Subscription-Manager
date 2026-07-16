from datetime import datetime
from decimal import Decimal

from flask import (
    Flask, 
    flash,
    redirect, 
    render_template, 
    request, 
    url_for
)


from app.models import Subscription, db

from app.utils import (
    calculate_estimated_monthly_cost,
    count_active_subscriptions,
    count_renewing_soon,
)

app = Flask(
    __name__, 
    template_folder="app/templates", 
    static_folder="app/static"
    )

app.secret_key = "smart_subscription_manager_secret"


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///subscriptions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/dashboard")
def dashboard():
    search_query = request.args.get("search", "").strip()
    status_filter = request.args.get("status", "")
    sort_by = request.args.get("sort", "")

    subscriptions_query = Subscription.query

    if search_query:
        subscriptions_query = subscriptions_query.filter(
            Subscription.name.ilike(f"%{search_query}%")
        )

    if status_filter:
        subscriptions_query = subscriptions_query.filter(
            Subscription.status == status_filter
        )

    if sort_by == "name_asc":
        subscriptions_query = subscriptions_query.order_by(
            Subscription.name.asc()
        )

    elif sort_by == "name_desc":
        subscriptions_query = subscriptions_query.order_by(
            Subscription.name.desc()
        )

    elif sort_by == "amount_asc":
        subscriptions_query = subscriptions_query.order_by(
            Subscription.amount.asc()
        )

    elif sort_by == "amount_desc":
        subscriptions_query = subscriptions_query.order_by(
            Subscription.amount.desc()
        )

    elif sort_by == "renewal_asc":
        subscriptions_query = subscriptions_query.order_by(
            Subscription.next_renewal_date.asc()
        )

    elif sort_by == "renewal_desc":
        subscriptions_query = subscriptions_query.order_by(
            Subscription.next_renewal_date.desc()
        )

    subscriptions = subscriptions_query.all()

    active_subscriptions = count_active_subscriptions()
    estimated_monthly_cost = calculate_estimated_monthly_cost()
    renewing_soon = count_renewing_soon()

    return render_template(
        "dashboard.html",
        subscriptions=subscriptions,
        active_subscriptions=active_subscriptions,
        estimated_monthly_cost=estimated_monthly_cost,
        renewing_soon=renewing_soon,
        search_query=search_query,
        status_filter=status_filter,
        sort_by=sort_by,
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

        flash("Subscription added successfully.", "success")

        return redirect(url_for("dashboard"))

    return render_template("add_subscription.html")



@app.route("/edit_subscription/<int:subscription_id>", methods=["GET", "POST"])
def edit_subscription(subscription_id):
    subscription = Subscription.query.get_or_404(subscription_id)

    if request.method == "POST":
        subscription.name = request.form["subscription_name"]
        subscription.category = request.form["category"]
        subscription.amount = Decimal(request.form["amount"])
        subscription.billing_frequency = request.form["billing_frequency"]
        subscription.start_date = datetime.strptime(
            request.form["start_date"], "%Y-%m-%d"
        ).date()
        subscription.next_renewal_date = datetime.strptime(
            request.form["next_renewal_date"], "%Y-%m-%d"
        ).date()
        subscription.status = request.form["status"]

        db.session.commit()

        flash("Subscription updated successfully.", "success")

        return redirect(url_for("dashboard"))

    return render_template(
        "add_subscription.html",
        subscription=subscription,
        is_editing=True,
    )



@app.route("/delete_subscription/<int:subscription_id>", methods=["POST"])
def delete_subscription(subscription_id):
    subscription = Subscription.query.get_or_404(subscription_id)

    db.session.delete(subscription)
    db.session.commit()

    flash("Subscription deleted successfully.", "success")

    return redirect(url_for("dashboard"))



with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
