'''
https://projecteuler.net/problem=74
'''


factorials = {'0': 1, '1': 1, '2': 2, 
              '3': 6, '4': 24, '5': 120, 
              '6': 720, '7': 5040, 
              '8': 40320, '9': 362880}
fact_sums = {}


def count_fact_repetitions(n, maximum):
    history = set()
    count = 0
    while count <= maximum and n not in history:
        history.add(n)
        try:
            n = fact_sums[n]
        except KeyError:   
            new_n = 0
            for digit in str(n):
                new_n += factorials[digit]
            fact_sums[n] = new_n
            n = new_n
        count += 1
    return count 


chains = 0
for n in range(1000000):
    if count_fact_repetitions(n, 60) == 60:
        chains += 1
print(chains)
