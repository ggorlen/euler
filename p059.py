'''
https://projecteuler.net/problem=59
'''

from requests import get
from sys import exit


# get a set of the 1000 most common english words
url = "https://gist.githubusercontent.com/deekayen/4148741/raw/01c6252ccc5b5fb307c1bb899c95989a8a284616/1-1000.txt"
common_words = set([x.decode("UTF-8") for x in get(url).content.split()])

with open("p059_cipher.txt") as f:
    data = [int(x) for x in f.read().split(",")]

for x in range(97, 123):
    for y in range(97, 123):
        for z in range(97, 123):
            key = [x, y, z]
            decoding = [c ^ key[i%3] for i, c in enumerate(data)] 
            text = "".join([chr(c) for c in decoding]).split()
            count = 0

            for word in text:
                if word in common_words:
                    count += 1  

            if count / len(text) > 0.2:
                print(sum(decoding))
                exit()
