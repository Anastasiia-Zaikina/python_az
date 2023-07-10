class Card:
    def __init__(self, suit: str, rank: str):
        self.__suit = suit
        self.__rank = rank
        self.__score = Card.scores_dict().get(rank)

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

    @property
    def score(self):
        return self.__score

    @staticmethod
    def possible_suites():
        return ['♠', '♡', '♢', '♣']

    @staticmethod
    def possible_rank():
        return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    @staticmethod
    def scores_dict():
        return {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                'A': 11}

    def __str__(self):
        return f'{self.__suit}:{self.__rank}'
