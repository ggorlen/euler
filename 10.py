"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million
"""
from math import sqrt
def sum_primes(end):
	sum = 1
	for n in range(1, end + 1, 2):
		prime = True
		for x in range(3, int(sqrt(n)) + 1, 2):
			if n % x == 0:
				prime = False
				break
		if prime == True:
			sum += n
	return sum

print(sum_primes(2000000))
