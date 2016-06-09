"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def smallest_divisible(start, end):
	c = end**2
	while(True):
		divisible = True
		for n in range(start, end + 1):
			if c % n != 0:
				divisible = False
				c += end
				break
		if divisible == True:
			return(c)
		else:
			#print(c)
			c += end

print(smallest_divisible(1, 20))
