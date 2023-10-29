from urllib.error import HTTPError
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
    max_date=func.get_max_date()
    return render_template("form.html", max_date=max_date)

@app.route("/api", methods=["POST"])
def api_post():
    '''Funktion som callas när man fyllt formulär på "form" sidan'''
    try:
        date = request.form["date"]
        year, month, day = date.split('-')
        prisklass = request.form["prisklass"]
        api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{prisklass}.json"

        data = func.json_data_to_html_table(api_url)

        return render_template("table.html", data=data)
    except ValueError as ve:
        # Felhantering för tomt datum fält i "/form" endpoint. 
        return "Vänligen ange giltigt datum."

@app.route("/api", methods=["GET"])
def api_get():
    '''Funktion som callas om man försöker komma in på 
    "/api" endpoint med "GET" metoden'''
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404