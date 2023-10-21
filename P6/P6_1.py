import datetime as dt


d1 = dt.date(2021, 2, 16)
d2 = dt.date(2021, 3, 20)

delta = d2 - d1
print(delta.days)