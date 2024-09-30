import random 

from src.card import Card
from src.deck import Deck

cards = [Card(6), Card(8), Card(10)]

def test_init():
    d = Deck(cards=cards)
    assert d.cards == cards

def test_save():
        d = Deck(cards=cards)
        assert d.save() == [6,8,10]
        
        d = Deck(cards=[])
        assert d.save() == []

def test_load():
    cards = [Card(12), Card(15), Card(16)]
    d = Deck(cards).save()
    assert Deck.load(d) == Deck(cards)

def test_draw_card():
     d1 = Deck.load([6, 10, 15])
     d2 = Deck.load([6, 10])
     c = d1.draw_card()
     assert c == Card.load(15)
     
     assert d1 == d2 

def test_shuffle():
    random.seed(3)

    cards = Card.all_cards([9, 10, 23])
    d = Deck(cards)
    d.shuffle()
    assert d.save() == [10, 23, 9]
    
    d.shuffle()
    assert d.save() == [10, 9, 23]
    
    d.shuffle()
    assert d.save() == [9, 10, 23]

