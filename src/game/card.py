from vars import SUITS, RANKS


class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return ''.join(
            [
                f"\n______________\n"
                f"|............|\n"
                f"|.{self.suit}..........|\n"
                f"|............|\n"
                f"|.....{self.rank}.....|\n"
                f"|............|\n"
                f"|..........{self.suit}.|\n"
                f"|____________|\n"
            ]
        ).replace('.', ' ')
