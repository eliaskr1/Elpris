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
    '''Funktion för endpointen "form". Skickar med
    variabel med morgondagens datum för att
    hindra användaren att fylla i datum som är
    ogiltiga.'''
    max_date=func.get_max_date()
    return render_template("form.html", max_date=max_date)

@app.route("/api", methods=["POST"])
def api_post():
    '''Funktion som callas när man fyllt formulär på "form" sidan.
    Skapar korrekt API url och skickar denna till funktioner
    i "func.py"'''
    try:
        date = request.form["date"]
        year, month, day = date.split('-')
        priceclass = request.form["prisklass"]
        api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{priceclass}.json"

        table = func.pandas_df_to_html_table(api_url)
        fig = func.pandas_df_to_plotly_diagram(api_url)

        return render_template("table.html", table=table, fig=fig, date=date, priceclass=priceclass)
    except ValueError as ve:
        '''Felhantering för tomt datum fält i "/form" endpoint.
        Laddar "/api" endpoint men skickar istället med "form.html"
        templaten och ett felmeddelande.''' 
        max_date=func.get_max_date()
        return render_template("form.html", max_date=max_date, error=ve)

@app.route("/api", methods=["GET"])
def api_get():
    '''Funktion som callas om man försöker komma in på 
    "/api" endpoint med "GET" metoden. Skickar användaren
    till startsidan istället.'''
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    '''Funktion som callas om man kopplar till hemsidan
    med en endpoint som inte finns. Laddar startsidan
    istället för att skicka felkod.'''
    return render_template("index.html"), 404