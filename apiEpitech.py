import requests


def get_planning(cookie, date_start, date_end):
    COOKIES = {
        "user" : cookie,
    }
    r = requests.get(f'https://intra.epitech.eu/planning/load?format=json&start={date_start}&end={date_end}', cookies=COOKIES)
    list_calendar = []
    for i in r.json():
        if i["event_registered"]:
            list_calendar.append(
                [i["start"].replace(" ", "T"), i["end"].replace(" ", "T"), i["acti_title"], f"salle : {i['room']['code'].split('/')[-1]}"])

    return list_calendar
if __name__ == "__main__":
    planner = get_planning('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InNpbW9uLmJhbmRpZXJhQGVwaXRlY2guZXUiLCJ0eiI6bnVsbCwiZXhwIjoxNjg0ODUwMDY2fQ.PO2LB7aQyUGqs4Atrm4cSF4n0GDsMAujd2d-pBkB1i8', '2021-11-08',
                           '2021-11-14')
    print(planner)
