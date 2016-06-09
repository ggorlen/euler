"""
https://projecteuler.net/problem=40
"""
n = "0."
for a in range(1, 1000001):
  n += str(a)
print(int(n[1 + 1]) * int(n[10 + 1]) * int(n[100 + 1]) * int(n[1000 + 1]) * int(n[10000 + 1]) * int(n[100000 + 1]) * int(n[1000000 + 1]))
