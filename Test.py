
import random

class Card(object):
    suit_name = ['Clubs','Diamond','Hearts','Spades']
    rank_name = [None, 'Ace','Two','Three','Four','Five','Six','Seven',
                 'Eight','Nine','Ten','Jack','Queen','King']
    def __init__(self, suit, rank):
        self.suitname = suit
        self.rankname = rank
    def __str__(self):
        return '%s of %s' % (Card.rank_name[self.rankname],
                             Card.suit_name[self.suitname])

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank) #suit 0 rank 123...14, suit 1 rank 123...14
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)


        
    def move(self, hand ,num): #여기서 셀프는 덱임. 핸드는 왜 나왔는지 모르겠는데, 아마도                                #hand때문에 생긴거 같은데 num 은 5임
        for i in range(num):# num = 5    
            hand.add_card(self.pop_card())
    def deal_hands(self, num_hands, num_cards):
        hands = []
        for i in range(num_hands):
            hand = Hand()
            self.move(hand, num_cards) # 여기서 손에다가 5개씩 카드 날릴거임
            hands.append(hand)
        return hands

class Hand(Deck):#그니까 덱에서 다 빠져나간다는 개념보다는 손으로 들어오는거임
    # 그러니까 지금은 빈손인 상태인데, 만약에 move 함수 때리면 들어온다는 거임
    # label은 명목상이고 빈손으로 만드는거임.
    def __init__(self, label = ' '):
        self.cards = []
        self.label = label

def main():
    deck = Deck()
    deck.shuffle()
    hands = deck.deal_hands(4,5)
    for hand in hands: #4명한테 카드를 5개 날려준 상태이고, 그걸 분류해서 프린트한거
        print('\n')
        print(hand)

main()


