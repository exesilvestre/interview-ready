class TestConnect4:
    def setup_method(self):
        self.game =  Connect4()
    
    def test_row(self):
        assert self.game.play(0) is None
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(1) is None
        assert self.game.play(2) is None
        assert self.game.play(2) is None
        assert self.game.play(3) == "A"
        self.game.display()
    
    def test_col(self):
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(0) == "A"
        self.game.display()
    
    def test_inc_diag(self):
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(1) is None
        assert self.game.play(2) is None
        assert self.game.play(2) is None
        assert self.game.play(3) is None
        assert self.game.play(2) is None
        assert self.game.play(3) is None
        assert self.game.play(3) is None
        assert self.game.play(5) is None
        assert self.game.play(3) == "A"
        self.game.display()
    

    def test_dec_diag(self):
        assert self.game.play(6) is None
        assert self.game.play(5) is None
        assert self.game.play(5) is None
        assert self.game.play(4) is None
        assert self.game.play(4) is None
        assert self.game.play(3) is None
        assert self.game.play(4) is None
        assert self.game.play(3) is None
        assert self.game.play(3) is None
        assert self.game.play(0) is None
        assert self.game.play(3) == "A"
        self.game.display()


    def test_no_winner(self):
        assert self.game.play(0) is None
        assert self.game.play(2) is None
        assert self.game.play(5) is None
        assert self.game.play(1) is None
        assert self.game.play(4) is None
        assert self.game.play(6) is None
        assert self.game.play(1) is None
        assert self.game.play(6) is None
        self.game.display()       

class Connect4:
    def __init__(self, width = 7, height = 5, player_1 = 'A', player_2 = 'B', empty_cell = '-'):
        self.width = width
        self.height = height
        self.player_1 = player_1
        self.player_2 = player_2
        self.empty_cell = empty_cell
        self.board = [[empty_cell for _ in range(width)] for _ in range(height)]
        self.current_player = player_1

    
    def display(self):
        print(' ', *list(range(self.width)))
        for i, row in enumerate(self.board):
            print(i, *row)
    
    def play(self, col_index):
        row_index = 0
        if self.board[row_index][col_index] != self.empty_cell:
            raise Exception(f'Column {col_index} is full')

        for row_index in range(self.height):
            if row_index < self.height - 1 and self.board[row_index + 1][col_index] == self.empty_cell:
                continue
            break

        self.board[row_index][col_index] = self.current_player

        if self.check_winner(self.current_player, row_index, col_index):
            print(f"The {self.current_player} won!")
            return self.current_player

        self.current_player = (self.player_1 if self.current_player == self.player_2 else self.player_2)
    

    def check_winner(self, player, row_index, col_index):
        row = self.board[row_index]
        col = [self.board[i][col_index] for i in range(self.height)]
        diag_inc = self.make_diag_inc(row_index, col_index)
        diag_dec = self.make_diag_dec(row_index, col_index)

        lines = row, col, diag_dec, diag_inc

        return any(player * 4 in ''.join(line) for line in lines )


    def make_diag_dec(self, row_index, col_index):
        diag_dec = []
        r, c = row_index, col_index
        while r > 0 and c > 0:
            r -= 1
            c -= 1
        
        while r < self.height and c < self.width:
            diag_dec.append(self.board[r][c])
            r += 1
            c += 1
        return diag_dec
    
    def make_diag_inc(self, row_index, col_index):
        diag_inc = []
        r, c = row_index, col_index
        while r < self.height - 1 and c > 0:
            r += 1
            c -= 1
        
        while r > 0 and c < self.width:
            diag_inc.append(self.board[r][c])
            r -= 1
            c += 1
        
        return diag_inc


c = Connect4()
c.display()


t = TestConnect4()
t.setup_method()

t.test_col()
