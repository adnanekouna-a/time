import datetime

today = datetime.date.today()
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
        3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
day = today.day
month = today.month
year = today.year
weekday = today.weekday()
letter_month = months[month]
letter_day = days[weekday]

date = f'Today is {letter_day}, {letter_month} the {day}th, {year}!'
print(date)

# TODO add special occasions
