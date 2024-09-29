import random 

from src.card import Card
from src.deck import deck

cards = [Card(6),Card(8),Card(10)]

def test_init():
    d = deck(cards=cards)
    assert d.cards == cards

