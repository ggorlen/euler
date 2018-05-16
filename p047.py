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
    if is_prime(n):
        return False
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

    
l = [0, 0, 0, 0]
n = 1
while True:
    if has_four_distinct_prime_factors(n):
        l.append(n)
        #l.pop(0)
    if l[-1] - l[-4] == 3:
        print(l[-4])
        break
#    print(l)
    n += 1
