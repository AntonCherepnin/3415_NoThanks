from src.card import Card
class Hand:
    def __init__(self,cards: list[Card]=[]):
        if cards is None:
            cards = []
        self.cards:list[Card] = cards
    def __repr__(self):
        return self.save()
    
    def __eq__(self,other):
        if isinstance(other,list):
            other = Hand.load(other)
        return self.cards == other.cards
    def save(self):
        s = [c.save() for c in self.cards]
        return s
    
    @classmethod
    def load(cls, lis: list):
        cards = [Card.load(s) for s in lis]
        return cls(cards=cards)
    def add_card(self,card: Card):
        self.cards.append(card)
    def score(self):
        res = 0
        ls = self.save()
        for i in range(len(ls)):
            res+=ls[i]
        return res