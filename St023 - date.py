"""
    for tests
"""
import datetime

y, m, d = map(int, input().split())
td = datetime.timedelta(days=int(input()))

d1 = datetime.date(y, m, d) + td

print(d1.year, d1.month, d1.day)

