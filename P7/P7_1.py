import numpy
import random
import matplotlib.pyplot as plt


class Deck:
    def __init__(self):
        self.cards = list(range(1, 11))
        self.cards.extend([10, 10, 10])
        self.cards *= 4
        self.shuffle()

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_two_cards(self):
        try:
            a = self.cards.pop()
            b = self.cards.pop()
        except:
            return None
        return a, b

    def check(self):
        try:
            a, b = self.get_two_cards()
        except:
            return 0
        if a + b == 21:
            return 1
        if a + b == 11 and (a == 1 or b == 1):
            return 1
        return 0

    def blackjack(self):
        count = 0
        while self.size() >= 2:
            count += self.check()
        return count


k = 0
l = []
n = 10000

for i in range(1, n + 1):
    temp_deck = Deck()
    # print(temp_deck.cards)
    k += temp_deck.blackjack()
    average = k / i
    l.append(average)

print(average)

plt.plot(l)
plt.show()
