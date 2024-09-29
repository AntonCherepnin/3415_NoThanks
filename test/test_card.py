import pytest
from src.card import Card


def test_init():
    a = Card(15)
    assert a.value == 15
    with pytest.raises(ValueError):
        Card('e')
    with pytest.raises(ValueError):
        Card(2.21)
    with pytest.raises(ValueError):
        Card(1)
def test_repr():
    a = Card(12)
    assert a.__repr__() == '12'
    assert Card.__repr__(Card(13)) == '13'
def test_eq():
    a1 = Card(3)
    a2 = Card(6)
    a3 = Card(10)
    a4 = Card(3)
    a5 = Card(6)
    assert a1==a4
    assert a1!=a3
    assert a2==a5
    assert a4!=a5
def test_load():
    s = 5
    c = Card.load(s)
    assert c == Card(5)

    s = 10
    c = Card.load(10)
    assert c == Card(10)
def test_all_cards():
    cards = Card.all_cards([13,5,10,20])
    expected_cards = [
        Card.load(13),
        Card.load(5),
        Card.load(10),
        Card.load(20)
    ]
    assert cards == expected_cards