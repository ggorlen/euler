'''
https://projecteuler.net/problem=84
'''

import random


squares = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", 
         "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", 
         "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", 
         "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", 
         "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

board = {e:i for i, e in enumerate(squares)}

frequency = {x:0 for x in squares}

cc = [board[x] for x in ["GO", "JAIL"]] + [None] * 14

chance = [board[x] for x in ["GO", "JAIL", "C1", "E3", "H2", "R1"]] + \
         [ "R", "R", "U", "BACK 3"] + [None] * 6

random.shuffle(chance)
random.shuffle(cc)

location = 0
consecutive_doubles = 0

dice_sides = 4
rolls = 1000000

for _ in range(rolls):
    die_1 = random.randint(1, dice_sides)
    die_2 = random.randint(1, dice_sides)

    if die_1 == die_2:
        consecutive_doubles += 1
    else: 
        consecutive_doubles = 0
        
    if consecutive_doubles == 3:
        location = board["JAIL"]
    else:
        location = (location + die_1 + die_2) % len(squares)

        if location == board["G2J"]:
            location = board["JAIL"]
        elif squares[location][:2] == "CH":
            card = chance.pop(0)
            
            if card != None:
                if card == "BACK 3":
                    location -= 3
                elif str(card) == card and len(card) == 1:
                    while squares[location][0] != card:
                        location = (location + 1) % len(squares)
                else:
                    location = card

            chance.append(card)
        elif squares[location][:2] == "CC":   
            card = cc.pop(0)

            if card != None:
                location = card

            cc.append(card)

    frequency[squares[location]] += 1

for x in sorted([(k, frequency[k] / rolls) for k in frequency], key=lambda x: -x[1])[:3]:
    print(str(board[x[0]]).zfill(2), end="")
