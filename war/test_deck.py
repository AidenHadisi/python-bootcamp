import unittest
from deck import Deck
from card import Card


class TestDeck(unittest.TestCase):
    def setUp(self):
        # Set up a test deck and cards for use in all tests
        self.deck = Deck()

    def test_initialization(self):
        # Test if deck is correctly initialized
        self.assertEqual(len(self.deck.cards), 52)

    def test_shuffle(self):
        # Test if deck is shuffled
        original_cards = self.deck.cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, original_cards)

    def test_deal(self):
        # Test if a card is dealt from the deck
        card = self.deck.deal()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.cards), 51)
