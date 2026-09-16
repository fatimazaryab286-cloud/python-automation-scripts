import argparse
import requests, csv
from bs4 import BeautifulSoup

parser=argparse.ArgumentParser()
parser.add_argument('--url',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()

books=requests.get(args.url)
soup=BeautifulSoup(books.text,'html.parser')
container=soup.find_all('article',class_='product_pod')

with open(args.output,mode='w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title','Priceintext','rating'])

    for books in container:
    #title
     title=(books.find('h3').find('a').get('title'))
    #price
     price=books.find(class_='price_color')
     priceintext=price.text
    #star-rating
     rating=books.find('p',class_='star-rating').get('class')[1]
     writer.writerow([title,priceintext,rating])
    


    
    