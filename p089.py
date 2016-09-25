"""
https://projecteuler.net/problem=89

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most 
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in 
valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

"""

DENOMINATIONS = {
    'I' : 1, 
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def numeral_to_int(numeral):
    # iterates through numeral and separates each number, adds up total and returns an integer
    
    value = []
    num = list(numeral.strip())
    i = 0
    
    while i < len(num):
        first = DENOMINATIONS.get(num[i])
        try:
            second = DENOMINATIONS.get(num[i + 1])
            if (first < second):
                value.append(second - first)
                i += 2
            else:
                value.append(first)
                i += 1
        except IndexError:
            value.append(first)
            i += 1
    
    return sum(value)
    
    
def make_numeral(number):
    # generates a roman numeral from a given number

    result = ""
    n = str(number)[::-1]
    
    if len(n) > 0:
        if n[0] == "1":
            result += "I"
        elif n[0] == "2":
            result += "II"
        elif n[0] == "3":
            result += "III"
        elif n[0] == "4":
            result += "IV"
        elif n[0] == "5":
            result += "V"
        elif n[0] == "6":
            result += "VI"
        elif n[0] == "7":
            result += "VII"
        elif n[0] == "8":
            result += "VIII"
        elif n[0] == "9":
            result += "IX"
        
    if len(n) > 1:
        if n[1] == "1":
            result = "X" + result        
        elif n[1] == "2":
            result = "XX" + result        
        elif n[1] == "3":
            result = "XXX" + result        
        elif n[1] == "4":
            result = "XL" + result
        elif n[1] == "5":
            result = "L" + result
        elif n[1] == "6":
            result = "LX" + result
        elif n[1] == "7":
            result = "LXX" + result
        elif n[1] == "8":
            result = "LXXX" + result
        elif n[1] == "9":
            result = "XC" + result

    if len(n) > 2:
        if n[2] == "1":
            result = "C" + result
        elif n[2] == "2":
            result = "CC" + result
        elif n[2] == "3":
            result = "CCC" + result
        elif n[2] == "4":
            result = "CD" + result
        elif n[2] == "5":
            result = "D" + result
        elif n[2] == "6":
            result = "DC" + result
        elif n[2] == "7":
            result = "DCC" + result
        elif n[2] == "8":
            result = "DCCC" + result
        elif n[2] == "9":
            result = "CM" + result

    if len(n) > 3:
        result += "M" * int(n[3:])
            
    return result
    
    
savings = 0
with open("p089_roman.txt", 'r') as file:
    for line in file:
        savings += len(line.strip()) - len(make_numeral(numeral_to_int(line)))
print(savings)

