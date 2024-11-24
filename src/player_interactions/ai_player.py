from src.card import Card
from src.hand import Hand
from src.player import Player
from src.game_state import GameState

from player_interaction import PlayerInteraction
import random
class Bot(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, coins: int):
        coins_top = coins
        if player.coins == 0:
            choose = 'Take card'
            print('Не взял')
        elif coins_top <= random.randint(1,15):
            choose = 'Spend'
        else:
            choose = 'Take card'
        return choose

        
            