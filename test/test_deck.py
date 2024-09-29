import random 

from src.card import Card
from src.deck import deck

cards = [Card(6),Card(8),Card(10)]

def test_init():
    d = deck(cards=cards)
    assert d.cards == cards

def test_save():
        d = deck(cards=cards)
        assert d.save() == [6,8,10]
        
        d = deck(cards=[])
        assert d.save() == []
def test_load():
    cards = [Card(12), Card(15), Card(16)]
    d = deck(cards).save()
    assert deck.load(d) == deck(cards)
def test_draw_card():
     d1 = deck.load([6,10,15])
     d2 = deck.load([6,10])
     c = d1.draw_card()
     assert c == Card.load(15)
     assert d1 == d2 

def test_shuffle():
    random.seed(3)

    cards = Card.all_cards([9,10,23])
    d = deck(cards)
    d.shuffle()
    assert d.save() == [10,23,9]
    d.shuffle()
    assert d.save() == [10,9,23]
    d.shuffle()
    assert d.save() == [9,10,23]

