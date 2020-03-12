from bs4 import BeautifulSoup
import requests
import pymysql.cursors

db = pymysql.connect("localhost","root","","scraping")
cur = db.cursor()

url = "https://news.detik.com/berita/d-4874849/100-hari-jokowi-maruf-penuntasan-ham-penindakan-korupsi-jadi-sorotan"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

judul = soup.find('h1', class_='detail__title').text
print(judul)

tgl = soup.find('div', class_='detail__date').text
print(tgl)

img = soup.find('img', class_='p_img_zoomin img-zoomin')['src']
print(img)

isi = soup.find('div',class_='detail__body-text').text
print(isi)

link=url
print(link)

cur.execute("INSERT INTO scrap (judul,tgl,img,isi,link) VALUES (%s,%s,%s,%s,%s)",(judul,tgl,img,isi,link))
cur.connection.commit()