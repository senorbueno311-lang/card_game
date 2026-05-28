import random
from card import Card
from vars import RANKS, SUITS


class Deck:

    def __init__(self):
        self.deck = []
        for rank in RANKS:
            for suit in SUITS:
                card = Card(rank, suit)
                self.deck.append(card)

    def deal(self):
        return self.deck.pop() if self.deck else None

    def shuffle(self):
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)

    def __repr__(self):
        return f"Deck with {len(self.deck)} cards remaining"
