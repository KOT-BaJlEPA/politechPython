import sched
import calendar
import time
import datetime

date1 = datetime.date.today()
day = date1.day
last_day = calendar.monthrange(date1.year, date1.month)[1]
print(last_day)
print(day)

def crete_Report():
    print("create report")


def monthly_report():
    date1 = datetime.date.today()
    if date1.day == 1:
        crete_Report()




monthly_report()
