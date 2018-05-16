"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(n):
  t = 1
  for i in range(1, n + 1):
    t *= i
  return t

total = 0
for i in range(3, 1000000):
  sum = 0
  for n in range(0, len(str(i))):
    sum += factorial(int(str(i)[n]))
  if sum == i:
    total += i

print(total)