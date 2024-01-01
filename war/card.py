from __future__ import annotations
from functools import total_ordering


@total_ordering
class Card:
    """A playing card."""

    def __init__(self: Card, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    @property
    def value(self: Card) -> int:
        """Return the value of the card."""
        if self.rank == "A":
            return 14
        elif self.rank == "K":
            return 13
        elif self.rank == "Q":
            return 12
        elif self.rank == "J":
            return 11
        else:
            return int(self.rank)

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Card):
            return NotImplemented
        return self.value == __value.value

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Card):
            return NotImplemented
        return self.value < __value.value


if __name__ == "__main__":
    c = Card("Clubs", "A")
    print(c)

    c2 = Card("Spades", "2")
    print(c2)

    print(c == c2)
    print(c > c2)
