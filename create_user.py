##
## EPITECH PROJECT, 2021
## epi_planning
## File description:
## create_user.py
##

from Google import Create_Service

CLIENT_SECRET_FILE = 'code_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

name = input("name : ")
url_intra = input("intra auto login : ")
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES, prefix=name)
with open("all_user.txt", "a") as f:
    f.write(f"{name},{url_intra};")
