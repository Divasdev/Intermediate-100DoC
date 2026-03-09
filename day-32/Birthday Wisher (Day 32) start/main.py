import smtplib
import pandas as pd

import datetime as dt
import random


# quotes_data=pd.read_csv("quotes.txt")
#
# quotes_list=quotes_data.to_dict(orient="records")
# random_quotes=random.choice(quotes_list)



my_email="sharmadivas881@gmail.com"
APP_PASSWORD="sxmb umwj jqiv dxwn"

now=dt.datetime.now()
day_of_week=now.weekday()

if day_of_week==0:
    with open("quotes.txt") as file:
        quotes = file.readlines()

    random_quote = random.choice(quotes)
    print(random_quote)
    connection=smtplib.SMTP("smtp.gmail.com",587)


    # Transport layer security(TLS)
    connection.starttls()
    connection.login(my_email,APP_PASSWORD)
    connection.sendmail(from_addr=my_email,
                to_addrs="sharmapadma12345@gmail.com",
                msg=f"Subject:MOTIVATIONAL QUOTES\n\n{random_quote}")
    connection.close()








