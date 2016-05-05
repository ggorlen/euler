"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

https://projecteuler.net/problem=19
"""

months = { 1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }

days = [ 1, 2, 3, 4, 5, 6, 7 ]

count = 0

day = 2

leap = False

for y in range(1901, 2001):
	leap = False
	if y % 4 == 0 and y % 100 != 0:
		leap = True
	elif y % 100 == 0 and y % 400 == 0:
		leap = True
	
	for m in months:
		current_month = months.get(m)
		if current_month == 28 and leap:
			current_month += 1

		for d in range(1, current_month + 1):
			if days[day] == 1 and d == 1:
				count += 1
			if day == 6:
				day = 0
			else:
				day += 1

print(count)



