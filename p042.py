"""
https://projecteuler.net/problem=42
"""

triangle_nums = []
for n in range(1, 1000):
	triangle_nums.append(int((1 / 2) * n * (n + 1)))

with open("p042_words.txt", 'r') as temp:
        words = temp.read().strip('"').split('","')

count = 0
for line in words:
	total = 0
	word = list(line)
	for letter in word:
		total += ord(letter) - 64
	if total in triangle_nums:
		count += 1

print(count)
