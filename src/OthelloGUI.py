##MISSING DOCUMENTATION
#Christopher Christian 52697582
#Othello Graphical User Interface
from Othelloclass_module import *

import tkinter

class OthelloBox:            
    def __init__(self):
        Default = ('Helvetica', 14)
        self._rows = 0
        self._cols = 0
        self._win_options = ''
        self._top_right = ''
        self._start_first = ''

        number_options = [ 4, 6, 8, 10, 12, 14, 16]
        win_options = ['Highest Score', 'Lowest Score']
        top_right_options = ['Black', 'White']
        start_first = ['Black', 'White']
        
        self.dialog_window = tkinter.Toplevel()
        
        self.rowvar = tkinter.StringVar()
        self.rowvar.set(number_options[0])

        self.colvar = tkinter.StringVar()
        self.colvar.set(number_options[0])

        self.startfirst = tkinter.StringVar()
        self.startfirst.set(start_first[0])

        self.win = tkinter.StringVar()
        self.win.set(win_options[0])

        self.top_right = tkinter.StringVar()
        self.top_right.set(top_right_options[0])

        no_of_rows_label = tkinter.Label(
            master = self.dialog_window, text ='How many rows would you like?',
            font = Default)
        no_of_rows_label.grid(row = 0, column = 0, padx = 10, pady = 10,
                              sticky = tkinter.N+tkinter.W)

        no_of_cols_label = tkinter.Label(
            master = self.dialog_window, text = "How many columns would you like?",
            font = Default)
        no_of_cols_label.grid(row = 1, column = 0, padx = 10, pady = 10,
                        sticky = tkinter.N+tkinter.W)

        start_first_label = tkinter.Label(
            master = self.dialog_window, text = "Who would you like to start first?",
            font = Default)
        start_first_label.grid(row = 2, column = 0, padx = 10, pady = 10,
                               sticky = tkinter.N+tkinter.W)

        top_right_label = tkinter.Label(master = self.dialog_window, text = "Who will start in the top right?",
                                        font = Default)
        top_right_label.grid(row = 3, column = 0, padx = 10, pady = 10,
                             sticky = tkinter.N+tkinter.W)

        win_label = tkinter.Label(master = self.dialog_window, text = "Which should decide the winner?",
                                  font = Default)
        win_label.grid(row = 4, column = 0, padx = 10, pady = 10,
                       sticky = tkinter.N+tkinter.W)

        no_of_rows_option = tkinter.OptionMenu(self.dialog_window, self.rowvar, *number_options)
        no_of_rows_option.grid(row = 0, column = 1, padx = 10, pady = 10)

        no_of_cols_option = tkinter.OptionMenu(self.dialog_window, self.colvar, *number_options)
        no_of_cols_option.grid(row = 1, column = 1, padx = 10, pady = 10)

        start_first_option = tkinter.OptionMenu(self.dialog_window, self.startfirst, *start_first)
        start_first_option.grid(row = 2, column = 1, padx = 10, pady = 10)

        top_right_option = tkinter.OptionMenu(self.dialog_window, self.top_right, *top_right_options)
        top_right_option.grid(row = 3, column = 1, padx = 10, pady = 10)

        win_option = tkinter.OptionMenu(self.dialog_window, self.win, *win_options)
        win_option.grid(row = 4, column = 1, padx = 10, pady = 10)

        button_frame = tkinter.Frame(master = self.dialog_window)
        button_frame.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10)

        proceed_button = tkinter.Button(
            master = button_frame, text = 'PLAY', font = Default,
            command = self.proceed_button_pressed)
        proceed_button.grid(row = 0, column = 0, padx =10, pady = 10)

        self.proceed = False

    def proceed_button_pressed(self):
        self.proceed = True
        self._rows = self.rowvar.get()
        self._cols = self.colvar.get()
        self._start_first = self.startfirst.get()
        self._top_right = self.top_right.get()
        self._win_options = self.win.get()

        self.dialog_window.destroy()

    def was_proceed_clicked(self):
        return self.proceed

    def get_rows(self):
        return self._rows

    def get_cols(self):
        return self._cols

    def get_start(self):
        if self._start_first == 'Black':
            return BLACK_PIECE
        else:
            return WHITE_PIECE

    def get_top_right(self):
        if self._top_right == 'Black':
            return BLACK_PIECE
        else:
            return WHITE_PIECE

    def get_win_option(self):
        return self._win_options

    def show(self):
        self.dialog_window.grab_set()
        self.dialog_window.wait_window()



        
        
        

        



