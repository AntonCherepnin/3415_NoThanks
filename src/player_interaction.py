from abc import ABC, abstractmethod
from src.card import Card
from src.hand import Hand
from src.player import Player
from enum import Enum

class ChooseAction(Enum):
    TAKE_CARD = "Take card"
    SPEND = "Spend"

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