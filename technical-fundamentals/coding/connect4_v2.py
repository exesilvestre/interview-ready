class TestConnect4:
    def setup_method(self):
        self.game =  Connect4()
    
    def test_row(self):
        assert self.game.play(0) is None
        self.game.display()
        assert self.game.play(0) is None
        self.game.display()
        assert self.game.play(1) is None
        self.game.display()
        assert self.game.play(1) is None
        self.game.display()
        assert self.game.play(2) is None
        self.game.display()
        assert self.game.play(2) is None
        self.game.display()
        assert self.game.play(3) == "X"
        self.game.display()
    
    def test_col(self):
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(0) is None
        assert self.game.play(1) is None
        assert self.game.play(0) == "X"
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
        assert self.game.play(3) == "X"
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
        assert self.game.play(3) == "X"
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
    def __init__(self, width = 8, height = 8, player_1 = 'X', player_2 = 'Y', empty_cell = '-'):
        self.width = width
        self.height = height
        self.player_1 = player_1
        self.player_2 = player_2
        self.empty_cell = empty_cell
        self.board = [[empty_cell for _ in range(self.width)] for _ in range(self.height)]
        self.current_player = player_1
    
    def display(self):
        print(' ', *list(range(self.width)))

        for i, row in enumerate(self.board):
            print(i, *row)

    
    def play(self, col):
        row_index = 0

        if self.board[row_index][col] != self.empty_cell:
            raise Exception(f"The column {col} is full")

        for row_index in range(self.height):
            if row_index < self.height - 1 and self.board[row_index + 1][col] == self.empty_cell:
                continue
            break

        self.board[row_index][col] = self.current_player

        if self.check_winner(row_index, col, self.current_player):
            print(f"The player {self.current_player} has won!")
            return self.current_player
    
        self.current_player = self.player_2 if self.current_player == self.player_1 else self.player_1
    

    def check_winner(self, row_index, col_index, current_player):
        # Horizontal
        row = []
        for c in range(-3, 4):
            col = col_index + c
            if col >= 0 and col < self.width:
                row.append(self.board[row_index][col])
        
        if self.check_4_in_arrow(row, current_player):
            return True 
        
 # Vertical - we need to evaluate de col 7 approaches
        col =[]
        for r in range(-3, 4):
            row = row_index + r
            if row >= 0 and row < self.height:
                col.append(self.board[row][col_index])
        
        if self.check_4_in_arrow(col, current_player):
            return True 

        # Diag Inc 
        diag_inc = []
        for i in range(-3, 4):
            r = row_index - i
            c = col_index + i
            if r >= 0 and r < self.height and c >= 0 and c < self.width:
                diag_inc.append(self.board[r][c])
            
        if self.check_4_in_arrow(diag_inc, current_player):
            return True
        
        # Diag dec 
        diag_dec = []
        for i in range(-3, 4):
            r = row_index + i
            c = col_index + i
            if r >= 0 and c >= 0 and r < self.height and c < self.height:
                diag_dec.append(self.board[r][c])
            
        if self.check_4_in_arrow(diag_dec, current_player):
            return True
        

    def check_4_in_arrow(self, arr, current_player):
        if current_player * 4 in ''.join(arr):
            return True
        else:
            return False


t = TestConnect4()
t.setup_method()
t.game.display()
t.test_row()

def play_console():
    while True:
        player_1 = str(input("Select a letter to representate player 1: "))
        player_2 = str(input("Select a letter to representate player 2: "))
        game =Connect4(player_1=player_1, player_2=player_2)
        while True:
            try:
                game.display()
                col = int(input(f"Player {game.current_player} select a column: "))
                winner = game.play(col)
                if winner:
                    print("Match ended")
                    break
            except Exception as e:
                print(f"Error: {e}")
                print("Please select a valid column.")
                continue
        play_again = str(input("Would you like to play again? (y/n): ")).lower()
        while play_again not in ['y', 'n']:
            play_again = str(input("Would you like to play again? (y/n): ")).lower()

        if play_again == 'n':
            break
    
    
play_console()
