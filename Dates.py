import datetime
from datetime import datetime as dt

"""
Brief: Class responsible for each operation on dates.
"""
class Dates:

    list_for_repeats = [1, 3, 7, 14, 30, 90, 180]  # Value for how many days to next repeat.
    actual_date = datetime.date.today()  # Get actual date.

    """
    Brief: Calculate date for next repeat.
    Param: int: number of repeat. Using it to know how many days from list_of_repeat should add to actual date.
    Return: str: date of next repeat in format %d/%m/%y.
    """
    def calculate_date_for_next_repeat(self, number_of_repeat):
        next_repeat = self.actual_date + datetime.timedelta(days=self.list_for_repeats[number_of_repeat])  # Calculate a next date to repeat.
        next_repeat = str(next_repeat.strftime("%d/%m/%y"))  # Convert object datatime to string. It's necessary because program have to save it into .txt file.
        return next_repeat

    """
    Brief: Check if word is to repeat or not.
    Param: str: date of next repeat.
    Return: bool: True - if is to repeat, False - if is not to repeat.
    """
    def is_it_to_repeat(self, date_to_repeat):
        date_r = dt.strptime(date_to_repeat, "%d/%m/%y")  # Get the date of repeat, for current word in this loop circulation

        date_to_repeate = datetime.date(date_r.year, date_r.month, date_r.day)  # Get object datatime for date to repeat.

        # Get delta for year, month and day
        y_delta = self.actual_date.year - date_to_repeate.year
        m_delta = self.actual_date.month - date_to_repeate.month
        d_delta = self.actual_date.day - date_to_repeate.day

        # Mechanism to checking date. If date is today or in past return True, else return False.
        if y_delta > 0:  # If year is bigger return True
            return True

        if m_delta > 0:  # If month is bigger return True
            return True

        if d_delta >= 0:  # If day is bigger or equal to the repeat date, return True
            return True
        elif d_delta < 0:
            return False
