import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("diamonds", 10)
        self.card2 = Card("spades", 1)
        self.game = CardGame()
        self.cards = [self.card1, self.card2]

    def test_found_an_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card2))

    def test_did_not_find_an_ace(self):
        self.assertEqual(False, self.game.check_for_ace(self.card1))

    def test_find_the_highest_card(self):
        self.assertEqual(self.card1, self.game.highest_card(self.card1, self.card2))

    def test_find_the_total(self):
        self.assertEqual("You have a total of 11", self.game.cards_total(self.cards))