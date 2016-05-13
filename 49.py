"""
https://projecteuler.net/problem=49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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


for a in range(1001, 10000, 2):
	if is_prime(a):
		for b in range(a + 2, 10000, 2):
			if is_prime(b):
				c = b - a + b
				if is_prime(c):
					if "".join(sorted(str(a))) == \
					   "".join(sorted(str(b))) == \
					   "".join(sorted(str(c))):
						print(str(a) + " " + str(b) + " " + str(c))
						print()
