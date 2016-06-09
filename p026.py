"""
https://projecteuler.net/problem=26
"""

import decimal

decimal.getcontext().prec = 10000
longest = 0
best = 0

for n in range(7, 1001):
    repeat = []     # Stores the repeat sequence
    candidate = str(decimal.Decimal(1) / decimal.Decimal(n))[2:]
    candidate = [d for d in candidate]

    for digit in candidate:
        if digit not in repeat:
            # Add a new digit to the repeat sequence
            repeat.append(digit) 
      
        elif repeat == candidate[len(repeat) : 2 * len(repeat)]:
            """
            Digit already in our repeat sequence; compare the sequence we've built so far against the next equal
            chunk in the original decimal; if they are the same, see if this repeat length is longer than the best
            and break out of exploring this candidate.
            """
            if longest < len(repeat):
                longest = len(repeat)
                best = n
                break
        
        else:
            # Although this number is in the sequence, our test for end of repeat failed, so add it and keep going.
            repeat.append(digit)

print(best)
