import unittest
from board import Board
from game import Game
from player import Player

class IntTestMethods(unittest.TestCase):
    
    def setUp(self):
        self.Game = Game()

    def test_o_win(self):
        self.Game.board.mark_square(int(1), int(1), 'o')
        self.Game.board.mark_square(int(1), int(0), 'x')
        self.Game.board.mark_square(int(2), int(2), 'o')
        self.Game.board.mark_square(int(2), int(1), 'x')
        self.Game.board.mark_square(int(0), int(0), 'o')
        self.assertEqual(self.Game.board.has_winner('o'), 2)

    def test_x_win(self):
        self.Game.board.mark_square(int(1), int(1), 'x')
        self.Game.board.mark_square(int(1), int(0), 'o')
        self.Game.board.mark_square(int(2), int(2), 'x')
        self.Game.board.mark_square(int(2), int(1), 'o')
        self.Game.board.mark_square(int(0), int(0), 'x')
        self.assertEqual(self.Game.board.has_winner('x'), 1)
    
    def test_check_same_box_valid(self):
        self.Game.board.mark_square(int(1), int(1), 'x')
        self.Game.board.mark_square(int(1), int(1), 'o')
        self.assertEqual(self.Game.board.board[1][1], 'x')

    def test_check_same_box_valid(self):
        self.Game.board.mark_square(int(1), int(1), 'x')
        self.Game.board.mark_square(int(1), int(1), 'o')
        self.assertEqual(self.Game.board.board[1][1], 'x')

    def test_cat_game(self):
        self.Game.board.mark_square(int(0), int(0), 'o')
        self.Game.board.mark_square(int(0), int(1), 'x')
        self.Game.board.mark_square(int(0), int(2), 'o')
        self.Game.board.mark_square(int(1), int(1), 'x')
        self.Game.board.mark_square(int(1), int(0), 'o')
        self.Game.board.mark_square(int(2), int(0), 'o')
        self.Game.board.mark_square(int(1), int(2), 'x')
        self.Game.board.mark_square(int(2), int(2), 'o')
        self.Game.board.mark_square(int(2), int(1), 'o')
        self.assertFalse(self.Game.board.mark_square(0,0,'x'))

if __name__ == '__main__':
    unittest.main()