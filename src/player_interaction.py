from abc import ABC, abstractmethod
import sys
sys.path.append('src')
from card import Card
from hand import Hand
from player import Player


class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_action(cls): 
        """
        Принимает решение взять карту или потратить фишку
        """
        pass

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