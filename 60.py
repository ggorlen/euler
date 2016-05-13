"""
https://projecteuler.net/problem=60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
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


def is_prime_concat(a, b):
	return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


primes = []

for i in range(3, 10000, 2):
	if is_prime(i):
		primes.append(i)

for a in primes:
	for b in primes:
		if is_prime_concat(a, b):
			for c in primes:
				if is_prime_concat(a, c) and is_prime_concat(b, c):
					for d in primes:
						if is_prime_concat(d, a) \
						and is_prime_concat(d, b) \
						and is_prime_concat(d, c):
							for e in primes:
								if is_prime_concat(e, a) \
								and is_prime_concat(e, b) \
								and is_prime_concat(e, c) \
								and is_prime_concat(e, d):
										print(a + b + c + d + e)
										sys.exit()

# Needs serious optimization
