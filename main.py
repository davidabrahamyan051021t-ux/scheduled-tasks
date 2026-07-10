##################### Extra Hard Starting Project ######################
import os
import datetime as dt
import random
import pandas as pd
import smtplib

EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

# մնացած կոդը նույնությամբ թողնում ես...
# 1. Update the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
file = pd.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv

for index, row in file.iterrows():
    if month == row["month"] and day == row["day"]:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number}.txt") as letter_file:
                letter = letter_file.read()
                final_letter = letter.replace("[NAME]", row["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(
                        from_addr=EMAIL,
                        to_addrs=row["email"],
                        msg=f"Subject:Happy Birthday\n\n{final_letter}"
                )
        
