import os
from pprint import pprint
import smtplib
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = os.environ['my_email']
my_pswd = os.environ['my_pswd']

url = "https://www.flipkart.com/samsung-galaxy-book3-intel-core-i5-13th-gen-1335u-16-gb-512-gb-ssd-windows-11-home-thin-light-laptop/p/itm9c25e72104066?pid=COMGN5FVZXFK26KS&lid=LSTCOMGN5FVZXFK26KSM6BP7L&marketplace=FLIPKART&sattr[]=color&sattr[]=system_memory&st=system_memory"
response = requests.get(url,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
                            "Accept-Language": "en-US,en;q=0.5",
                        }
                        )
web_page = response.text

# Scraping the Website, Price and Title
soup = BeautifulSoup(web_page, "lxml")

title = soup.find(name="span", class_="B_NuCI").get_text()
print(title)
price = soup.find(name="div", class_="_30jeq3 _16Jk6d").get_text().split("₹")[1].replace(',', '').strip()
actual_price = float(price)
print(actual_price)

# Sending an Email if it drops the price
if actual_price < 79990.0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pswd)
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = "sweetyvox123@gmail.com"
        msg['Cc'] = "190031562cse@gmail.com"
        msg['Subject'] = "Mail from Automatic Laptop price teller Bot 📩🤖."
        body = f"The price for the below product went down 🔻 \n\n {title} \n\n you can checkout from this link 😉👇 \n\n {url}"
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        msg_str = msg.as_string()
        connection.sendmail(my_email, "sweetyvox123@gmail.com", msg_str)
# connection.sendmail(from_addr=my_email, to_addrs="sweetyvox123@gmail.com",
#                            msg=f"Subject: Test Mail for Laptop price teller bot 📩🤖. \n\n The price for the below product went down 🔻 \n {title} \n you can checkout from this link 😉👇 \n {url}")
