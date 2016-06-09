"""
https://projecteuler.net/problem=6
"""
def sum_squares(end):
	total = 0
	for n in range(1, end + 1):
		total += n**2
	return total


def square_sums(end):
	total = 0
	for n in range(1, end + 1):
		total += n
	return total**2

print(square_sums(100) - sum_squares(100))
