"""
https://projecteuler.net/problem=31

In England the currency is made up of pound, (pound), and pence, p, 
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, (pound)1 (100p) and (pound)2 (200p).
It is possible to make (pound)2 in the following way:

1x(pound)1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can (pound)2 be made using any number of coins?
"""


def memoize(f):
    memo = {}
    def helper(x, y):
        str_y = str(y)
        if (x, str_y) not in memo:
            memo[(x, str_y)] = f(x, y)
        return memo[(x, str_y)]
    return helper
    
@memoize
def make_change(amount, denominations):
    if amount == 0:
        return 1
    if not denominations:
        return 0
        
    current_denom = denominations[-1]
    num_ways = 0    
    count = 0
    while count <= amount:
        num_ways += make_change(amount - count, denominations[:-1])
        count += current_denom
    return num_ways

    
print(make_change(200, [1, 2, 5, 10, 20, 50, 100, 200]))





"""

def make_change(amount, denominations):
    counter = 0
    print(denominations, amount)
    
    if amount == 0:
        return 1
    elif amount < 0:
        return 0

    for denomination in denominations:
        
        while amount // denomination > 0:
            amount -= denomination

        new_denominations = denominations[denominations.index(denomination) + 1:]
        counter += make_change(amount, new_denominations)
    
    return counter

#print(make_change(10, [2,5,3,6]))

print(make_change(200, [200, 100, 50, 20, 10, 5, 2, 1]))


import copy

memo = {}
 
def make_change(amount, denominations, sequence=[]):
    global memo
    
    sequence.sort()
    current_sequence = tuple(sequence)
    
    if amount == 0: # we've made change with the last denomination pick
        if current_sequence not in memo:
            memo[current_sequence] = 1
    elif amount > 0: # not there yet
        for n in denominations:
            new_sequence = copy.deepcopy(sequence)
            new_sequence.append(n)
            memo[current_sequence] = make_change(amount - n, denominations, new_sequence)
    else: # overshot the change
        return 0
        
    return memo[current_sequence]

make_change(200, [200, 100, 50, 20, 10, 5, 2, 1])
total = 0

for k in memo:
    if memo[k] > 0:
        total += 1
print(total - 1)


"""



"""
# https://www.hackerrank.com/challenges/coin-change

import copy

memo = {}

def make_change(amount, denominations, sequence):
    global memo
    
    sequence.sort()
    current_sequence = ",".join([str(x) for x in sequence])

    if current_sequence not in memo:
        if amount == 0:  # sequence is accurate change
            memo[current_sequence] = 1
        elif amount > 0: # haven't finished making change yet, pick another coin
            total_of_subproblems = 0
            for n in denominations:
                new_sequence = copy.deepcopy(sequence)
                new_sequence.append(n)
                
                total_of_subproblems += make_change(amount - n, denominations, new_sequence)
            memo[current_sequence] = total_of_subproblems
        else: # amount < 0.  adding the last coin put us below 0
            return 0    
    return memo[current_sequence]

    
print(make_change(4, [1, 2, 3], []))

total = 0
print("---")
for k in memo:
    if memo[k] > 0:
        print(k + "\t"  + str(memo[k]))
        total += 1
print(total - 1)

"""
