from bs4 import BeautifulSoup

import requests

domain = "apod.nasa.gov/apod/"
url = domain + "astropix.html"
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)
print domain + soup.find_all('a')[1].get('href')

