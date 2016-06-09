"""
https://projecteuler.net/problem=50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import sys

def is_prime(n):
    if n == 2 or n ==3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for i in range(5, int((n ** .5) + 1), 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True

primes = []
    
for n in range(1, 1000000, 2):
        if is_prime(n):
            primes.append(n)

best_count = 0
best_number = 0

# Dumb solution but it worked
for j in range(1, len(primes)):
    count = 0
    total = 0
    for i in range(j, len(primes)):
        total += primes[i]
        count += 1
        if total > 1000000:
            total -= primes[i]
            if is_prime(total) and count > best_count:            
                best_count = count
                best_number = total
                print("Total: " + str(total))
                print("Count: " + str(count))
                
print(best_number)
