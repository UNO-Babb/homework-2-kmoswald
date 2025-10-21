import datetime

now = datetime.datetime.now()
print(now) 
print(now.hour)
print(now.hour - 5)
currentHour = (now.hour - 5) % 24
print(currentHour)