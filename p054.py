"""
https://projecteuler.net/problem=54
"""


class Card:
    """
    Represents a playing card.
    """
    
    def __init__(self, raw):
        self.rank = int(raw[0:2])
        self.suit = raw[2] 
        
    def __repr__(self):
        return str(self.rank) + " " + self.suit

    def __eq__(self, other):
        return self.rank == other.rank

        
def high_card(hand):
    """
    Highest value card in a pre-sorted hand.
    """
    
    return hand[-1].rank

def one_pair(hand):
    """
    Two cards of the same value.
    """
 
    for i in range(len(hand)):
        for j in range(i, len(hand)):
            if hand[i] == hand[j] and i != j:
                return hand[i].rank
    return False
    
def two_pairs(hand):
    """
    Two different pairs.
    """
 
    pairs = []
    for i in range(len(hand)):
        for j in range(i, len(hand)):
            if hand[i] == hand[j] and i != j and hand[i] not in pairs:
                pairs.append(hand[i])
                if len(pairs) == 2:
                    return hand[i].rank
    return False
    
def three_of_a_kind(hand):
    """
    Three cards of the same value.
    """
 
    for i in range(len(hand)):
        counter = 1
        for j in range(i, len(hand)):
            if hand[i] == hand[j] and i != j:
                counter += 1
                if counter == 3:
                    return hand[i].rank
    return False
    
def straight(hand):
    """
    All cards are consecutive values.  Requires sorted input list.
    """
    
    previous_card = hand[0]
    for card in hand[1:]:
        if card.rank != previous_card.rank + 1:
            return False
        previous_card = card
    
    return hand[-1]

def flush(hand):
    """
    All cards of the same suit.
    """

    for card in hand[1:]:
        if card.suit != hand[0].suit:
            return False
    return hand[-1]
    
def full_house(hand):
    """
    Three of a kind and a pair.
    """

    three_test = three_of_a_kind(hand)
    one_pair_test = one_pair(hand)
    if three_test is not False and one_pair_test is not False and three_test != one_pair_test:
        return three_test
    return False
    
def four_of_a_kind(hand):
    """
    Four cards of the same value.
    """
    
    for i in range(len(hand)):
        counter = 1
        for j in range(i, len(hand)):
            if hand[i] == hand[j] and i != j:
                counter += 1
                if counter == 4:
                    return hand[i].rank
    return False
    
def straight_flush(hand):
    """
    All cards are consecutive values of same suit.  Requires sorted input.
    """
    
    if straight(hand) and flush(hand):
        return hand[-1]
    
def royal_flush(hand):
    """
    Ten, Jack, Queen, King, Ace, in same suit.  Requires sorted input.
    """
    
    return hand[0].rank == 10 and straight_flush(hand)
    
def sort_hand(hand):
    """
    Converts strings to Cards and returns a sorted hand
    """
    
    new_hand = []
    
    for i in range(len(hand)):
        hand[i] = hand[i].replace("T", "10")
        hand[i] = hand[i].replace("J", "11")
        hand[i] = hand[i].replace("Q", "12")
        hand[i] = hand[i].replace("K", "13")
        hand[i] = hand[i].replace("A", "14")
        hand[i] = hand[i].zfill(3)
        
    hand.sort()

    for card in hand:
        new_card = Card(card)
        new_hand.append(new_card)
     
    return new_hand
    
def evaluate(hand):
    """
    Determines the value of a poker hand
    """

    if royal_flush(hand):
        return (9, royal_flush(hand))
    elif straight_flush(hand):
        return (9, straight_flush(hand))
    elif four_of_a_kind(hand):
        return (7, four_of_a_kind(hand))
    elif full_house(hand):
        return (6, full_house(hand))
    elif flush(hand):
        return (5, flush(hand))
    elif straight(hand):
        return (4, straight(hand))
    elif three_of_a_kind(hand) is not False:
        return (3, three_of_a_kind(hand))
    elif two_pairs(hand):
        return (2, two_pairs(hand))
    elif one_pair(hand):
        return (1, one_pair(hand))
    else:
        return (0, high_card(hand))

def play_hand(hands):
    """
    Determines winner given iterable of legal poker hands
    """
    
    scores = []
    
    for i in range(len(hands)):
        scores.append(evaluate(hands[i]))

    winner = scores.index(max([score for score in scores]))
    
    for i in range(len(scores)):
        for j in range(i, len(scores)):
            if i != j and scores[i] == scores[j]:
                winner = break_tie(hands[i], hands[j])
    
    return winner
    
def break_tie(hand1, hand2):
    """
    Determines winner of two pre-sorted tied hands
    """

    for i in range(len(hand1) - 1, 0, -1):
        if hand1[i].rank > hand2[i].rank:
            return 0
        elif hand1[i].rank < hand2[i].rank:
            return 1
            
    return -1
    
def main():
    win_counter = 0
    loss_counter = 0

    with open("p054_poker.txt") as file:
        for line in file:
            if play_hand((sort_hand(line.split()[0:5]), sort_hand(line.split()[5:10]))) == 0:
                win_counter += 1
            else:
                loss_counter += 1
            
        print(win_counter)
        print(loss_counter)
            
if __name__ == "__main__":
    main()