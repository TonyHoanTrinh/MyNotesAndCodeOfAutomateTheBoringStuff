#! /usr/bin/env python3

import datetime, time
print(datetime.datetime.now())
dt = datetime.datetime.now()
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

# Comparing times
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(halloween2015 == oct31_2015)
print(halloween2015 > newyear2016)
print(newyear2016 > halloween2015)
print(newyear2016 != oct31_2015)
