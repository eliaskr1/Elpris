from application import func
import urllib


def test_json_data_to_pandas_df():
    '''Testar att json_data_to_pandas_df funktionen
    inte returnerar en exception med korrekt 
    formatterad API url.'''
    api_url = "https://www.elprisetjustnu.se/api/v1/prices/2023/05-05_SE1.json"
    df = func.json_data_to_pandas_df(api_url)
    assert len(df) > 0
    
def test_pandas_df_to_html_table():
    '''Testar att pandas_df_to_html_table funktionen
    inte returnerar en exception med korrekt 
    formatterad API url.'''
    api_url = "https://www.elprisetjustnu.se/api/v1/prices/2023/05-05_SE1.json"
    html_table = func.pandas_df_to_html_table(api_url)
    
    assert len(html_table) > 0
    
def test_pandas_df_to_plotly_diagram():
    '''Testar att pandas_df_to_plotly funktionen
    inte returnerar en exception med korrekt 
    formatterad API url.'''
    api_url = "https://www.elprisetjustnu.se/api/v1/prices/2023/05-05_SE1.json"
    plotly_diagram = func.pandas_df_to_plotly_diagram(api_url)
    
    assert len(plotly_diagram) > 0
    
def test_get_max_date():
    '''Testar att get_max_date funktionen
    returnerar en sträng på 10 karaktärer
    EG. åååå-mm-dd'''
    max_date = func.get_max_date()
    
    assert len(max_date) == 10
    
def test_data_to_pandas_df_exception():
    '''Testar att data_to_pandas_df funktionen
    returnerar förutsedd exception med 
    felaktigt formatterad API url.'''
    api_url = "https://www.elprisetjustnu.se/api/v1/prices//-_SE1.json"
    df = func.json_data_to_pandas_df(api_url)

    assert type(df) == urllib.error.HTTPError
    
def test_pandas_df_to_html_table_exception():
    '''Testar att pandas_df_to_html_table 
    funktionen returnerar förutsedd exception 
    med felaktigt formatterad API url.'''
    api_url = "https://www.elprisetjustnu.se/api/v1/prices//-_SE1.json"
    df = func.pandas_df_to_html_table(api_url)

    assert type(df) == AttributeError
    
def test_pandas_df_to_plotly_diagram_exception():
    '''Testar att andas_df_to_plotly_diagram 
    funktionen returnerar förutsedd exception 
    med felaktigt formatterad API url.'''
    api_url = "https://www.elprisetjustnu.se/api/v1/prices//-_SE1.json"
    df = func.pandas_df_to_plotly_diagram(api_url)

    assert type(df) == AttributeError