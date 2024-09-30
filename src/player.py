import json 
import typing


from src.hand import Hand


class Player:
    def __init__(self, name: str, hand: Hand, coins: int = 11):
        self.name = name
        self.hand = hand
        self.coins = coins
        
    def __str__(self):
        return f'{self.name}({self.coins}): {self.hand}'

    def __eq__(self, other: typing.Self | str | dict):
        if isinstance(other, str):
            other = self.load(json.loads(other))
        if isinstance(other, dict):
            other = self.load(other)
        return self.name == other.name \
               and self.coins == other.coins \
               and self.hand == other.hand
    
    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': self.hand,
            'score': self.coins,
        }
    
    @classmethod
    def load(cls, data: dict):
        return cls(name=data['name'], hand=Hand.load(data['hand']), coins=int(data['coins']))
