#OTHELLO
#Christopher Christian 52697582
BLACK_PIECE = '@'
WHITE_PIECE = 'O'
EMPTY_SPACE = '.'
class OthelloBoard:
    def __init__(self, rows, cols, player, top_right, win):
        self.board = []
        self.rows = rows
        self.cols = cols
        self.player = player
        self.opposite = self.opp_player(self.player)
        self.top_right_corner = top_right
        self.win_condition = win
        self.generate(self.board, self.rows, self.cols)
        

    def get_rows(self):
        while True:
            no_of_rows = int(input("How many rows would you like (4-16)? "))
            if no_of_rows < 4 or no_of_rows > 16 or no_of_rows %2 !=0:
                print("ERROR: INVALID INPUT SPECIFIED")
            else:
                return no_of_rows

    def get_cols(self):
        while True:
            no_of_cols = int(input("How many columns would you like (4-16)? "))
            if no_of_cols < 4 or no_of_cols > 16 or no_of_cols %2 !=0:
                print("ERROR: INVALID INPUT SPECIFIED")
            else:
                return no_of_cols


    def start(self):
        while True:
            starting_player = input("Enter who will start first: Black or White ")
            if starting_player.upper() != 'BLACK' and starting_player.upper() != 'WHITE':
               print("ERROR: INVALID INPUT SPECIFIED")
            else:
                if starting_player.upper() == 'BLACK':
                    return BLACK_PIECE
                else:
                    return WHITE_PIECE

    def top_right(self):
        while True:
            top_right_space = input("Who will be in the top right corner: Black or White? ")
            if top_right_space.upper() != 'BLACK' and top_right_space.upper() != 'WHITE':
                print("ERROR: INVALID INPUT SPECIFIED")
            else:
                return top_right_space

    def win_cond(self):
        while True:
            win_cond = input("What will determine the winner: LOW score or HIGH score? ")
            if win_cond.upper() != 'LOW' and win_cond.upper() != 'HIGH':
                print("ERROR: INVALID INPUT SPECIFIED")
            else:
                return win_cond


    def change_player(self, player):
        return self.opp_player(player)
        

    def opp_player(self, player):
        if player == BLACK_PIECE:
            return WHITE_PIECE
        else:
            return BLACK_PIECE
    
    def valid_move(self, board, row, col):
        if board[row][col] != EMPTY_SPACE:
                    return False
        flip_tiles = []
        for rowdir, coldir in [[0, 1], [1,1], [1,0],[1,-1],[0, -1], [-1,-1],[-1, 0], [-1, 1]]:
            rows = row
            cols = col
            rows +=rowdir
            cols+=coldir
            if self.on_board(rows, cols) and board[rows][cols] == self.opposite:
                rows+=rowdir
                cols+=coldir
                if not self.on_board(rows,cols):
                    continue
                while board[rows][cols]== self.opposite:
                    rows+=rowdir
                    cols+=coldir
                    if not self.on_board(rows,cols):
                        break
                if not self.on_board(rows,cols):
                    continue
                if board[rows][cols] == self.player:
                    while True:
                        rows -=rowdir
                        cols -=coldir
                        if rows == row and cols == col:
                            break
                        flip_tiles.append([rows,cols])
        if len(flip_tiles) == 0:
                return False
        return flip_tiles
                
           
    
    def on_board(self, row, col):
        return row >=0 and row < self.rows and col >= 0 and col < self.cols
                            


    def build_valid_moves_list(self, player):
        valid_moves = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.valid_move(self.board, row, col):
                   valid_moves.append([row, col])
                
                
        return valid_moves
        

    def current_player(self):
        if self.player == BLACK_PIECE:
            return "TURN: BLACK"
        else:
            return "TURN: WHITE"

    def generate(self, board, rows, cols):
        
        for i in range(rows):
            board.append([])
            for j in range(cols):
                board[i].append(EMPTY_SPACE)

        top = int(rows/2)-1 
        bottom = int(rows/2)
        left =  int(cols/2)-1
        right = int(cols/2)

        if self.top_right_corner == BLACK_PIECE:
            board[top][right] = BLACK_PIECE
            board[bottom][right] = WHITE_PIECE
            board[top][left] = WHITE_PIECE
            board[bottom][left] = BLACK_PIECE
        else:
            board[top][right] = WHITE_PIECE
            board[bottom][right] = BLACK_PIECE
            board[top][left] = BLACK_PIECE
            board[bottom][left] = WHITE_PIECE
        
    def print(self):
        for i in range(len(self.board)):
            print (self.board[i])

    def make_move(self, row, col):
            flipped_tiles = self.valid_move(self.board, row, col)
            self.board[row][col] = self.player
            for rows, cols in flipped_tiles:
                self.board[rows][cols] = self.player
            
            if len(self.build_valid_moves_list( self.player)) == 0:
                if len(self.build_valid_moves_list( self.opposite)) == 0:
                    self.winner()
                else:
                    self.player = self.opp_player(self.player)
                    self.opposite = self.opp_player(self.player)
            self.player = self.opp_player(self.player)
            self.opposite = self.opp_player(self.player)
       
                

    def score(self, player):
        score = 0
        for rows in range(len(self.board)):
            for cols in range(len(self.board[0])):
                if self.board[rows][cols] == player:
                    score+=1
        return score

    def winner(self):
        current_player = ''
        opposing_player = ''
        if self.player == BLACK_PIECE:
            current_player = 'Black'
            opposing_player = 'White'
        else:
            player = 'White'
            opp_player = 'Black'
        if self.win_condition == 'Highest Score':
            if self.score(self.player) > self.score(self.opposite):
                return (current_player + " Wins!")
            else:
                return (opposing_player + " Wins!")
        else:
            if self.score(self.player) < self.score(self.opposite):
                return (current_player+" Wins!")
            else:
                return (opposing_player + " Wins!")
    
    


def InvalidInputError(Exception):
    print("INVALID INPUT ENTERED")













