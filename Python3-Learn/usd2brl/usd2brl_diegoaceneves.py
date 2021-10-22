# AUTHOR: Diego Neves
# Python3 Concept: API, JSON
# GITHUB: github.com/diegoaceneves

import requests
import json

URL="http://economia.awesomeapi.com.br/json/last/USD-BRL"

response = requests.get(URL)
if (response.status_code == 200):
    print("$US1.00 is equal R${:.2f}\n".format(float(response.json()['USDBRL']['ask'])))