class OthelloApplication:
    def __init__(self):
        
        self.size = self.get_text_size(800,600)
        self.default = 'Helvetica'
        
        self.root_window = tkinter.Tk()
        
        self.canvas = tkinter.Canvas(self.root_window,
                                    width = 800, height = 600,
                                    background = '#006400')
                
        self.canvas.grid(
            row = 1, column = 0, 
            sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)

        self.root_window.rowconfigure(0, weight = 0)
        self.root_window.rowconfigure(1, weight = 1)
        self.root_window.rowconfigure(2, weight = 0)
        self.root_window.columnconfigure(0, weight = 1)
        self.display_header = tkinter.StringVar()

        play_button = tkinter.Button(master = self.root_window, text = "NEW GAME", command =
                                     self._on_play_pressed)
        play_button.grid(row = 2, column = 0,
                         sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)

    def _on_play_pressed(self):
        self.get_info()
        self.canvas.bind('<Configure>', self._on_canvas_resize)
        self.canvas.bind('<Button-1>', self.on_mouse_click)

    def start(self):
        self.root_window.mainloop()
        
        

    def get_info(self):
        pre_play = OthelloBox()
        pre_play.show()
        if pre_play.was_proceed_clicked:
            self.rows = int(pre_play.get_rows())
            self.columns = int(pre_play.get_cols())
            self.starting_player = pre_play.get_start()
            self.top_right_player = pre_play.get_top_right()
            self.win_condition = pre_play.get_win_option()
            
            self.gameboard = OthelloBoard(self.rows, self.columns, self.starting_player, self.top_right_player,
                                 self.win_condition)
            self.board = self.gameboard.board
            self.draw_squares(800,600)
            self.update()
        

    def get_text_size(self,WIDTH,HEIGHT):
            return int(WIDTH/100)+int(HEIGHT/100)
        

    def draw_squares(self, WIDTH, HEIGHT):
        box_height = HEIGHT/self.columns
        box_width = WIDTH/self.rows
        self.squarelist = []
        self.num = -1
        self.x = 0
        for i in range(self.rows):
            self.y = 0
            self.squarelist.append([])
            for j in range(self.columns):
                if self.num == -1:
                    color = "#228B22"
                else:
                    color = "#006400"
                self.canvas.create_rectangle(self.x, self.y, self.x+box_width,
                                             self.y+box_height, fill = color)
                self.squarelist[i].append([self.x, self.y, self.x+box_width, self.y+box_height])
                
                self.y+=box_height
                self.num = -(self.num)
                
            self.x+=box_width
            self.num = -(self.num)
            

    def scores(self):
        
        self.black_score = tkinter.StringVar()
        self.white_score = tkinter.StringVar()
        
        self.black_score.set("BLACK: "+str(self.gameboard.score(BLACK_PIECE)))
        self.white_score.set("WHITE: "+str(self.gameboard.score(WHITE_PIECE)))
        
        black_score_label = tkinter.Label(
            master = self.root_window, textvariable = self.black_score,
            font = (self.default, self.size))
        
        black_score_label.grid(row = 2, column = 0,
                               sticky = tkinter.S+tkinter.W+tkinter.N)

        white_score_label = tkinter.Label(
            master = self.root_window, textvariable = self.white_score,
            font = (self.default, self.size))
        white_score_label.grid(row = 2, column = 0,
                               sticky = tkinter.S+tkinter.E+tkinter.N)
    def display(self):
      
        
        if len(self.gameboard.build_valid_moves_list(self.gameboard.player)) > 0 or len(self.gameboard.build_valid_moves_list(self.gameboard.opposite)) > 0:
            self.display_header.set(self.gameboard.current_player())
        else:
            
            self.display_header.set(self.gameboard.winner())
            
        display_header_label = tkinter.Label(
            master = self.root_window, textvariable = self.display_header,
            font = (self.default, self.size))
        display_header_label.grid(row = 0, column = 0,
                                sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)
        

    def print_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j]!= '.':
                    if self.board[i][j] == '@':
                        self.canvas.create_oval(self.squarelist[i][j][0],
                                                self.squarelist[i][j][1],
                                                self.squarelist[i][j][2],
                                                self.squarelist[i][j][3],
                                                fill = "Black")
                    else:
                        self.canvas.create_oval(self.squarelist[i][j][0],
                                                self.squarelist[i][j][1],
                                                self.squarelist[i][j][2],
                                                self.squarelist[i][j][3],
                                                fill = "White")

    def _on_canvas_resize(self, event):
        self._redraw_all_objects()

    def _redraw_all_objects(self):
        self.canvas.delete(tkinter.ALL)
    
        WIDTH = self.canvas.winfo_width()
        HEIGHT = self.canvas.winfo_height()

        self.size = self.get_text_size(WIDTH, HEIGHT)
        self.draw_squares(WIDTH, HEIGHT)
        self.update()
        

    def on_mouse_click(self, event):
        x = event.x
        y = event.y
        
        for i in range(self.rows):
            for j in range(self.columns):
                square_x1 = self.squarelist[i][j][0]
                square_x2 = self.squarelist[i][j][2]
                square_y1 = self.squarelist[i][j][1]
                square_y2 = self.squarelist[i][j][3]
                if x >= square_x1 and x <= square_x2 and y >= square_y1 and y <= square_y2:
                    if self.board[i][j] == EMPTY_SPACE:
                        if self.gameboard.valid_move(self.board, i, j):
                            self.gameboard.make_move(i, j)
                            self.update()
                            
                            

        
                                
    def update(self):
        self.display()
        self.print_board()
        self.scores()
     
        
                            
    
        
        
        
            
    

OthelloApplication = OthelloApplication()
OthelloApplication.start()

