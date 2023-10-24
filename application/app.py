from flask import Flask, render_template
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

@app.route("/api", methods=["POST"])
def api_post():
    '''Funktion som callas när man fyllt formulär på "form" sidan'''
    pass # Byts ut med return sats