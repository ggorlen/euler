'''
https://projecteuler.net/problem=99

reference:
https://www.rookieslab.com/posts/fast-power-algorithm-exponentiation-by-squaring-cpp-python-implementation

'''


def pow(base, power):
    
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = result * base

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = base * base

    return result
    
with open("p099_base_exp.txt") as f:
    largest_number = 0
    largest_line = 0
    i = 0

    for line in f:
        base, exp = [int(x) for x in line.split(',')]
        result = pow(base, exp)
        print(result)

        if result > largest_number:
            largest_number = result
            largest_line = i

        i += 1

    print(largest_line)
