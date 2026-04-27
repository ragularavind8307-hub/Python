import calendar
x=input()
d=x.split()
w=calendar.weekday(int(d[2]),int(d[0]),int(d[1]))
day=calendar.day_name[w]
print(day.upper())
