"""
https://projecteuler.net/problem=27
"""

# http://stackoverflow.com/questions/15285534/isprime-function-for-python-language

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

max_product = 0
best_count = 0
prime_count = 0

for i in range(-1001, 1001):
    for j in range(0, 1001):
        prime_count = 0
        for n in range(0, 1000):
            if is_prime(n ** 2 + n * i + j):
                prime_count += 1
            else:
                break
        if prime_count > best_count:
            best_count = prime_count
            max_product = i * j
            print(best_count)


print(max_product)
