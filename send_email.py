import datetime as dt
import random
import smtplib


# sending email:
my_email = "sophiaadventure2020@gmail.com"
my_password ="#pythoncoding"

# use the datetime to abtain the current day of the week
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6: # today's day. Sunday
    # read quotes.txt and create a new list
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        one_quote = random.choice(quotes_list) # a random quote from the list
        print(one_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="s.yuan89@hotmail.com",
                            msg=f"Subject: Motivation quote everyday! \n\n{one_quote}")



