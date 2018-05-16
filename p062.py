'''
https://projecteuler.net/problem=62
'''

seen = {}
n = 0

while 1:
    cubed = n ** 3
    sorted_digits = tuple(sorted(str(cubed)))

    if sorted_digits in seen:
        seen[sorted_digits].append(cubed)

        if len(seen[sorted_digits]) == 5:
            print(seen[sorted_digits][0])
            break
    else:
        seen[sorted_digits] = [cubed]

    n += 1
