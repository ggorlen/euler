"""
https://projecteuler.net/problem=14

**better solution: make a dictionary of previously checked collatz lengths?

"""

largest_collatz = 0

def collatz(n, i):
	if n == 1 or n == 2:
		return i
	i += 1
	if n % 2 == 0:
		return collatz(n // 2, i)
	else:
		return collatz(3 * n + 1, i)

for number in range (999999, 3, -2):
	attempt = collatz(number, 0)
	if attempt > largest_collatz:
		print("new largest: " + str(number) + " taking "  + str(attempt) + " iterations")
		largest_collatz = attempt

print(largest_collatz)
