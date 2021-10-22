# AUTHOR: Diego Neves
# Python3 Concept: API, JSON
# GITHUB: github.com/diegoaceneves

import requests
import json

URL="http://economia.awesomeapi.com.br/json/last/USD-BRL"

response = requests.get(URL)
if (response.status_code == 200):
    print("R${:.2f} equal $US1.00 ".format(float(response.json()['USDBRL']['ask'])))
