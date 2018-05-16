"""
https://projecteuler.net/problem=52
"""
for n in range(1, 1000000):
  t = [int(x) for x in str(n)]
  r = [int(x) for x in str(n * 2)]
  t.sort()
  r.sort()
  if t == r:
    r = [int(x) for x in str(n * 3)]
    r.sort()
    if t == r:
      r = [int(x) for x in str(n * 4)]
      r.sort()
      if t == r:
        r = [int(x) for x in str(n * 5)]
        r.sort()
        if t == r:
          r = [int(x) for x in str(n * 6)]
          r.sort()
          if t == r:
            print(n)