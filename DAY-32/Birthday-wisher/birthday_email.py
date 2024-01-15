import os
from email.message import EmailMessage
import smtplib
import datetime as dt
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

import pandas as pd
MY_EMAIL = os.env.EMAIL
MY_PASSWORD = os.env.PASSWORD

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
letter_templates = ["letter_1", "letter_2", "letter_3"]
random_images = ["birthday_img_1", "birthday_img_2", "birthday_img_3", "birthday_img_4", "birthday_img_5"]

for i in range(len(df)):
    if now.month == df.month[i] and now.day == df.day[i]:
        random_letter = random.choice(letter_templates)
        with open(f"./letter_templates/{random_letter}.txt", "r") as letter:
            birthday_wish = letter.read()
            birthday_wish = birthday_wish.replace("[NAME]", df.name[i])
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Happy Birthday Dear {df.name[i]}!"
        msg['From'] = MY_EMAIL
        msg['To'] = df.email[i]
        text = MIMEText(_text=birthday_wish, _subtype='html')
        msg.attach(text)
        random_img = random.choice(random_images)
        image = MIMEImage(open(f'birthday_pictures/{random_img}.jpg', 'rb').read())
        image.add_header('Content-ID', '<ímage1>')
        msg.attach(image)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=df.email[i],
                                    msg=msg.as_string())
