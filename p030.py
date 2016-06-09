"""
https://projecteuler.net/problem=30
"""

total = 0

for n in range(2, 1000000):
	candidate = 0

	for i in range(0, len(str(n))):
		candidate += int(str(n)[i]) ** 5
	
	if candidate == n:
		total += candidate

print(total)
