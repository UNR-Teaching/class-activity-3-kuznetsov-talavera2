from player import Player
import numpy as np

class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = np.chararray((3,3), unicode=True)
        self.board[:] = '_'
        # self.p1 = Player('x')
        # self.p2 = Player('o')
        self.win = 0
        #print(self.board)
        

    def mark_square(self, r, c, sym):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to markif __name__ == '__main__': board = Board() winner = board.play_game() print("{} has won!".format(winner))
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        if c < 3 and r < 3 and self.board[r][c] == '_':
            legal = True
        else:
            legal = False
        if legal:
            self.board[r][c] = sym
        #print(self.board)
        return legal
        

    def has_winner(self, symbol):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        # horizontals
        for i in range(3):
            row = self.board[i]
            if row[0] != '_' and row[0] == row[1] and row[0] == row[2]:
                if row[0] == symbol and symbol == 'x':
                    self.win = 1
                elif row[0] == symbol and symbol == 'o':
                    self.win = 2
        # verticals        
        for i in range(3):
            row = self.board[:, i]
            if row[0] != '_' and row[0] == row[1] and row[0] == row[2]:
                if row[0] == symbol and symbol == 'x':
                    self.win = 1
                elif row[0] == symbol and symbol == 'o':
                    self.win = 2
        # check diagonals
        if self.board[0][0] != '_' and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            if self.board[1][1] == symbol and symbol == 'x':
                    self.win = 1
            elif self.board[1][1] == symbol and symbol == 'o':
                    self.win = 2
        if self.board[0][2] != '_' and self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1]:
            if self.board[1][1] == symbol and symbol == 'x':
                    self.win = 1
            elif self.board[1][1] == symbol and symbol == 'o':
                    self.win = 2
        return self.win
        

    # def play_game(self):
    #     """
    #     Takes moves from raw_input as comma-separated list in form (column, row, player)
    #         and makes a move. When a winner has been determined, the game ends
        
    #     :return: (str) the letter representing the player who won
    #     """
    #     p = 1
    #     while self.win == 0:
    #         if p == 1:
    #             self.p1.get_move()
    #             r, c = self.p1.player_move()
    #             s = self.p1.player_symbol()
    #             self.mark_square(r, c, s)
    #             self.has_winner(s)
    #         elif p == 2:
    #             self.p2.get_move() 
    #             r, c = self.p2.player_move()
    #             s = self.p2.player_symbol()
    #             self.mark_square(r, c, s)
    #             self.has_winner(s)
    #         print(self.board)
    #         if p == 1:
    #             p = 2
    #         else:
    #             p = 1
    #     if self.win == 1:
    #         return "Player 1"
    #     elif self.win == 2:
    #         return "Player 2"


# if __name__ == '__main__':
#     board = Board()
#     winner = board.play_game()
#     print("{} has won!".format(winner))