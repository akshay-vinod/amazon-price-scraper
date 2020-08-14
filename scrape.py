import requests
from bs4 import BeautifulSoup
import smtplib
import time
def check_price():
    url = "https://www.amazon.in/PB10IZM/dp/B07VZRJQX1/ref=sr_1_6?crid=2V5YIWPXLY1D6&dchild=1&keywords=boat+power+bank&qid=1597386015&sprefix=boat+p%2Caps%2C464&sr=8-6"

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
        
    page = requests.get(url, headers=headers)

    soup =  BeautifulSoup(page.content, 'html.parser') #loaded site content

    title = soup.find(id="productTitle").get_text() #fetched item name

    price = soup.find(id="priceblock_ourprice").get_text() #fetch item price
    modprice = ''.join(filter(lambda i: i.isdigit(), price))
    converted_price = float(modprice[0:3])
    print((converted_price))
    print(title.strip())

    if (converted_price < 899.0): 
        send_mail()  
    else:
        print("NO CHANGE IN PRICE")
def send_mail():
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("sender_email_id", "sender_email_id_password") 

        # message to be sent
        message = "PRICE CHANGED CHECK NOW "

        # sending the mail
        s.sendmail("sender_email_id", "receiver_email_id", message)

        # terminating the session
        s.quit()
        print("email has been send")
while(True):
    check_price()
    time.sleep(1) #check price in every 1 min


        
