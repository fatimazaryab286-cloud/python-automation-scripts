import requests
from bs4 import BeautifulSoup
import csv

books=requests.get('https://books.toscrape.com/')
soup=BeautifulSoup(books.text,'html.parser')
container=soup.find_all('article',class_='product_pod')

with open('books.csv',mode='w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title','Priceintext','rating'])

    for books in container:
    #title
     title=(books.find('h3').find('a').get('title'))
    #price
     price=books.find(class_='price_color')
     priceintext=price.text
     print(priceintext)
    #star-rating
     rating=books.find('p',class_='star-rating').get('class')[1]
     print(rating)
     writer.writerow([title,priceintext,rating])

    
    