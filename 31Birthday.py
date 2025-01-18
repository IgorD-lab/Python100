from datetime import datetime
import pandas
import random
import smtplib

# ---------------------------------------
# This application stores birthday dates of people and sends them automated emails.

#
# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# TODO - as of 2025 google no longer supports login via app so you are no longer able to log in with @gmail.com
# 2. Go to your email provider and make it allow less secure apps.
# Account that is sending emails needs to have reduced security:
# 2-Step-off, Use phone to sign in-off, Less Secure Apps - ON
# 3. Update the SMTP ADDRESS to match your email provider (ex: smtp.gmail.com).
# 4. Update birthdays.csv to contain today's month and day.
# ---------------------------------------

MY_EMAIL = "EMAIL"
MY_PASSWORD = "EMAIL PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./resources/Data/31letters/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

