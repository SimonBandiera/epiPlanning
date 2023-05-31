import datetime
from google import Create_Service
from google_calendar import create_calendar, get_calendar_list
import apiEpitech
import time

one_day = datetime.timedelta(days=1)
last = ""
CLIENT_SECRET_FILE = 'code_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_week(date):
    day_idx = (date.weekday()) % 7  # turn sunday into 0, monday into 1, etc.
    sunday = date - datetime.timedelta(days=day_idx)
    date = sunday
    for n in range(7):
        yield date
        date += one_day



print("lancement de la query " + str(datetime.date.today()))
while True:
    last = datetime.date.today()
    with open("all_user.txt", "r") as f:
        data = f.read()
    for user in data.split(";"):
        user = user.split(",")
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES, prefix=user[0])
        week = [d.isoformat() for d in get_week(datetime.datetime.now().date())]
        data = apiEpitech.get_planning(user[1], week[0], week[6])
        create_calendar(get_calendar_list(service), service, data)
    time.sleep(3600)

