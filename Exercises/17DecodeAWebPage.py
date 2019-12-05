import requests

from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'

r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("span")

for link in links:
    print(link.text)