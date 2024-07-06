from card import Card

class Deck:
    def __init__(self, name : str, description : str, cards : list[Card]):
        self.name = name
        self.description = description
        self.cards = cards

    def __str__(self) -> str :
        representation = 'Deck Name: {0}\nDescription: {1}\nCards :'.format(self.name, self.description, self.cards)
        for card in self.cards :
            representation += '\n' + str(card) 
        return representation
        