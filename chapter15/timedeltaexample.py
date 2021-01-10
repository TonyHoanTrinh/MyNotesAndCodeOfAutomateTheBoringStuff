import datetime

delta = datetime.timedelta(days = 11, hours = 10, minutes = 9, seconds = 8)
print(delta.days)
print(delta.seconds)
print(delta.microseconds)
print(delta.total_seconds())
print(str(delta))

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days = 1000)
print(dt + thousandDays)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days = 365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))
