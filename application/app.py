from flask import Flask, render_template, request
from application import func
from datetime import datetime, timedelta, date

app = Flask(__name__)

@app.route("/")
def index():
    '''Funktion för om man kopplar till hemsidan utan endpoint.'''
    return render_template("index.html")

@app.route("/form")
def form():
    '''Funktion för endpointen "form"'''
    
    return render_template("form.html", max_date=func.get_max_date())

@app.route("/api", methods=["POST"])
def api_post():
    '''Funktion som callas när man fyllt formulär på "form" sidan'''
    date = request.form["date"]
    year, month, day = date.split('-')
    prisklass = request.form["prisklass"]
    api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{prisklass}.json"

    data = func.json_data_to_html_table(api_url)

    return render_template("table.html", data=data)