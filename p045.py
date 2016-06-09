"""
https://projecteuler.net/problem=45
"""

t = []
p = []
h = []

count = 0

for n in range(1000000):
	t.append(n * (n + 1) / 2)


for n in range(1000000):
	p.append(n * (3 * n - 1) / 2)


for n in range(1000000):
	h.append(n * (2 * n - 1))

t = set(t)
p = set(p)
h = set(h)

for a in t:
	if a in p:
		if a in h:
			print(a)
