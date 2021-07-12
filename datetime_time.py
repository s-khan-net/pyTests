from datetime import datetime, timedelta
import time

dt1 = datetime(2020, 7, 1)
print(dt1.__str__(), dt1)
dt2 = datetime.now()
print(dt2)
print(dt1 > dt2)
# timedelta object
duration = dt2 - dt1
print(duration)  # duration is represented as days:hrs:min:sec:milsec
print("seconds -> duration time to secs", duration.seconds)
print("total_seconds ->  complete duration to secs", duration.total_seconds())
dt1 = datetime(2020, 7, 1) + timedelta(days=1, minutes=10, seconds=23)
print("adding time delta", dt1)

dtparsed = datetime.strptime('2020/3/3', '%Y/%m/%d')
print("parsed time", dtparsed)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

dtstr = datetime.strftime(datetime.now(), '%Y/%m')
print(dtstr)

print(time.time, time.time())
dttimest = datetime.fromtimestamp(time.time())
print(dttimest)
print(f"{dttimest.year} / {dttimest.month} / {dttimest.day}")
print(dttimest.strftime("%Y / %m / %d"))
