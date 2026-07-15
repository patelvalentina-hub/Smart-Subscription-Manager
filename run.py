from flask import Flask, render_template
from app.models import db

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
    return render_template("dashboard.html")



@app.route("/add_subscription")
def add_subscription():
    return render_template("add_subscription.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
