from datetime import datetime, date, time, timedelta


# simple examples
date_today = date.today()
print(date_today)

datetime_now = datetime.now()
print(datetime_now)


# Constructors
"""date(year, month, day)
   time([hour],[min],[sec],[micro])
   datetime(year, month, day,[hour],[min],[sec],[micro])"""

halloween = date(year=2024, month=10, day=31)
print('\n', halloween)
print(type(halloween))

meeting = time(hour=14, minute=30)
print('\n', meeting)
print(type(meeting))

appointment = datetime(year=2024, month=10, day=28, hour=14, minute=30)
print('\n', appointment)
print(type(appointment))


appointment = datetime(year=2024, month=10, day=28, hour=14, minute=30, second=48)
print('\n', appointment)
print(type(appointment))

print(halloween.day)
print(halloween.month)
print(halloween.year)
print()
print(appointment.hour)
print(appointment.minute)
print(appointment.second)
print()

halloween = '10/31/2024'
american_halloween = datetime.strptime(halloween, '%m/%d/%Y')
print(american_halloween)
print()
halloween = '10/31/2024 22:30'
american_halloween = datetime.strptime(halloween, '%m/%d/%Y %H:%M')
print(american_halloween)
print()
halloween = '10/31/2024 22:48'
american_halloween = datetime.strptime(halloween, '%m/%d/%Y %H:%M')
print(f'{american_halloween: %B %d, %I:%M %p}')
print()
print(f'{american_halloween: %c}')
print()
custom_format = '%m*%d-%Y'
print(f'{american_halloween: {custom_format}}')

timedelta_example = american_halloween - appointment
print()
print(timedelta_example)
"""Constructor for time delta
timedelta([days] [,seconds] [,microseconds] [,milliseconds] [,minutes] [,hours] [,months] [,weeks])
"""
time_span = timedelta(weeks=2, days=3, hours=4, minutes=5)
print(time_span)
print()
three_weeks_ago = datetime.now() - timedelta(weeks=3)
print(three_weeks_ago)
print()