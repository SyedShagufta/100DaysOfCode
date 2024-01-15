import os
import random
import smtplib
import datetime as dt
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_EMAIL = os.env.EMAIL
MY_PASSWORD = os.env.PASSWORD

random_quotes = ["quote_1", "quote_2", "quote_3", "quote_4", "quote_5", "quote_6", "quote_7", "quote_8", "quote_9",
                 "quote_10", "quote_11", ]
emails = ["sweetyvox123@gmail.com", "sofiapersonalspace@gmail.com", "190039022cse@gmail.com",
          "johnjoelmota0418@gmail.com",
          "mister.gowthamkumar@gmail.com"]
now = dt.datetime.now()

for i in range(len(emails)):
    if now.weekday() == 0:
        with open("quotes.txt", "r") as quotes_data:
            quote = random.choice(quotes_data.readlines())
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "MONDAY MOTIVATION BY SOFIA"
        msg['From'] = MY_EMAIL
        msg['To'] = emails[i]
        text = MIMEText(_text=quote, _subtype='html')
        msg.attach(text)
        random_img = random.choice(random_quotes)
        image = MIMEImage(open(f'quotes_pictures/{random_img}.jpg', 'rb').read(), _subtype="jpg")
        image.add_header('Content-ID', '<ímage1>')
        msg.attach(image)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=emails[i], msg=msg.as_string())
