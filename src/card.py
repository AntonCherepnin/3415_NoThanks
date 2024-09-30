'''No_thnaks'''

class Card:
    VALUES = list(range(3, 36))

    def __init__(self, value: int):
        if value not in Card.VALUES:
            raise ValueError
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other):
        return self.value == other.value 
    
    def save(self) -> int:
        '''Card(15)->15'''
        return self.value
   
    
    @staticmethod
    def load(number: int):
        return Card(value = number)
    
    
    @staticmethod
    def all_cards(values: None | list[int] = None):
        if values is None:
            values  = Card.VALUES
        cards = [Card(value = val) for val in values]
        return cards
