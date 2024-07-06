from deck import Deck
from card import Card

class DecksManager:
    def __init__(self, decks : list[Deck] | None = None):
        self.decks = decks or list()

    def create_deck(self) -> None :
        # get deck information
        deck_name = None
        while not deck_name :
            deck_name = input('Enter deck name : ')

        deck_description = None
        while not deck_description :
            deck_description = input('Enter deck description : ')

        # create cards
        add_card : bool = True
        new_cards : list[Card] = list()
        print('\nStarting to create cards.')
        while add_card :
            print()
            new_card : Card = self.create_card()
            new_cards.append(new_card)
            user_answer : str = input('Do you want to add an additional card? [yes/no]: ').lower()
            add_card = user_answer in ['yes', 'y']

        # create deck
        new_deck = Deck(deck_name,
                        deck_description,
                        new_cards)

        self.decks.append(new_deck)

        print('new deck :')
        print(new_deck)

    def create_card(self) -> Card :
        # get question
        card_question = None 
        while not card_question :
            card_question = input('Enter card question : ')

        # get answer
        card_answer = None 
        while not card_answer :
            card_answer = input('Enter card answer : ')
        
        # get additional info
        card_info = None 
        while not card_info :
            card_info = input('Enter card additional information : ')

        new_card = Card(card_question,
                        card_answer,
                        card_info)

        return new_card