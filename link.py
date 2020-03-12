from bs4 import BeautifulSoup
import requests
import re


links = []
page = requests.get("https://news.detik.com/indeks")
soup = BeautifulSoup(page.text, 'html.parser')

link = soup.find_all('a', {"href": re.compile('berita')})
for l in link:
     i = l.get("href")
     links.append(i)
     get = list(dict.fromkeys(links))
print(get)