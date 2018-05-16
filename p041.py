"""
https://projecteuler.net/problem=41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
import itertools

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

l = [1,2,3,4,5,6,7]
l = list(itertools.permutations(l))

for n in l:
    if is_prime(int(str(n[0]) + str(n[1]) + str(n[2]) + str(n[3]) + str(n[4]) + str(n[5]) + str(n[6]))):
        print(int(str(n[0]) + str(n[1]) + str(n[2]) + str(n[3]) + str(n[4]) + str(n[5]) + str(n[6])))


# Things that didn't work:
        
"""
def is_pandigital(n):
    l = [int(x) for x in str(n)]
    l.sort()
    if list(set(l)) == l:
        for i in range(1, len(str(n)) + 1):
            if i not in l:
                return False
        return True
    return False

def shift_digit(n, i):
	return str(n)[-i:] + str(n)[:-i]

    
n = 123456789
i = 0
counter = 0
while True:
    print(n)
    print(i)
    if is_prime(n):
        print(n)
    n = int(shift_digit(n, i))
    if counter % len(str(n)):
        n = int(str(n)[::-1])
    if counter == len(str(n)) - 1:
        counter = 0
    i += 1
    if i == len(str(n)):
        i = 0
    
""" 

