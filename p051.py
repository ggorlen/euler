import math
import sys


def sieve(n):
    nums = [False, False] + [True for x in range(1, n)]
    nums_len = len(nums)

    sqrt_n = math.floor(n ** 0.5)

    for i in range(2, sqrt_n):
        if nums[i]:
            for j in range(i * i, nums_len, i):
                nums[j] = False

    return nums


prime_list = [tuple([int(x) for x in str(i)]) for i, v in enumerate(sieve(999999)) if v]
primes = set(prime_list)

for prime in prime_list:
    for target_digit in prime:
        matches = []

        for n in range(10):
            cpy = list(prime)

            for i, cpy_digit in enumerate(cpy):
                if target_digit == cpy_digit:
                    cpy[i] = n

            if tuple(cpy) in primes:
                matches.append(cpy)
        
        if len(matches) == 8:
            print("".join([str(x) for x in matches[0]]))
            sys.exit()
