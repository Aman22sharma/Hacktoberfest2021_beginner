from bs4 import BeautifulSoup
import requests
initial_url = 'https://www.linkedin.com/jobs/search?'
def find_jobs():
    location = input("Enter Your Prefferred Location: ")
    keyword = input("Do you Want any Specific Keyword in the Search?")
    if " " in location:
        location = location.replace(" ","%20")
    if "," in location:
        location = location.replace(",","%2C")
    if " " in keyword:
        keyword = keyword.replatimece(" ","%20")
    if "," in keyword:
        keyword = keyword.replace(",","%2C")
    final_url = initial_url+"keywords="+keyword+"&location="+location+"&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0"
    print(final_url)
    address = requests.get(final_url)
    src = address.content
    soup = BeautifulSoup(src, 'lxml')
    notes = soup.find_all('a', class_="base-card__full-link")
    #print(notes)
    for i in notes:
        link=i['href']
        #print(link)
        parent = i.find_parent()
        print(parent.find('h3').text)
        #print(parent.find('h4').text)
        #print(parent.find('span',class_="job-search-card__location").text)
        #print(parent.find('time')['datetime'])
find_jobs()
