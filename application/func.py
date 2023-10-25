import ssl
import json
from urllib import request
import urllib
import pandas as pd


def elpris_data_to_html_table(date, prisklass, columns=None):
    '''Konverterar angiven data i formatet åååå-mm-dd till html 
    tabell med elpriser för angiven dag och prisklass'''

    year, month, day = date.split('-')
    context = ssl._create_unverified_context()

    api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{prisklass}.json"
    json_data = request.urlopen(api_url, context=context).read()
    data = json.loads(json_data)
    df = pd.DataFrame(data)

    if columns==None:
        table_data = df.to_html(classes="table p-5", justify="left")    
    else:
        table_data = df.to_html(columns=columns,classes="table p-5", justify="left")

    return table_data


