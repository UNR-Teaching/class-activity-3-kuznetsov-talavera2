class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.r = -1
        self.c = -1
        self.win = False

    def get_move(self):
        self.r, self.c = input("What is your move? ").split()
        self.r = int(self.r)
        self.c = int(self.c)

    def player_move(self):
        if self.r == -1 or self.c == -1:
            return None
        return int(self.r), int(self.c)

    def player_symbol(self):
        return self.symbol

    def win(self, win=False):
        self.win = win
        return self.win