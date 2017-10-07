'''
https://projecteuler.net/problem=112
'''


def is_bouncy(n):
    decreasing = True 
    increasing = True

    last_digit = n % 10
    n //= 10

    while n > 0 and (decreasing or increasing):
        curr_digit = n % 10

        if n > 0 and last_digit > curr_digit:
            decreasing = False

        if n > 0 and last_digit < curr_digit:
            increasing = False

        n //= 10
        last_digit = curr_digit
    
    return not decreasing and not increasing


n = 99
bouncy = 0

while 1:
    if is_bouncy(n):
        bouncy += 1

        if bouncy / n >= 0.99:
            print(n)
            break
    n += 1
