"""
https://projecteuler.net/problem=21
"""

total = 0

for n in range(1, 10001):
	a = 0
	for i in range(1, int(n / 2 + 1)):
		if n % i == 0:
			a += i

	b = 0
	for j in range(1, int(a / 2 + 1)):
		if a % j == 0:
			b += j

	if n == b and a != b:
		total += n


print(total)	
