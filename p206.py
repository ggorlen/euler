"""
https://projecteuler.net/problem=206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
"""
import math
import sys
import decimal

decimal.getcontext().prec = 30

for i in range(0, 999999999 + 1, 10):
    i = str(i).rjust(9, '0')
    n = ('1' + i[0] + '2' + i[1] + '3' + i[2] + '4' + i[3] + '5' + \
    i[4] + '6' + i[5] + '7' + i[6] + '8' + i[7] + '9' + i[8] + '0')
    #print(n)
    if decimal.Decimal(int(n)).sqrt() % 1 == 0:
        print(n)
        sys.exit()

# optimize / count backwards.  answer: 1389019170
