'''
https://projecteuler.net/problem=69
'''


### UNSOLVED ###


def phi_even(n):
    count = 1
    for i in range(1, n, 2):
        if n % i != 0:
            print('   ' + str(i))
            count += 1
    return count
    
    
best = 0

for x in range(6, 200, 6):
    p = x / phi_even(x)
    print('x: ' + str(x) + ' p: ' + str(p))
    #    best = p
#print(best)
