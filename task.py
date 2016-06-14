from datetime import datetime

PERIOD_DAY = 1
PERIOD_WEEK = 2
PERIOD_MON = 4
PERIOD_YEAR = 8


class Task(object):
    def __init__(self):
        self.subject = ""
        self.datetime_start = datetime.now()
        self.datetime_end = datetime.now()
        self.is_day_task = False
        self.period = False
        self.notification = False
        self.content = ""


class PeriodMode(object):
    def __init__(self, mode):
        self.mode = mode


class PeriodModeDay(PeriodMode):
    def __init__(self):
        PeriodMode.__init__(self, PERIOD_DAY)


class PeriodModeWeek(PeriodMode):
    def __init__(self):
        PeriodMode.__init__(self, PERIOD_WEEK)


class PeriodModeMon(PeriodMode):
    def __init__(self):
        PeriodMode.__init__(self, PERIOD_MON)


class PeriodModeYear(PeriodMode):
    def __init__(self):
        PeriodMode.__init__(self, PERIOD_YEAR)


class Period(object):
    def __init__(self):
        self.mode = PERIOD_DAY
        self.cycle = False
        self.datetime_start = datetime.now()
        self.datetime_end = datetime.now()
        self.deadline = False
        self.date_start = datetime.now().date()
        self.date_end = datetime.now().date()
