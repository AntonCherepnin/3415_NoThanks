
from src.card import Card
from src.deck import Deck
from src.hand import Hand
from src.game_state import GameState
from src.player import Player

data = {
    "top":
        {
        "card": 12,
        "coins": 25,
        },
    "current_player_index": 1,
    "deck": [15, 28],
    "players": 
        [
        {"name": 'Alex', "hand": [4,7,10,12],"coins": 10},
        {"name": 'Anton',"hand": [11,13,14,18],"coins": 11},
        {"name": 'Bob', "hand": [9,19,23,25],"coins": 10},
        ],
}
alex = Player.load(data["players"][0])
anton = Player.load(data["players"][1])
bob = Player.load(data["players"][2])
full_deck = Deck(5)

def test_init():
    players = [alex, anton, bob]
    game = GameState(players = players, deck = full_deck, current_player = 1, card = Card(5), coins = 0 )
    
    assert game.players == players
    assert game.deck == full_deck
    assert game._current_player == 1
    assert game.card == Card(5)
    assert game.coins == 0

def test_current_player():
    players = [alex, anton, bob]
    for i, player in enumerate(players):
        game = GameState(players = players, deck = full_deck, current_player = i, card = Card(5), coins = 0 )
        assert game.current_player() == player
      
def test_eq():
    players = [alex, anton, bob]
    game1 = GameState(players = players, deck = full_deck,  card = Card(5), coins = 0 )
    game2 = GameState(players = players.copy(), deck = Deck(5),  card = Card(5), coins = 0 )
    game3 = GameState(players=players, deck=Deck.load([6, 10, 11]), card = Card(5), coins = 0 )
    assert game1 == game2
    assert game1 != game3
 
def test_save():
    players = [alex, anton, bob]
    game = GameState(
        players=players,
        deck=Deck.load(data["deck"]),
        card = Card.load(data["top"]["card"]),
        coins = int(data["top"]["coins"]),
        current_player=1
    )
    assert game.save() == data
def test_load():
    game = GameState.load(data)
    assert game.save() == data

def test_next_player():
    game = GameState.load(data)
    assert game.current_player() == anton

    game.next_player()
    assert game.current_player() == bob

    game.next_player()
    assert game.current_player() == alex

    game.next_player()
    assert game.current_player() == anton

def test_draw_card():
    players = [alex, anton, bob]
    game = GameState(
        players=players,
        deck=Deck.load(data["deck"]),
        card = Card.load(data["top"]["card"]),
        coins = int(data["top"]["coins"]),
        current_player= 2
    )
    assert game.deck == Deck.load([15,28])
    assert game.current_player().hand == [9,19,23,25]

    game.draw_card()
    assert game.deck == Deck.load([15])
    assert game.current_player().hand == [9,19,23,25,28]