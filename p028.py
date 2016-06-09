"""
https://projecteuler.net/problem=28
"""

total = 1
corner_number = 0
corner_value = 1
side_length = 3
step = 2

while (True):
	corner_number += 1
	corner_value += step
	total += corner_value
	if corner_number == 4:
		corner_number = 0
		step += 2
		side_length += 2
	print(str(corner_value) + " " + str(side_length))
	if side_length == 1003:
		break

print(total)
