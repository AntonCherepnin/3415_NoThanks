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