import datetime

current_year = datetime.date.today().year
year = 0
while year < current_year:
    year += 1
    if year % 4 == 0:
        print(year)
    else:
        pass
