import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/PB10IZM/dp/B07VZRJQX1/ref=sr_1_6?crid=2V5YIWPXLY1D6&dchild=1&keywords=boat+power+bank&qid=1597386015&sprefix=boat+p%2Caps%2C464&sr=8-6"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    
page = requests.get(url, headers=headers)

soup =  BeautifulSoup(page.content, 'html.parser') #loaded site content

title = soup.find(id="productTitle").get_text() #fetched item name

price = soup.find(id="priceblock_ourprice").get_text() #fetch item price

price_converted = price[0 : 5]

print(price_converted)

print(title.strip())

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("akshayvinod73@gmail.com", "dtgnfetkzqfachbv")

# message to be sent
message = "test message"

# sending the mail
s.sendmail("akshayvinod73@gmail.com", "athiravinod964@gmail.com", message)

# terminating the session
s.quit()
