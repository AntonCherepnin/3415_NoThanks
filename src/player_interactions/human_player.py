from src.card import Card
from src.hand import Hand
from src.player import Player
from src.game_state import GameState

from src.player_interaction import PlayerInteraction

class Human(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, coins: int):
        while True:
            print('Choose one of the option: T(Take card) and S(Spend)')
            choose = input("Choose action: \n")
            if player.coins == 0 or choose == 'T':
                choose = 'Take card'
            elif choose == 'S':
                choose = 'Spend'
            return choose

            
                    