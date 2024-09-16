import pytest
from card import (Card)


def test_init():
    a = Card(15)
    assert a.value == 15
def test_repr():
    a = Card(12)
    assert a.__repr__() == '15'
    assert Card.__repr__(Card(13)) == '14'
