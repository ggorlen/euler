"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""


with open("p022_names.txt", 'r') as temp:
	names = temp.read().strip('"').split('","')

#names = [s.strip('"') for s in names]

names.sort()

position = 0
total = 0

for name in names:
	position += 1
	name_total = 0
	
	for letter in name:
		name_total += (ord(letter) - 64)
	total += name_total * position

print(total)
