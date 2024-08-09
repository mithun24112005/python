import holidays
from datetime import date

# for day,name in sorted(holidays.India(years=2024,state='KA').items()):
#     print(day,name)

# check weather a given date is a holiday or not

in_holidays=holidays.India()
print('01-01-2024' in in_holidays)
print( in_holidays.get('01-01-2024'))

