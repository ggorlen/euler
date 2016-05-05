"""
https://projecteuler.net/problem=15
"""

grid = 2

routes = 2

for number in range(1, grid * grid):
	if grid % number == 0:
		routes += 2
print(routes)
