"""
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called 
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers 
greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math

def is_abundant(n):
    total = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            total += i
            if total > n:
                return True
    return False

def is_sum_of_two_abundants(n):
    for b in abundant_numbers:
        if n - b in abundant_numbers_set:
            return True
        if b > n:
            break
    return False

# generate abundant number list
abundant_numbers = []
for n in range(28123):
    if n % 2 == 0 or n % 3 == 0:
        if is_abundant(n):
            abundant_numbers.append(n)
            
# make a set of abundant numbers for fast lookup
abundant_numbers_set = set(abundant_numbers)

# run totals
total = 0
for n in range(41):
    if not is_sum_of_two_abundants(n):
        total += n
for n in range(41, 28123):
    if not is_sum_of_two_abundants(n):
        total += n
print(total)
