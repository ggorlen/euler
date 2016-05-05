"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

one_to_nineteen = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen' }


def word_digit(n):
	s = str(n)
	r = ""
	
	# ones, teens
	if n in one_to_nineteen:
		return one_to_nineteen[n]

	# tens to hundred, post-teens
	if len(s) in [2]:
		if int(s[0]) in [2, 3, 8, 9]:
			r += "twenty"
		elif int(s[0]) in [4, 5, 6]:
			r += "fifty"
		elif int(s[0]) == 7:
			r += "seventy"
		
		if int(s[1]) in [1, 2, 6]:
			r += "one"
		elif int(s[1]) in [3, 7, 8]:
			r += "three"
		elif int(s[1]) in [4, 5, 9]:
			r += "four"

	if len(s) in [3]:
		if int(s[1:3]) in one_to_nineteen:
			r += one_to_nineteen[int(s[1:3])]
		else:
	
			if int(s[1]) in [2, 3, 8, 9]:
				r += "twenty"
			elif int(s[1]) in [4, 5, 6]:
				r += "fifty"
			elif int(s[1]) == 7:
				r += "seventy"
			
			if int(s[2]) in [1, 2, 6]:
				r += "one"
			elif int(s[2]) in [3, 7, 8]:
				r += "three"
			elif int(s[2]) in [4, 5, 9]:
				r += "four"
		
	# hundreds
	if n in [100, 200, 600]:
		return "onehundred"
	elif n in [300, 700, 800]:
		return "threehundred"
	elif n in [400, 500, 900]:
		return "fourhundred"
	
	if len(s) == 3:
		if int(s[0]) in [1, 2, 6]:
			r += "onehundredand"
		elif int(s[0]) in [3, 7, 8]:
			r += "threehundredand"
		elif int(s[0]) in [4, 5, 9]:
			r += "fourhundredand"
	
	# thousands, unfinished
	if len(s) == 4:
		r += "onethousand"
	
	#print(s + " " + r)
	return r


f = ""
for number in range(1, 1001):
	f += word_digit(number)

print(len(f))


