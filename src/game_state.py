from src.card import Card
from src.deck import Deck
from src.player import Player


class GameState:
    def __init__(self, players: list[Player], deck: Deck, current_player: int = 0, card: Card | None = None, coins: int = 0):
        self.players: Player = players
        self.deck: Deck = deck
        self._current_player: int = current_player
        self.card = card
        self.coins = coins
     
        
    def current_player(self) -> Player:
        return self.players[self._current_player]
    
    def __eq__(self, other):
        return self.players == other.players and self.deck == other.deck and \
               self._current_player == other._current_player and self.card == other.card \
               and self.coins == other.coins      
    def save(self) -> dict:
        return {
            "top": {"card": self.card, "coins": self.coins},
            "deck":self.deck,
            "current_player_index": self._current_player,
            "players": [p.save() for p in self.players],
        }
        
    @classmethod
    def load(cls, data: dict):
        players = [Player.load(d) for d in data["players"]]
        
        
        return cls(
            players=players,
            deck=Deck.load(data["deck"]),
            card = Card.load(data["top"]["card"]),
            coins = int(data["top"]["coins"]),
            current_player=int(data["current_player_index"]),
        )
    
    def next_player(self):
        self._current_player += 1
        self._current_player  %= len(self.players)
   
    def draw_card(self):
        card = self.deck.draw_card()
        self.current_player().hand.add_card(card)
        return card
    
    def take_card(self):
        self.current_player().hand.add_card(self.card)
        self.current_player().coins += self.coins
    
    def _raise(self):
        self.current_player().coins -= 1
        self.coins +=1
    
    def score_players(self) -> {Player: int}:
        return {p.name: p.score()-p.coins for p in self.players}
        