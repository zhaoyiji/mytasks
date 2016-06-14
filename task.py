from datetime import datetime


class Task(object):
    def __init__(self):
        self.subject = ""
        self.datetime_start = datetime.now()
        self.datetime_end = datetime.now()
        self.is_day_task = False
        self.period = False
        self.notification = False
        self.content = ""
