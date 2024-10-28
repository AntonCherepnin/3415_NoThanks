from src.hand import Hand
from src.player import Player

def test_init():
    h = Hand.load([5, 10, 15])
    p = Player(name = 'Alex', hand = h, coins = 0)
    
    assert p.name == 'Alex'
    
    assert p.hand == [5, 10, 15]
    
    assert p.coins == 0

def test_str():
    h = Hand.load([5, 10, 15])
    p = Player(name = 'Alex', hand = h, coins = 0)
    
    assert str(p) == 'Alex(11): [5, 10, 15]'

def test_save():
    h1 = Hand.load([5, 10, 15])
    h2 = Hand.load([5, 10, 15])
    p1 = Player(name = 'Alex', hand = h1, coins = 0)
    p2 = Player(name = 'Alex', hand = h2, coins = 0)
    assert p1 == p2

def test_load():
    data = {'name': 'Alex', 'hand': [5, 6, 7], 'coins': 15}
    h = Hand.load([5, 6, 7 ])
    p_expected = Player(name = 'Alex', hand = h, coins = 15)
    p = Player.load(data)
    assert p == p_expected

