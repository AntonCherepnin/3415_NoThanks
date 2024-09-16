import pytest
from src.card import (Card)


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
    assert a.__repr__() == '15'
    assert Card.__repr__(Card(13)) == '14'
