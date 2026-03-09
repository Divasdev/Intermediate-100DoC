import datetime as dt
import pandas as pd
import random
import smtplib

now=dt.datetime.now()
today_date=now.date()
today_day=now.day
today_month=now.month
today=(today_month,today_day)


birthday_data=pd.read_csv("birthdays.csv")
birthday_dict = {
    (data_row.month,data_row.day): data_row
    for (index, data_row) in birthday_data.iterrows()
}

letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
random_letter=random.choice(letters)
print(random_letter)

if (today_month, today_day) in birthday_dict  :
    with open(f"letter_templates/{random_letter}","r") as to_send:
        letter_content=to_send.read()
        birthday_person=birthday_dict[today]
        letter_to_send=letter_content.replace("[NAME]",birthday_person["name"])

        my_email="sharmadivas881@gmail.com"
        APP_PASSWORD="sxmb umwj jqiv dxwn"

        connection = smtplib.SMTP("smtp.gmail.com", 587)

        # Transport layer security(TLS)
        connection.starttls()
        connection.login(my_email, APP_PASSWORD)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg="Subject:Birthday Wish\n\n{}".format(letter_to_send))
        connection.close()
