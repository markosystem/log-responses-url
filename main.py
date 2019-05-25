import requests
from urls import sites
from model.log import Log
import datetime


class Main:
    def __init__(self):
        t = Log()
        for s in sites:
            t.date = datetime.datetime.now()
            t.url = s
            t.status = requests.get(s).status_code
            print(t)


Main()
