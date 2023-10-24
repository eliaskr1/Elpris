from flask import Flask, render_template, request
from application import func

app = Flask(__name__)

@app.route("/")
def index():
    '''Funktion för om man kopplar till hemsidan utan endpoint.'''
    return render_template("index.html")

@app.route("/form")
def form():
    '''Funktion för endpointen "form"'''
    return render_template("form.html")

@app.route("/api", methods=["POST"])  # type: ignore
def api_post():
    '''Funktion som callas när man fyllt formulär på "form" sidan'''
    date = request.form["date"]
    prisklass = request.form["prisklass"]

    data = func.elpris_data_to_html_table(date, prisklass)

    return render_template("table.html", data=data)