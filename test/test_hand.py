from src.card import Card 
from src.hand import Hand

cards = [Card(10), Card(12), Card(15)]

def test_init():
    d = Hand(cards=cards)
    assert d.cards == cards
def test_save():
    d = Hand(cards=cards)
    assert d.save() == [10, 12, 15]
def test_load():
    cards = [Card(12), Card(15), Card(16)]
    d = Hand(cards).save()
    assert Hand.load(d) == Hand(cards)
def test_score():
    h = Hand.load([10,15,16])
    assert h.score() == 41

    h = Hand.load([5,9])
    assert h.score() == 14
def test_add_card():
    h = Hand.load([10,15,16])
    h.add_card(Card.load(9))
    assert h == [10,15,16,9]
    
    h.add_card(Card.load(5))
    assert h == [10,15,16,9,5]