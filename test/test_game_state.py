
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
full_deck = Deck(None)

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
    game = GameState(players = players, deck = full_deck,  card = Card(5), coins = 0 )
    assert game.current_player() == alex
    
    game = GameState(players = players, deck = full_deck, current_player = 1, card = Card(5), coins = 0 )
    assert game.current_player() == anton
    
    game = GameState(players = players, deck = full_deck, current_player = 2, card = Card(5), coins = 0 )
    assert game.current_player() == bob
      
def test_eq():
    players = [alex, anton, bob]
    game1 = GameState(players = players, deck = full_deck,  card = Card(5), coins = 0 )
    game2 = GameState(players = players.copy(), deck = full_deck,  card = Card(5), coins = 0 )
    game3 = GameState(players=players, deck=Deck.load([6, 10, 11]), card = Card(5), coins = 0 )
    assert game1 == game2
    assert game1 != game3
