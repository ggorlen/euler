"""
Largest prime factor
Problem 3
Published on Friday, 2nd November 2001, 06:00 pm; Solved by 325562; Difficulty rating: 5%
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

def largest_prime_factor(number):
  for n in range(int(sqrt(number)) + 1, 3, -1):
    if number % n == 0:
      prime = True
      for p in range(3, n, 2):
        if n % p == 0:
          prime = False
          break
      if prime == True:
        return n
  return -1

#print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
