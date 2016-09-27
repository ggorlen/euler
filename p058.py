def is_prime(n):
    if n == 2 or n ==3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for i in range(5, int((n ** .5) + 1), 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True

    
diagonals = []
temp = []
increase = 0
step = 0
n = 1
length = -1
ratio = [0, 0]

while True:
  diagonals.append(n)
  temp.append(n)

  n += step
  increase += 1
  if increase % 4 == 1:
    increase = 1
    length += 2
    step += 2
    
    count = 0
    for k in temp:
      if is_prime(k):
        count += 1
		
    ratio = [ratio[0] + count, ratio[1] + len(temp)]
    temp = []

    if ratio[0] / ratio[1] < .1 and step > 2:
      print(length)
      break
