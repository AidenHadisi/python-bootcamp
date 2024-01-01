from deck import Deck
from card import Card


class Game:
    """A game of Blackjack!"""

    def __init__(self) -> None:
        self._deck = Deck()
        self._deck.shuffle()
        self.player_hand: int = self._deck.hit().value(0)
        self.dealer_hand: int = self._deck.hit().value(0)
        self.player_hand += self._deck.hit().value(self.player_hand)
        self.dealer_hand += self._deck.hit().value(self.dealer_hand)

    def play(self) -> None:
        """Play the game."""

        while not self.is_over:
            print(f"Your hand: {self.player_hand}")
            match input("Hit or stand? (h/s) ").lower():
                case "h":
                    self.player_hand += self._deck.hit().value(self.player_hand)
                case "s":
                    break
                case _:
                    print("Invalid input. Try again.")

            if self.player_hand > 21:
                print("You bust!")
                break

            if self.dealer_hand < 17:
                self.dealer_hand += self._deck.hit().value(self.dealer_hand)
            else:
                break

        print(f"Your hand: {self.player_hand}")
        print(f"Dealer's hand: {self.dealer_hand}")
        print(
            "You win!"
            if self.player_hand > self.dealer_hand and self.player_hand <= 21
            else "You lose!"
        )

    @property
    def is_over(self) -> bool:
        """Return True if the game is over."""
        return self.player_hand > 21 or self.dealer_hand > 21


if __name__ == "__main__":
    Game().play()
