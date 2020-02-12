import unittest
from tictactoe import Board

class TestTicTacToeMethods(unittest.TestCase):

    def setUp(self):
        self.Board = Board()

    def test_mark_square_x(self):
        self.Board.mark_square(int(2), int(1), 'X')
        self.assertEqual(self.Board.board[1][2], 'X')

    def test_mark_square_o(self):
        self.Board.mark_square(int(1), int(2), 'O')
        self.assertEqual(self.Board.board[2][1], 'O')

    def test_has_winner_horizontal(self):
        self.Board.mark_square(int(1), int(1), 'X')
        self.Board.mark_square(int(0), int(1), 'X')
        self.Board.mark_square(int(2), int(1), 'X')
        self.assertTrue(self.Board.has_winner())
        
    def test_has_winner_diagonal(self):
        self.Board.mark_square(int(0), int(0), 'X')
        self.Board.mark_square(int(1), int(1), 'X')
        self.Board.mark_square(int(2), int(2), 'X')
        self.assertTrue(self.Board.has_winner())

    def test_has_winner_vertical(self):
        self.Board.mark_square(int(0), int(0), 'X')
        self.Board.mark_square(int(0), int(1), 'X')
        self.Board.mark_square(int(0), int(2), 'X')
        self.assertTrue(self.Board.has_winner())

    def test_legal_move_false(self):
        self.assertFalse(self.Board.mark_square(int(3), int(3), 'X'))

    def test_legal_move_true(self):
        self.assertTrue(self.Board.mark_square(int(1), int(2), 'X'))

if __name__ == '__main__':
    unittest.main()