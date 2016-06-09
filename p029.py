"""
https://projecteuler.net/problem=29
"""

uniques = []

for a in range(2, 101):
	for b in range(2, 101):
		if a**b not in uniques:
			uniques.append(a**b)

print(len(uniques))
