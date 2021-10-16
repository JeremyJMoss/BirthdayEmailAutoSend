import datetime as dt
import pandas
import smtplib
from random import randint

# replace with email you want to send from
my_email = "test@gmail.com"
# replace with password for email
password = "create_password()"

# 2. Check if today matches a birthday in the birthdays.csv
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")

for record in birthday_dict:
    if current_month == record["month"] and current_day == record["day"]:
        with open(f"letter_templates/letter_{str(randint(1, 3))}.txt", "r") as letter:
            email = letter.read().replace("[NAME]", record["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=record["email"],
                                msg=f"Subject: Happy Birthday!\n\n{email}")
