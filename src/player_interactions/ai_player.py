import sys
sys.path.append('src')
from card import Card
from hand import Hand
from player import Player
from game_state import GameState

from player_interaction import PlayerInteraction
import random
class Bot(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, coins: GameState):
        coins_top = coins
        if player.coins == 0:
            choose = 'Take card'
            print('Не взял')
        elif coins_top <= random.randint(1,15):
                print('Взял')
                choose = 'Spend'
        else:
            choose = 'Take card'
        return choose
    @classmethod
    def inform_card_take(cls, player: Player):
        """
        Сообщает, что игрок взял карту.
        """
        pass

    @classmethod
    def inform_player_spend(cls, player: Player):
        """
        Сообщает, что игрок потратил фишку.
        """
        pass
            
        
        
            