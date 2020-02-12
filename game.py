from player import Player
from board import Board

class Game(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = Board()
        self.p1 = Player('x')
        self.p2 = Player('o')
        self.win = 0
        #print(self.board)

    def player_play(self, p):
        if p == 1:
            self.p1.get_move()
            r, c = self.p1.player_move()
            s = self.p1.player_symbol()
            self.board.mark_square(r, c, s)
            self.board.has_winner(s)
        elif p == 2:
            self.p2.get_move() 
            r, c = self.p2.player_move()
            s = self.p2.player_symbol()
            self.board.mark_square(r, c, s)
            self.board.has_winner(s)

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        p = 1
        while self.win == 0:
            self.player_play(p)
            print(self.board.board)
            if p == 1:
                p = 2
            else:
                p = 1
            self.win = self.board.has_winner('x' if p == 1 else 'o')
        if self.win == 1:
            return "Player 1"
        elif self.win == 2:
            return "Player 2"

if __name__ == '__main__':
    game = Game()
    winner = game.play_game()
    print("{} has won!".format(winner))