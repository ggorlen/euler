"""
https://projecteuler.net/problem=35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
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


def shift_digit(n, i):
	return str(n)[-i:] + str(n)[:-i]


def circular_prime(n):
	if is_prime(n):
		s = [d for d in str(n)]
		s = "".join(s)
		for i in range(0, len(s)):
			if not is_prime(int(shift_digit(s, i))):
				return 0
		#print("good: " + str(n))
		return 1
	return 0


count = 1   # added '2' as prime manually
for n in range(1, 1000000, 2):
	count += circular_prime(n)

print(count)



"""
#test shift_digit:
n=197
for i in range(0, len(str(n))):
	print(shift_digit(n, i))
"""

