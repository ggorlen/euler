"""
https://projecteuler.net/problem=56
"""

def digital_sum(n):
    l = [int(d) for d in str(n)]
    return sum(l)
    
maximum = 0
for a in range(100):
    for b in range(100):
        if maximum < digital_sum(a ** b):
            maximum = digital_sum(a ** b)
            
            
print(maximum)
