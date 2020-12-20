import datetime

print('Hi!')
print('Enter the dates [DD/MM/YYYY]!')

date1 = input('Date 1: ')
date2 = input('Date 2: ')

year1 = int(date1[6:])
month1 = int(date1[3:5])
day1 = int(date1[:2])

year2 = int(date2[6:])
month2 = int(date2[3:5])
day2 = int(date2[:2])

date1 = datetime.date(year1, month1, day1)
date2 = datetime.date(year2, month2, day2)

duration = abs(date1 - date2)
print(duration)
