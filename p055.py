'''
https://projecteuler.net/problem=55
'''


def count_palindrome(n):
    count = 0
    s = str(n)
    while count < 50:
        count += 1
        n += int(s[::-1])
        s = str(n)
        if s == s[::-1]:
            return count
    return -1


total = 0
for n in range(10000):
    if count_palindrome(n) < 0:
        total += 1
print(total)
