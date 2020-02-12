import unittest
from player import Player

class PlayerMethods(unittest.TestCase):

    def setUp(self):
        self.Player = Player('$')

    def test_get_move(self):
        self.Player.get_move()
        self.assertEqual(self.Player.r, 1)
        self.assertEqual(self.Player.c, 1)

    def test_player_move(self):
        self.assertEqual(self.Player.player_move(), None)

    def test_player_symbol(self):
        self.assertEqual(self.Player.player_symbol(), '$')

    def test_win(self):
        self.assertFalse(self.Player.win())

if __name__ == '__main__':
    unittest.main()