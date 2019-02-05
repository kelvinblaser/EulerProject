# Euler 54 - Poker

# Global Names for Suits
class Suits:
    DIAMONDS = 0
    HEARTS = 1
    CLUBS = 2
    SPADES = 3
    Names = ['Diamonds','Hearts','Clubs','Spades']

# Global Names for Face Cards
class FaceCards:
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    Names = ['','',2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

# Global Names for Poker Hand Ranks
class Ranks:
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9
    Names = ['High Card',
             'One Pair',
             'Two Pairs',
             'Three of a Kind',
             'Straight',
             'Flush',
             'Full House',
             'Four of a Kind',
             'Straight Flush',
             'Royal Flush',
             'Not Poker Hand']

class Card:
    """
    A class for playing cards
    """
    def __init__(self, value = 0, suit = -1):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return (str(FaceCards.Names[self.value]) + ' of ' + Suits.Names[self.suit])

    def __str__(self):
        return (str(FaceCards.Names[self.value]) + ' of ' + Suits.Names[self.suit])

    def __lt__(self, right):
        if self.suit < right.suit:
            return True
        if self.suit == right.suit:
            if self.value < right.value:
                return True
        return False

class HandOfCards:
    """
    A class for a hand of playing cards
    """
    def __init__(self, cards = []):
        """
        Initialization Function:
        cards is a list of cards prepared before hand.
        """
        self.cards = cards
        self.cards.sort()
        self.pokerRank, self.rankCard = self.CalcPokerRank()

    def __repr__(self):
        return self.cards.__repr__() + '\n' + Ranks.Names[self.pokerRank]

    def __str__(self):
        return self.cards.__repr__() + '\n' + Ranks.Names[self.pokerRank]

    def CalcPokerRank(self):
        self.cards.sort()
        if not len(self.cards)==5:
            return -1

        valuesDict = getValuesDict(self)
        valuesList = getValuesList(self)
        
        if isFlush(self):
            if isStraight(self, valuesList):
                if valuesList[0] == 10:
                    return Ranks.ROYAL_FLUSH, [self.cards[0].suit]
                return Ranks.STRAIGHT_FLUSH, [valuesList[0]]
            return Ranks.FLUSH, [valuesList]

        if isStraight(self,valuesList):
            return Ranks.STRAIGHT, [valuesList[0]]

        keys = valuesDict.keys()
        pairCount = 0
        pairs = []
        three = 0
        for key in keys:
            if valuesDict[key] == 4:
                return Ranks.FOUR_OF_A_KIND, [key]
            if valuesDict[key] == 3:
                three = key
            if valuesDict[key] == 2:
                pairCount += 1
                pairs.append(key)
        pairs.sort()
        if three and pairCount:
            return Ranks.FULL_HOUSE, [pairs[0], three]
        if three:
            return Ranks.THREE_OF_A_KIND, [three]
        if pairCount == 2:
            return Ranks.TWO_PAIR, pairs
        if pairCount:
            return Ranks.ONE_PAIR, pairs
        

        '''


        if isRoyalFlush(self):
            return Ranks.ROYAL_FLUSH, self.cards[0].suit
        if isStraightFlush(self):
            return Ranks.STRAIGHT_FLUSH, self.cards[0].value
        
        if isFourOfAKind(self):
            values = getValuesDict(self)
            
            return Ranks.FOUR_OF_A_KIND
        
        if isFullHouse(self):
            return Ranks.FULL_HOUSE
    
        if isFlush(self):
            return Ranks.FLUSH
        if isStraight(self):
            return Ranks.STRAIGHT
        
        if isThreeOfAKind(self):
            return Ranks.THREE_OF_A_KIND
        if isTwoPair(self):
            return Ranks.TWO_PAIR
        if isOnePair(self):
            
            return Ranks.ONE_PAIR
        '''
        return Ranks.HIGH_CARD, [-1]

def isFlush(hand):
    """
    Returns True if the hand is a flush
    """
    suit = hand.cards[0].suit
    for card in hand.cards:
        if not card.suit == suit:
            return False
    return True

def getValuesList(hand):
    values = []
    for card in hand.cards:
        values.append(card.value)
    values.sort()
    return values

def isStraight(hand, values):
    lowValue = values[0]
    for index in range(5):
        if not values[index] == lowValue+index:
            return False
    return True
    
def getValuesDict(hand):
    values = {}
    for card in hand.cards:
        key = card.value
        if not values.has_key(key):
            values[key] = 0
        values[key] += 1
    return values

'''
def isRoyalFlush(hand):
    if (isFlush(hand) and
        hand.cards[0].value==10 and
        isStraight(hand)):
        return True
    return False

def isStraightFlush(hand):
    if isFlush(hand) and isStraight(hand):
        return True
    return False

def isFourOfAKind(hand):
    values = getValuesDict(hand)
    
    for key in values.keys():
        if values[key] == 4:
            return True
    return False

def isFullHouse(hand):
    values = getValuesDict(hand)
    keys = values.keys()
    if (len(keys) == 2 and
        (values[keys[0]] == 2 or
         values[keys[0]] == 3)):
        return True
    return False

def isThreeOfAKind(hand):
    values = getValuesDict(hand)
    for key in values.keys():
        if values[key] == 3:
            return True
    return False

def isTwoPair(hand):
    values = getValuesDict(hand)
    pairCount = 0
    for key in values.keys():
        if values[key] == 2:
            pairCount += 1
    if pairCount == 2:
        return True
    return False

def isOnePair(hand):
    values = getValuesDict(hand)
    for key in values.keys():
        if values[key] == 2:
            return True
    return False
'''    
def convertCardCodes(codes):
    cards = []
    valueDict = {'K': FaceCards.KING,
                 'Q': FaceCards.QUEEN,
                 'J': FaceCards.JACK,
                 'A': FaceCards.ACE,
                 'T': 10}
    for n in range(2,10):
        valueDict[str(n)] = n
    suitDict = {'H': Suits.HEARTS,
                'D': Suits.DIAMONDS,
                'C': Suits.CLUBS,
                'S': Suits.SPADES}
    for code in codes:
        cards.append(Card(valueDict[code[0]],suitDict[code[1]]))
    return HandOfCards(cards)
    
def determineWinner(line):
    cardCodes = line.split()
    # Create the hands
    hand1 = convertCardCodes(cardCodes[:5])
    hand2 = convertCardCodes(cardCodes[5:])
    # Compare Ranks
    if hand1.pokerRank > hand2.pokerRank:
        return 1
    if hand2.pokerRank > hand1.pokerRank:
        return 2
    # If tie, choose hand with highest rank card
    rankCard1 = []
    rankCard2 = []
    rankCard1.extend(hand1.rankCard)
    rankCard2.extend(hand2.rankCard)
    for index in range(len(rankCard1)):
        if rankCard1[index] > rankCard2[index]:
            return 1
        if rankCard1[index] < rankCard2[index]:
            return 2
    # If still a tie, compare highest cards
    values1 = getValuesList(hand1)
    values2 = getValuesList(hand2)
    if values1[-1] > values2[-1]:
        return 1
    if values2[-1] > values1[-1]:
        return 2
    return 0

def countPlayer1Wins(filename):
    winsCount = 0
    tiesCount = 0
    f = open(filename)
    for line in f:
        winner = determineWinner(line)
        if winner == 1:
            winsCount += 1
        if winner == 0:
            tiesCount += 1
    return winsCount, tiesCount

            
