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

class GameServer:
    
    def __init__(self, player_types, game_state):
        self.game_state: GameState = game_state
        self.player_types: dict = player_types
        
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
               GamePhase.START_BIDDING: self.start_bidding_phase(),
               GamePhase.BIDDING: self.bidding_phase(),
               GamePhase.CONTINUE_BIDDING: self.continue_bidding_phase(),
               GamePhase.DECLARE_WINNER: self.declare_winner_phase(),
            }
            current_phase = phases[current_phase]()
    
    