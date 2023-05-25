import requests


def get_planning(url, date_start, date_end):
    s = requests.Session()
    s.get(url)
    r = s.get(f'https://intra.epitech.eu/planning/load?format=json&start={date_start}&end={date_end}')
    list_calendar = []
    for i in r.json():
        if i["event_registered"]:
            list_calendar.append(
                [i["start"].replace(" ", "T"), i["end"].replace(" ", "T"), i["acti_title"], f"salle : {i['room']['code'].split('/')[-1]}"])

    return list_calendar
if __name__ == "__main__":
    planner = get_planning('https://intra.epitech.eu/auth-49a1479057f247d75ac3d0d251d9d03de2e1172a', '2021-11-08',
                           '2021-11-14')
