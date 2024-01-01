from __future__ import annotations
from random import shuffle
from card import Card


class Deck:
    """A deck of playing cards."""

    suites = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [str(n) for n in range(2, 11)] + list("AKQJ")

    def __init__(self) -> None:
        self.cards: list[Card] = [Card(s, r) for r in self.ranks for s in self.suites]

    def shuffle(self) -> None:
        """Shuffles the deck of cards."""
        shuffle(self.cards)

    def hit(self) -> Card:
        """Get a card from the deck"""
        return self.cards.pop()

    def is_empty(self) -> bool:
        """Return True if the deck is empty."""
        return not self.cards
