import ssl
import json
import urllib
from urllib import request
from urllib import error
import pandas as pd
from datetime import datetime, timedelta


def json_data_to_html_table(api_url, columns=None):
    '''Konverterar json data från api till en
    html tabell med Pandas'''

    context = ssl._create_unverified_context()
    try:
        json_data = request.urlopen(api_url, context=context).read()
        data = json.loads(json_data)
        df = pd.DataFrame(data)

        if columns==None:
            table_data = df.to_html(classes="table p-5", justify="left")    
        else:
            table_data = df.to_html(columns=columns,classes="table p-5", justify="left")

        return table_data
    except Exception as e:
        # Om man försöker ladda elpriser som inte har publicerats ännu.
        if isinstance(e, error.HTTPError) and e.code == 404:
            return "Sidan existerar inte."

        # Plats för annan eventuell felhantering
        return "Ett fel uppstod. Kontakta administratören för hjälp."

def get_max_date():
    '''Returnerar en sträng med morgondagens datum
    i formatet "åååå-mm-dd'''
    date = datetime.today()
    new_date = date + timedelta(days=1)
    day = new_date.day
    month = new_date.month
    year = new_date.year
    max_date = f"{year}-{month:02d}-{day:02d}"
    
    return max_date
