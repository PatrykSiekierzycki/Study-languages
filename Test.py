import datetime
from datetime import datetime as dt



def is_it_to_repeat(date_to_repeat, actual_date):
    date_r = dt.strptime(date_to_repeat, "%d/%m/%y")  # Get the date of repeat.
    date_to_repeate = datetime.date(date_r.year, date_r.month, date_r.day)  # Get object datatime from date to repeat.

    # Get delta for year, month and day
    y_delta = actual_date.year - date_to_repeate.year
    m_delta = actual_date.month - date_to_repeate.month
    d_delta = actual_date.day - date_to_repeate.day


    subt = datetime.timedelta(days=date_to_repeate.day)
    difference = datetime.datetime.today

    return difference

    """
    date_to_repeate = datetime.date(date_r.year, date_r.month, date_r.day)  # Get object datatime for date to repeat.

    # Get delta for year, month and day
    y_delta = actual_date.year - date_to_repeate.year
    m_delta = actual_date.month - date_to_repeate.month
    d_delta = actual_date.day - date_to_repeate.day

    # Mechanism to checking date. If date is today or in past return True, else return False.
    year = False
    month = False

    if y_delta > 0:
        year = True
    elif y_delta == 0:
        year = False

    if m_delta > 0:
        month = True
    elif m_delta < 0 and year is True:
        month = True
    elif m_delta <= 0 and year is False:
        month = False

    if d_delta >= 0:
        return True
    elif d_delta < 0 and (month is True or year is True):
        return True
    else:
        return False

"""
while True:
    actual_date = datetime.date.today()

    print("actual date as days", actual_date)
    d = str(input("Data: "))
    print(is_it_to_repeat(d, actual_date))