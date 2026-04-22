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
            raise Exception('This column is full')
        
        for row_index in range(self.height):
            if row_index < self.height - 1 and self.board[row_index + 1][col_index] == self.empty_cell:
                continue
            break

        self.board[row_index][col_index] = self.current_player

        if self.check_win(row_index, col_index, self.current_player):
            print(f"The player {self.current_player} won!")
            return self.current_player
        
        self.current_player = (self.player_1 if self.current_player == self.player_2 else self.player_2)
    
    
    def check_win(self, row_index, col_index, current_player):
        row = []
        for c in range(col_index - 3, col_index + 4):
            if 0 <= col_index < self.width:
                row.append(self.board[row_index][c])
        
        if current_player * 4 in ''.join(row):
            return True
        
        col = []
        for r in range(row_index - 3, row_index + 4):
            if 0 <= r < self.height:
                col.append(self.board[r][col_index])
        
        if current_player * 4 in ''.join(col):
            return True
        
        diag_dec = []
        for i in range(-3, 4):
            r = row_index + i
            c = col_index + 1
            if 0 <= r < self.height and 0 <= col_index < self.width:
                diag_dec.append(self.board[r][c])
            
        
        if current_player * 4 in ''.join(diag_dec):
            return True
        
        diag_inc = []
        for i in range(-3, 4):
            r = row_index + i
            c = col_index - i
            if 0 <= r < self.height and 0 <= col_index < self.width:
                diag_inc.append(self.board[r][c])
        
        if current_player * 4 in ''.join(diag_inc):
            return True
    
        return False

    

t = TestConnect4()
t.setup_method()
t.test_row()

def play_console():
    player_name_1 = str(input("Type the name for the first player: "))
    player_name_2 =  str(input("Type the name for the second player: "))
    game = Connect4(player_1=player_name_1, player_2=player_name_2)
    try:
        game.display()
        while True:
            col = int(input(f"The player {game.current_player} has to select a column: "))
            play = game.play(col)
            game.display()

            if play:
                print("Match finished!")
                return
    except:
        raise Exception(f"Error")   

play_console() 
    