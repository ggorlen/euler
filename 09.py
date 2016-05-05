"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pyth_trip(n):
	for a in range(n - 100):
		for b in range(n - 100):
			for c in range(n - 100):
				if (a + b + c == n) and (a < b < c) and (a**2 + b**2 == c**2):
					return a * b * c
print(pyth_trip(1000))
