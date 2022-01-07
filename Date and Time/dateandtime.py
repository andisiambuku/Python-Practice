# Date and Time module in Python
'''Get the current day, month, year, hour, minute and timestamp from datetime module'''
from datetime import  datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(day,month,year,hour,minute)
print('timestamp',timestamp)
print(f'{day}/{month}/{year},{hour}:{minute}')

'''Format the current date using this format: "%m/%d/%Y, %H:%M:%S")'''
from datetime import date
d = date.today()
print('Current date:',d)
present_day =d.strftime("%m/%d/%Y, %H:%M:%S")
print("today's date:",present_day)


