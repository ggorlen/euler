"""
https://projecteuler.net/problem=92
"""

def num_chain(n):
    count = 0
    total = 0
    for i in range (1, n + 1):
        x = i
        #print(i)
        total = 0
        while total != 89 and total != 1:
            total = 0
            e = len(str(x))
            a = len(str(x)) - 1
            for j in range(0, len(str(x))):
                total += int(str(x)[e - a - 1:e - a]) ** 2
                #print(total)
                a -= 1
            if total == 89:
                count += 1
            x = total
    return count

# TODO: optimize
print(num_chain(10000000))