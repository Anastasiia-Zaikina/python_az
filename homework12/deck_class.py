import random

from homework12.card_class import Card


class Deck:
    def __init__(self):
        self.__cards = Deck.create_deck()

    @staticmethod
    def create_deck():
        deck = []
        for suit in Card.possible_suites():
            for rank in Card.possible_rank():
                deck.append(Card(suit, rank))
        random.shuffle(deck)
        return deck

    @property
    def cards(self):
        return self.__cards

    def deal_card(self):
        return self.__cards.pop()
