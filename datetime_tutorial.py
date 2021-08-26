

import smtplib

# https://docs.python.org/3/library/smtplib.html

""""

# create a new smtp object, sending email from gamil
my_email = "sophiaadventure2020@gmail.com"
my_password = "#pythoncoding"


# the location of smtp server provide
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # tls stands for :transport layout security
    connection.login(user=my_email, password=my_password)  # provide user name and password
    connection.sendmail(from_addr=my_email,
                        to_addrs="sophiacodes@yahoo.com",
                        msg="Subject:this is subject\n\nThis is the body")


"""
# sending email from yahoo:
my_email = "sophiacodes@yahoo.com"
my_password = "jblheatbecfkcwpk" # this is password is generate by yahoo (app password)


# the location of smtp server provide
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()  # tls stands for :transport layout security # to connect the gmail server
    connection.login(user=my_email, password=my_password)  # provide user name and password
    connection.sendmail(from_addr=my_email,
                        to_addrs="sophiaadventure2020@gmail.com",
                        msg="Subject:this is subject\n\nThis is the body")


"""

import datetime as dt

# get current date and time
now = dt.datetime.now()
print(type(now))
year = now.year
if year == 2021:
    print("wear a mask!!")
print(type(year))
month = now.month
print(month)
day_of_week = now.weekday()  # 星期几，but computer starts count from 0, 0 is monday.
print(day_of_week)

#create a new object from datetime class:
date_of_birth =dt.datetime(year=1989, month=11, day=2, hour=17)
print(date_of_birth)

"""