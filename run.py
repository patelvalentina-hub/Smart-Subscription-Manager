from flask import Flask, render_template
app = Flask(
    __name__, 
    template_folder="app/templates", 
    static_folder="app/static"
    )


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



@app.route("/add_subscription")
def add_subscription():
    return render_template("add_subscription.html")



if __name__ == "__main__":
    app.run(debug=True)
