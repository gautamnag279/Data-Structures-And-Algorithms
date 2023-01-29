import calendar
month, day, year = map(int, input().split())
ans = calendar.day_name[calendar.weekday(year, month, day)].upper()
print(ans)
