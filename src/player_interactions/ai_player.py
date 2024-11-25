from src.card import Card
from src.hand import Hand
from src.player import Player
from src.game_state import GameState

from src.player_interaction import PlayerInteraction
from src.player_interaction import ChooseAction

import random

class Bot(PlayerInteraction):
    @classmethod
    def choose_action(cls, player: Player, coins: int):
        coins_top = coins
        if player.coins == 0:
            choose = ChooseAction.TAKE_CARD
        elif coins_top <= random.randint(1,15):
            choose = ChooseAction.SPEND
        else:
            choose = ChooseAction.TAKE_CARD
        return choose

        
            