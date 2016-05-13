"""
https://projecteuler.net/problem=36
"""

total = 0

def is_palindrome(n):
	n = str(n)
	if n == n[::-1]:
		return True
	return False

for n in range(1000000):
	if is_palindrome(n) and is_palindrome(int(bin(n)[2:])):
		total += n

print(total)
