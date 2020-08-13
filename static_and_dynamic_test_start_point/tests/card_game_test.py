import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def setUp(self):
        self.card_ace = Card("Hearts", 1)
        self.card_2 = Card("Hearts", 2)
        self.card_3 = Card("Hearts", 2)
        self.game_1 = CardGame()

    def test_checkforAce_is_ace(self):
        self.assertEqual(True, self.game_1.checkforAce(self.card_ace))

    def test_checkforAce_isnt_ace(self):
        self.assertEqual(False, self.game_1.checkforAce(self.card_2))

    def test_highest_card_first_card(self):
        self.assertEqual(self.card_2, self.game_1.highest_card(self.card_2, self.card_ace))

    def test_highest_card_second_card(self):
        self.assertEqual(self.card_2, self.game_1.highest_card(self.card_ace, self.card_2))

    def test_cards_total_no_cards(self):
        cards = []
        self.assertEqual("You have a total of 0", self.game_1.cards_total(cards))

    def test_cards_total_1_card(self):
        cards = [self.card_2]
        self.assertEqual("You have a total of 2", self.game_1.cards_total(cards))

    def test_cards_toal_3_cards(self):
        cards = [self.card_ace, self.card_2, self.card_3]
        self.assertEqual("You have a total of 5", self.game_1.cards_total(cards))