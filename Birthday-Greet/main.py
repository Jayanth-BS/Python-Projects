import random
import pandas as pd
import datetime
import smtplib

email = "xxxxxxxxxxxxxxx@gmail.com"
passw = "xxxxxxxxxxxxxxxxxxxx"


def send(name):
    ch = random.randint(1, 3)
    with open(f"letter_templates/letter_{ch}.txt") as f:
        content = f.read()

    content = content.replace('[NAME]', name)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=passw)
        connection.sendmail(from_addr=email, to_addrs="yyyyyyyyyyyyyyy@gmail.com",
                            msg=f'Subject:Happy Birthday\n\n{content}')

now = datetime.datetime.now()
day = now.day
month = now.month

data = pd.read_csv('birthdays.csv')
print(data)
global name
for ind,row in data.iterrows():
    if day == row['day'] and month == row['month']:
        name = row['name']
        send(name)



