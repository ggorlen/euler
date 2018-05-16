n! means n x (n − 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

digits = 1
for i in range(1, 100):
  digits = digits * i
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print(sum_digits(digits))
# http://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python