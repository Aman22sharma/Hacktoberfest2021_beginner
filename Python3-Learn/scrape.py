

import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=994e1fc4-4bee-4da2-83c9-ff6663b2e0da"

#get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')

job_elems = soup.find_all('div', class_='_1HmYoV _35HD7C')

for job in job_elems:
    product = job.find_all('div', class_='_3wU53n')
    for pr in product:
        print(pr.text)
