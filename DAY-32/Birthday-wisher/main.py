# --------------------- Extra Hard Starting Project -----------------
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import os
import random
import smtplib

import pandas as pd
MY_EMAIL = os.env.EMAIL
MY_PASSWORD = os.env.PASSWORD

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
letter_templates = ["letter_1", "letter_2", "letter_3"]


for i in range(len(df)):
    if now.month == df.month[i] and now.day == df.day[i]:
        print("yes")
        print(df.email[i])
        random_letter = random.choice(letter_templates)
        with open(f"./letter_templates/{random_letter}.txt", "r") as letter:
            birthday_wish = letter.read()
            birthday_wish = birthday_wish.replace("[NAME]", df.name[i])
            print(birthday_wish)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=df.email[i],
                                    msg=f"Subject:HAPPY BIRTHDAY\n\n {birthday_wish}")
