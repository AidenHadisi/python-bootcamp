from __future__ import annotations
from functools import total_ordering


@total_ordering
class Card:
    """A playing card."""

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def value(self, valueOfCurrentHand: int) -> int:
        """Return the value of the card."""
        match self.rank:
            case "K" | "Q" | "J":
                return 10
            case "A" if valueOfCurrentHand < 11:
                return 11
            case "A":
                return 1
            case _:
                return int(self.rank)

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other: object) -> bool:
        return (
            NotImplemented if not isinstance(other, Card) else self.value == other.value
        )

    def __lt__(self, other: object) -> bool:
        return (
            NotImplemented if not isinstance(other, Card) else self.value < other.value
        )
