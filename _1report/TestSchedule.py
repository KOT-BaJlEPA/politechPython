
import calendar
import datetime


def get_dateFromTo():
    date1 = datetime.date.today()
    day_from = 1
    year = None
    c_month = None
    day_to = None
    if date1.month == 1:
        year = date1.year-1
        c_month = 12
        day_to = 31
    else:
        year = date1.year
        c_month = date1.month - 1
        day_to = calendar.monthrange(date1.year, date1.month - 1)[1]
    date_from = date1.replace(year= year, month=c_month, day=day_from)
    date_to = date1.replace(year= year, month=c_month, day=day_to)
    return [date_from, date_to]












#
# def crete_Report():
#     print("create report")
#
#
# def monthly_report():
#     date1 = datetime.date.today()
#     if date1.day == 1:
#         crete_Report()
#
#
#
#
# monthly_report()
