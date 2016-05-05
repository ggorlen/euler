"""
Largest palindrome product
Problem 4
Published on Friday, 16th November 2001, 06:00 pm; Solved by 292716; Difficulty rating: 5%
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def product_palindrome(lo, hi):
  largest = 0
  for i in range(lo, hi, 1):
    for j in range(lo, hi, 1):
      pal = True
      backwards = str(i * j)[::-1]
      index = 0
      for f in str(i * j):
        if f != backwards[index]:
          pal = False
          break
        index += 1
      if pal == True and (i * j) > largest:
        largest = (i * j)
  return largest

print(product_palindrome(100, 1000))


