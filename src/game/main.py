from vars import SUITS, RANKS, VALUES, NUMBER_PER_HAND as nph
from render import render_ascii_table
from card import Card
from deck import Deck
import os


def main():
    deck = Deck()
    deck.shuffle()

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Drawing {nph} cards:")
    player_hand = []
    comp_hand_1 = []
    partner_hand = []
    comp_hand_2 = []
    for _ in range(nph):
        player_hand.append(deck.deal())
        comp_hand_1.append(deck.deal())
        partner_hand.append(deck.deal())
        comp_hand_2.append(deck.deal())
    render_ascii_table(player_hand, nph)

    print(deck)


if __name__ == "__main__":
    main()
