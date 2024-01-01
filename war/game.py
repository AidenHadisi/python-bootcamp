from __future__ import annotations

from deck import Deck
from card import Card
from player import Player


class Game:
    """A game of War."""

    def __init__(self: Game, player1: Player, player2: Player) -> None:
        """Initialize the game."""
        self._player1 = player1
        self._player2 = player2
        self._deck = Deck()
        self._deck.shuffle()
        self.table: list[Card] = []

    @property
    def is_over(self: Game) -> bool:
        """Return True if the game is over."""
        return len(self._player1._hand) == 0 or len(self._player2._hand) == 0

    def deal(self: Game) -> None:
        """Deal the cards."""
        while len(self._deck.cards) > 0:
            self._player1.add_cards([self._deck.deal()])
            self._player2.add_cards([self._deck.deal()])

    def play(self: Game) -> None:
        """Play the game."""
        self.deal()

        print("Let's play War!")
        while not self.is_over:
            self.table.append(self._player1.remove_card())
            self.table.append(self._player2.remove_card())

            if self.table[-1] > self.table[-2]:
                print(
                    f"{self._player1.name} wins the hand and gets {len(self.table)} cards!"
                )
                self._player1.add_cards(self.table)
                self.table.clear()

            elif self.table[-1] < self.table[-2]:
                print(
                    f"{self._player2.name} wins the hand and gets {len(self.table)} cards!"
                )
                self._player2.add_cards(self.table)
                self.table.clear()

            else:
                print("WAR!")
                if len(self._player1._hand) < 5 or len(self._player2._hand) < 5:
                    print("Not enough cards to continue. Game over.")
                    break

                for _ in range(3):
                    self.table.append(self._player1.remove_card())
                    self.table.append(self._player2.remove_card())

        if len(self._player1._hand) > len(self._player2._hand):
            print(f"{self._player1.name} wins!")
        else:
            print(f"{self._player2.name} wins!")


if __name__ == "__main__":
    g = Game(Player("John"), Player("Joe"))
    g.play()
