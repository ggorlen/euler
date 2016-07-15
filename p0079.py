"""
https://projecteuler.net/problem=79

A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt, contains fifty successful login attempts.
Given that the three characters are always asked for in hist, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

with open('p079_keylog.txt') as keylog:
    hist = {}
    
    for line in keylog:
        for n in line:
            
            # create histogram of indices
            if n.isdigit() and n in hist:
                hist[n].append(line.index(n))
            elif n.isdigit():
                hist[n] = [line.index(n)]
        
# sort the histogram by average index position
for k, v in sorted(hist.items(), key = lambda x: sum(x[1]) / len(x[1])):
    print(k, end = "")
print()
