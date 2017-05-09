"""
This file was written Rebecca Hanlon.

"""
import os
import requests

response = requests.get('http://or.water.usgs.gov/non-usgs/bes/')

class RainStation:

    def __init__(self, date: str, total: str, hours: list):




class RainDay:

    def __init__(self, date: str, total: str, hours: list):
        self.data = date
        self.total = int(total)
        self.hours = [int(h) for h in hours]


    def __repr__(self):

        message = "{} Total: {}".format(self.date, self.total)
        return message

    def max_hour(self):
        hour, value = max(enumerate(rain), key=lambda t: t[1])
        return hour

