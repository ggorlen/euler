
"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def primes(target):
	counter = 3
	primes = 1
	while(True):
		print(primes)
		is_prime = True
		for n in range(3, counter, 2):
			if counter % n == 0:
				is_prime = False
				break
		if is_prime == True:
			primes += 1
		if primes == target:
			return counter
		else:
			counter += 2

print(primes(10001))


