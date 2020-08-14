import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/PB10IZM/dp/B07VZRJQX1/ref=sr_1_6?crid=2V5YIWPXLY1D6&dchild=1&keywords=boat+power+bank&qid=1597386015&sprefix=boat+p%2Caps%2C464&sr=8-6"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    
page = requests.get(url, headers=headers)

soup =  BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())