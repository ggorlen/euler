"""
https://projecteuler.net/problem=47
http://stackoverflow.com/questions/18198318/in-project-euler-47-why-is-22-considered-a-prime-number-distinct-from-2
"""
"""

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


def has_distinct_prime_factors(n, num_distinct):
    prime_factors = []
    for a in range(2, 11):
        if n % a == 0 and is_prime(a) and a not in prime_factors:
            prime_factors.append(a)
    for a in range(11, int(n / 2) + 7, 2):
        if n % a == 0 and is_prime(a) and a not in prime_factors:
            prime_factors.append(a)
            if len(prime_factors) == num_distinct:
                return True
    return False

num_distinct = 3
n = 0
count = 0
while True:
    if has_distinct_prime_factors(n, num_distinct):
        consecutive = []
        for i in range(n - num_distinct, n + num_distinct + 1):
            #print(i)
            if has_distinct_prime_factors(i, num_distinct):
                consecutive.append(i)
        #print("----")
        if len(consecutive) == num_distinct:
            print(consecutive)
            count += 1
            if count > 1:
                break
    n += num_distinct
"""

"""
https://projecteuler.net/problem=47
http://stackoverflow.com/questions/18198318/in-project-euler-47-why-is-22-considered-a-prime-number-distinct-from-2
"""

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

# Needs serious optimization
def has_four_distinct_prime_factors(n):
    prime_factors = []
    for a in range(1, 11):
        if n % a == 0 and is_prime(a):
            prime_factors.append(a)
    for a in range(11, int(n / 2) + 1, 2):
        if n % a == 0 and is_prime(a):
            prime_factors.append(a)
            if len(set(prime_factors)) > 4:
                return False
    if len(set(prime_factors)) == 4:
        return True
    return False

    
n = 1
while True:
    if has_four_distinct_prime_factors(n) \
        and has_four_distinct_prime_factors(n + 1) \
        and has_four_distinct_prime_factors(n + 2) \
        and has_four_distinct_prime_factors(n + 3):
        print(n)
        break
    n += 1
