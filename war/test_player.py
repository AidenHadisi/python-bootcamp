import unittest
from player import Player
from card import Card


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Set up a test player and cards for use in all tests
        self.player = Player("TestPlayer")
        self.card1 = Card("Hearts", "10")
        self.card2 = Card("Diamonds", "A")
        self.cards = [self.card1, self.card2]

    def test_initialization(self):
        # Test if player is correctly initialized
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(len(self.player._hand), 0)

    def test_add_cards(self):
        # Test if cards are added to the player's hand
        self.player.add_cards(self.cards)
        self.assertEqual(len(self.player._hand), 2)
        self.assertIn(self.card1, self.player._hand)
        self.assertIn(self.card2, self.player._hand)

    def test_remove_card(self):
        # Test if a card is removed from the player's hand
        self.player.add_cards(self.cards)
        removed_card = self.player.remove_card()
        self.assertEqual(removed_card, self.card1)
        self.assertEqual(len(self.player._hand), 1)
        self.assertNotIn(self.card1, self.player._hand)
        self.assertIn(self.card2, self.player._hand)

    def test_str_representation(self):
        # Test the string representation of the player
        self.player.add_cards(self.cards)
        expected_str = f"{self.player.name} has {len(self.player._hand)} cards."
        self.assertEqual(str(self.player), expected_str)

    def test_remove_card_from_empty_hand(self):
        # Test removing a card from an empty hand (should raise IndexError)
        with self.assertRaises(IndexError):
            self.player.remove_card()


if __name__ == "__main__":
    unittest.main()
