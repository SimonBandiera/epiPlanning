##
## EPITECH PROJECT, 2021
## epi_planning
## File description:
## google_calendar.py
##


def add_event(list_of_lessons, calendar, service):
    if list_of_lessons == []:
        return []
    for event in list_of_lessons:
        event = {
            'summary' : event[2],
            'description' : event[3],

            'start' : {
                'dateTime' : event[0],
                'timeZone' : 'Europe/Paris'
            },
            'end' : {
                'dateTime' : event[1],
                'timeZone' : 'Europe/Paris'
            }
        }
        event = service.events().insert(calendarId = calendar['id'], body = event).execute()
    return event

def get_calendar_list(service):
    page_token = None
    calendar_list2 = []

    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    for items in calendar_list['items']:
        calendar_list2.append((items['summary'], items['id']))
    return calendar_list2

def create_calendar(calendar_list, service, list_of_lessons):
    for name in calendar_list:
        if 'EpiCalendar' == name[0]:
            service.calendars().delete(calendarId = name[1]).execute()
    calendar = {
        'summary' : 'EpiCalendar'
    }
    calendar = service.calendars().insert(body = calendar).execute()
    event = add_event(list_of_lessons, calendar, service)
    return (calendar, event)
