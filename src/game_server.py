import inspect
import json
import sys

sys.path.append('src')

from deck import Deck
from game_state import GameState
from hand import Hand
from player import Player
from player_interaction import PlayerInteraction
import player_interactions as all_player_types

import logging

import enum

from player_interactions import Bot


class GamePhase(enum.StrEnum):
    START_BIDDING = "Draw new card"
    BIDDING = "Choose action: raise or take"
    CONTINUE_BIDDING = "Switch current player due to raise"
  
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

   # START_BIDDING -> BIDDING | DECLARE_WINNER
   # BIDDING -> START_BIDDING | CONTINUE_BIDDING
   # CONTINUE_BIDDING -> BIDDING

    #DECLARE_WINNER -> GAME_END
class GameServer:
    
    def __init__(self, player_types, game_state):
        self.game_state = game_state
        self.player_types = player_types  
        
    @classmethod
    def load_game(cls):
        filename = 'NoThanks.json'
        with open(filename,'r') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save)
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)
    
    def save(self):
        filename = 'NoThanks.json'
        data = self.save_to_dict()
        with open(filename, 'w') as fout:
            json.dump(data, fout, indent=4)
    
    def save_to_dict(self):
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data['players'][player_index]['kind'] = self.player_types[player].__name__
        return data
    
    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()

        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name, Hand())
            player_types[player.name] = kind
        return player_types
    
    @classmethod
    def new_game(cls, player_types: dict):
        deck = Deck()
        deck.shuffle()
        for _ in range(9):
            deck.draw_card()
        card_top= deck.draw_card()
        players: list[Player] = [Player(name=name, coins=11)
                                 for name in player_types.keys()]
        game_state = GameState(players=players, deck = deck, card = card_top) 
        
        print(game_state.save())
        
        res = cls(player_types, game_state)
        return res
    
    def run(self):
        current_phase = GamePhase.BIDDING
        while current_phase != GamePhase.GAME_END:
            phases = {
               GamePhase.START_BIDDING: self.start_bidding_phase,
               GamePhase.BIDDING: self.bidding_phase,
               GamePhase.CONTINUE_BIDDING: self.continue_bidding_phase,
               GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()
    
    def declare_winner_phase(self) -> GamePhase:
            #Leaderboard:
            #1. Alex = 50
            #2. Anton = 87
            #3. Bob = 88
            #Alex WIN!
        score = self.game_state.score_players()
        sortedScore = sorted(score.items(), key=lambda x:x[1])
        print('Leaderboard:')
        
        for i in range(len(sortedScore)):
            print(f'{i+1}. {sortedScore[i][0]} = {sortedScore[i][1]}')

        print(f"{sortedScore[0][0]} is the winner!")
        return GamePhase.GAME_END
    def start_bidding_phase(self) -> GamePhase:
        if self.game_state.deck.is_empty(): 
            return GamePhase.DECLARE_WINNER
        self.game_state.card = self.game_state.deck.draw_card()
        self.game_state.score = 0
        print('Top:', {"card": self.game_state.card , "coins": self.game_state.score})
        return GamePhase.BIDDING 
    
    def bidding_phase(self)  -> GamePhase:
        current_player = self.game_state.current_player()
        interaction = self.player_types[current_player.name]
        print(current_player.hand)
        choose = interaction.choose_action(current_player, self.game_state.coins)
        if choose == 'Take card':
                self.game_state.take_card()
                interaction.inform_card_take(current_player)
                return GamePhase.START_BIDDING
        elif choose == 'Spend':
            self.game_state._raise()
            interaction.inform_player_spend(current_player)
            return GamePhase.CONTINUE_BIDDING
    def continue_bidding_phase(self) -> GamePhase:
        self.game_state.next_player()
        print(f"=== {self.game_state.current_player()}'s turn")
        return GamePhase.BIDDING
        
    def inform_all(self, method: str, *args, **kwargs):
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)
            
    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("How many players?"))
                if 3 <= player_count <= 5:
                    return player_count
            except ValueError:
                pass
            
            print("Please input a number between 3 and 5")
            
    @staticmethod
    def request_player() -> (str, PlayerInteraction):   
        player_types = []
        for name, cls in inspect.getmembers(all_player_types):
            if inspect.isclass(cls) and issubclass(cls, PlayerInteraction):
                player_types.append(cls.__name__)
        player_types_as_str = ', '.join(player_types)
        
        while True:
            name = input("How to call a player?")
            if name.isalpha():
                break
            print("Name must be a single word, alphabetic characters only")
            
        while True:
            try:
                kind = input(f"What kind of player is it ({player_types_as_str})?")
                kind = getattr(all_player_types, kind)
                break
            except AttributeError:
                print(f"Allowed player types are: {player_types_as_str}")
        return name, kind

    
def __main__():
    load_from_file = False
    if load_from_file:
        server = GameServer.load_game()
        server.save()
    else:
        server = GameServer.new_game(GameServer.get_players())
    server.run()
                
if __name__ == "__main__":
        __main__()    
