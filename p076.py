'''
https://projecteuler.net/problem=76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''


def memoize(f):
    memo = {}
    def helper(x, y):
        if (x, y) not in memo:
            memo[(x, y)] = f(x, y)
        return memo[(x, y)]
    return helper
    
@memoize
def count_ways(n, current_digit):
    if n == 0:
        return 1
    if current_digit <= 0:
        return 0

    num_ways = 0
    for i in range(0, n+1, current_digit):
        num_ways += count_ways(n - i, current_digit - 1)
    return num_ways

print(count_ways(100, 99))
