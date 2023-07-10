"""Implement a console game (sea-fight, blackjack, poker) using all your knowledge from previous lessons.
You should use Classes, decorators, magic methods, etc..."""


import random

from homework12.deck_class import Deck



class Blackjack:
    def __init__(self):
        self.__deck = Deck()
        self.__player_hand = []
        self.__dealer_hand = []

    @property
    def deck(self):
        return self.__deck

    @staticmethod
    def calculate_hand_value(hand):
        hand_value = sum(card.score for card in hand)
        return hand_value

    def print_hand(self, hand, hide_first_card=False):
        if hide_first_card:
            print('* ' + ' '.join(str(card) for card in hand[1:]))
        else:
            print(' '.join(str(card) for card in hand))

    def blackjack_welcome(func):
        def wrapper(self,*args, **kwargs):
            print("***Welcome to Blackjack!***")
            return func(self, *args, **kwargs)
        return wrapper

    def check_blackjack(self, hand):
        return len(hand) == 2 and self.calculate_hand_value(hand) == 21

    def player_turn(self):
        while True:
            choice = input('Do you want to hit or stand? (h/s): ')
            if choice.lower() == 'h':
                self.__player_hand.append(self.__deck.deal_card())
                self.print_hand(self.__player_hand)
                if self.calculate_hand_value(self.__player_hand) > 21:
                    print('You bust! Dealer wins.')
                    return 'bust'
            elif choice.lower() == 's':
                break
            else:
                print('Invalid input! Please enter h for hit or s for stand.')

    def dealer_turn(self):
        self.print_hand(self.__dealer_hand)
        while self.calculate_hand_value(self.__dealer_hand) < 17:
            self.__dealer_hand.append(self.deck.deal_card())
            self.print_hand(self.__dealer_hand)
            if self.calculate_hand_value(self.__dealer_hand) > 21:
                print('Dealer busts! You win.')
                return 'bust'



    @blackjack_welcome
    def play(self):

        self.__player_hand = [self.deck.deal_card(), self.deck.deal_card()]
        self.__dealer_hand = [self.deck.deal_card(), self.deck.deal_card()]

        self.print_hand(self.__player_hand)
        self.print_hand(self.__dealer_hand, hide_first_card=True)

        if self.check_blackjack(self.__player_hand) and self.check_blackjack(self.__dealer_hand):
            print('Both player and dealer have blackjack.')
        elif self.check_blackjack(self.__player_hand):
            print('Blackjack! You win.')
        elif self.check_blackjack(self.__dealer_hand):
            print('Dealer has blackjack. You lose.')
        else:
            player_result = self.player_turn()
            if player_result == 'bust':
                return
            dealer_result = self.dealer_turn()
            if dealer_result == 'bust':
                return

            player_hand_value = self.calculate_hand_value(self.__player_hand)
            dealer_hand_value = self.calculate_hand_value(self.__dealer_hand)

            if player_hand_value > dealer_hand_value:
                print('You win.')
            elif player_hand_value < dealer_hand_value:
                print('Dealer wins.')
            else:
                print('The game ends in a tie.')

if __name__ == '__main__':
    game = Blackjack()
    game.play()
