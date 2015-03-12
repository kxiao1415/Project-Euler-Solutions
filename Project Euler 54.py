#project euler 54
#compare two poker hands

def isFlush(hand):
    a = []
    for card in hand:
        a.append(card[-1])
        
    return len(set(a)) == 1

def isStraight(hand):
    a = noSuitHand(hand)
    
    return a[1] == a [0] + 1 and \
           a[2] == a[1] + 1 and \
           a[3] == a[2] + 1 and \
           a[4] ==  a[3] + 1

def isFourOfaKind(hand):
    dl = handToDict(hand)
    count = []
    for card in dl:
        count.append(dl[card])
    count.sort()
    
    return count == [1, 4]

def FullHouse(hand):
    dl = handToDict(hand)
    count = []
    for card in dl:
        count.append(dl[card])
    count.sort()

    return count == [2, 3]

def ThreeOfaKind(hand):
    dl = handToDict(hand)
    count = []
    for card in dl:
        count.append(dl[card])
    count.sort()

    return count == [1, 1, 3]


def twoPairs(hand):
    dl = handToDict(hand)
    count = []
    for card in dl:
        count.append(dl[card])
    count.sort()

    return count == [1, 2, 2]

def onePair(hand):
    dl = handToDict(hand)
    count = []
    for card in dl:
        count.append(dl[card])
    count.sort()
    
    return count == [1, 1, 1, 2]

def handToDict(hand):
    dl = {}
    for card in hand:
        if card[:-1] in dl:
            dl[card[:-1]] += 1
        else:
            dl[card[:-1]] = 1
    return dl

def noSuitHand(hand):
    a = []
    for card in hand:
        a.append(int(card[:-1]))
    a.sort()
    
    return a

def rank(hand):
    
    if isFlush(hand) and isStraight(hand):
        a = noSuitHand(hand)
        if a[0] == 10:
            #Royal Flush, win!
            return [10]
        else:
            #Straight Flush, returns [rank, smallest card]
            return [9, a[0]]
        
    elif isFourOfaKind(hand):
        handValue = [8, 0]
        
        dl = handToDict(hand)
        for i in dl:
            if dl[i] == 4:
                handValue[1] = i
        #Four of a Kind, returns [rank, the card]
        return handValue

    elif FullHouse(hand):
        handValue = [7, 0]

        dl = handToDict(hand)
        for i in dl:
            if dl[i] == 3:
                handValue[1] = i
        #FullHouse, returns [rank, the card]
        return handValue

    elif isFlush(hand):
        a = noSuitHand(hand)
        a = sorted(a, reverse = True)
        a.insert(0, 6)
        #Flush, returns [rank, high to low]
        return a

    elif isStraight(hand):
        a = noSuitHand(hand)
        #Straight, returns [rank, lowest card]
        return [5, a[0]]

    elif ThreeOfaKind(hand):
        handValue = [4, 0]

        dl = handToDict(hand)
        for i in dl:
            if dl[i] == 3:
                handValue[1] = i
        #Three Of a kind, returns [rank, the card]
        return handValue

    elif twoPairs(hand):
        handValue = [3, 0, 0, 0]
        dl = handToDict(hand)

        for i in dl:
            if dl[i] == 2:
                if handValue[1] == 0:
                    handValue[1] = i
                else:
                    if i > handValue[1]:
                        handValue[2] = handValue[1]
                        handValue[1] = i
                    else:
                        handValue[2] = i
            else:
                handValue[3] = i
        
        #Two pairs, returns [rank, greater pair, lesser pair, single]
        return handValue

    elif onePair(hand):
        handValue = [2, 0]
        dl = handToDict(hand)

        for i in dl:
            if dl[i] == 2:
                handValue[1] = i
            else:
                handValue.append(int(i))
        
        handValue[2:] = sorted(handValue[2:], reverse = True)

        #One pair, returns [rank, pair, high to low]
        return handValue

    else:
        a = noSuitHand(hand)
        a = sorted(a, reverse = True)
        a.insert(0,1)
        #Highest card, returns [high to low]
        return a


if __name__ == "__main__":

    playerOneWinCount = 0
    translate = {'K':'13', 'T':'10', 'J':'11', 'Q':'12', 'A':'14'}
    
    f = open(r'C:\Users\kxiao\Desktop\Python\p054_poker.txt', 'r')
    for i in f.readlines():
        a = i
        for j in translate:
            a = a.replace(j, translate[j])
        a = a[:-1].split(' ')
    
        rankHandOne = rank(a[:5])
        rankHandOne = [int(i) for i in rankHandOne]
    
        rankHandTwo = rank(a[5:])
        rankHandTwo = [int(i) for i in rankHandTwo]

        if rankHandOne[0] == rankHandTwo[0]:
            if rankHandOne > rankHandTwo:
                playerOneWinCount += 1
            else:
                continue
        elif rankHandOne[0] > rankHandTwo[0]:
            playerOneWinCount += 1
        
    f.close()

    print playerOneWinCount




