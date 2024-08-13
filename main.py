import smtplib
import datetime as dt
import random

USER_EMAIL = ""  # enter user email address
USER_PASS = ""  # this is the app password generated from email provider
USER_SMTP = ""  # this is the smtp address of user email provider
RECIPIENT_EMAIL = ""  # this is recipients email address
DATE = 0  # if today's date is equal to this, then send the email, Monday = 0 and Sunday  = 7
EMAIl_SUB = ""  # enter what should appear as emails subject

today = dt.datetime.now()  # obtains today's date
random_quote = random.randint(0, 100)


def quotes(random_quote=random_quote):
    """takes the int generated and assigned to random_quote variable and
    uses this to index a random quote from quotes txt"""
    if today.weekday() == DATE:
        with open("quotes.txt", mode="r") as c:
            quotes = c.read().splitlines()
            return quotes[random_quote]
    else:
        return None


quote = quotes(random_quote)  # variable with random quote assigned

with smtplib.SMTP(USER_SMTP) as connection:
    connection.starttls()
    connection.login(user=USER_EMAIL, password=USER_PASS)
    connection.sendmail(
        from_addr=USER_EMAIL,
        to_addrs=RECIPIENT_EMAIL,
        msg=f"Subject:{EMAIl_SUB}\n\nHere is a motivational quote to start your week!\n\n{quote}"
    )
