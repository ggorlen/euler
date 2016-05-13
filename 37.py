"""
https://projecteuler.net/problem=37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def is_prime(n):
    if n == 2 or n ==3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for i in range(5, int((n ** .5) + 1), 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True


def is_truncatable_prime(n):
	if is_prime(n):
		s = str(n)
		for i in range(0, len(s)):
			if not is_prime(int(s[i:])) \
			or not is_prime(int(s[:i + 1])):
				return 0
		print(n)
		return n
	return 0

count = 0
total = 0
n = 5
while count < 11:
	n += 2
	total += is_truncatable_prime(n)

print(total)

# needs optimizing badly
