from src.card import Card

class Hand:
    def __init__(self, cards: None | list[Card]):
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
    
    def add_card(self, card: Card):
        self.cards.append(card)
    
    def score(self):
        ls = [c.value for c in self.cards]
        ls.sort()
        s = 0
        last, card = 0, 0
        while ls:
            last, card = card, ls.pop()
            if last != 0 and last - card == 1:
                continue
            s += last
        s += card
        return s