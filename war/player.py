from __future__ import annotations
from card import Card


class Player:
    """A player in the game."""

    def __init__(self: Player, name: str) -> None:
        """Initialize the player."""
        self.name: str = name
        self._hand: list[Card] = []

    def add_cards(self: Player, cards: list[Card]) -> None:
        """Add cards to the player's hand."""
        self._hand.extend(cards)

    def remove_card(self: Player) -> Card:
        """Remove a card from the player's hand."""
        return self._hand.pop(0)

    def __str__(self) -> str:
        return f"{self.name} has {len(self._hand)} cards."


if __name__ == "__main__":
    p = Player("Bob")
    print(p)

    p.add_cards([Card("Clubs", "A"), Card("Spades", "2")])
    print(p)

    p.remove_card()
    print(p)