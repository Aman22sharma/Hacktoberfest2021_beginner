// AUTHOR: Avyay Jain
// Python3 Concept: (calculator)
// GITHUB: https://github.com/avyayjain

import requests
from bs4 import BeautifulSoup

city = str(input("enter city name "))

url = "https://google.com/search?q="+"weather"+city
html = requests.get(url).content

soup = BeautifulSoup(html,'html.parser')

temp = soup.find('div',attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

time_skyDescription = soup.find('div',attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

data = time_skyDescription.split('\n')
time = data[0]
sky = data[1]

listdiv = soup.findAll('div',attrs={'class': 'BNeawe s3v9rd AP7Wnd'})


strd = listdiv[5].text

pos = strd.find('wind')
otherData= strd[pos:]

print("Temperature is ",temp)
print("time is ",time)
print("sky description: ",sky)
print(otherData)
