from src.card import Card
import random
class deck:
    def __init__(self,cards: None | list[Card]):
        if cards is None:
            cards = Card.all_cards()
            random.shuffle(cards) #shuffle случайно распологает числа в массиве
        self.cards: list[Card] = cards
    def __repr__(self):
        return self.save()
    def __eq__(self,other):
        if isinstance(other, list):
            other = deck.load(other)
        return self.cards == other.cards
    def save(self) -> list:
        s = [c.save() for c in self.cards]
        return s
    
    @classmethod
    def load(cls, ls: list[int]):
        cards = [Card.load(num) for num in ls]
        return cls(cards)
    def draw_card(self):
     return self.cards.pop()
    def shuffle(self):
        random.shuffle(self.cards)