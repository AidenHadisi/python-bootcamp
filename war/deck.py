from __future__ import annotations
from random import shuffle
from card import Card


class Deck:
    """A deck of playing cards."""

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suites = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self: Deck) -> Deck:
        """Initialize the deck."""
        self._cards = [Card(s, r) for s in self.suites for r in self.ranks]

    @property
    def cards(self: Deck) -> list:
        """Return the cards in the deck."""
        return self._cards

    def shuffle(self: Deck) -> None:
        """Shuffle the deck."""
        shuffle(self._cards)

    def deal(self: Deck) -> Card:
        """Deal a card from the deck."""
        return self._cards.pop()


if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    print(d.cards[0])
