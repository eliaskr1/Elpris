import pytest
import urllib.request
import ssl
import requests

context = ssl._create_unverified_context()


def test_Is_online_index():
    assert urllib.request.urlopen("http://127.0.0.1:5000/", context=context, timeout=10)

def test_Is_online_form():
    assert urllib.request.urlopen("http://127.0.0.1:5000/form", context=context, timeout=10)
    
def test_api_get_reroute_to_index():
    '''Kollar om "/api" endpoint laddar "index" template'''
    with urllib.request.urlopen("http://127.0.0.1:5000/api", context=context) as response:
        html = str(response.read())
        assert "Aktuella elpriser:" in html
        
