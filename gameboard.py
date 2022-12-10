from boarddata import BoardData
from copy import deepcopy
import bisect

class GameBoard:
    def __init__(self):
        self.boards = BoardData().boards
        self.user_board = []
        self.question_board = []
        self.note_board = [[[] for i in range(9)] for j in range(9)]
        self.cells_left = 81
    
    def get_cells_left(self):
        res = 0
        for r in self.question_board:
            for c in r:
                if c == 0:
                    res += 1
        return res
    
    def select_board(self, diffculty, board_id):
        self.user_board = deepcopy(self.boards[diffculty][board_id])
        self.question_board = deepcopy(self.boards[diffculty][board_id])
        self.cells_left = self.get_cells_left()
    
    def update_cell(self, x, y, number):
        if (self.question_board[y][x] == 0 and 
            self.user_board[y][x] != 0 and 
            number == 0):
            self.user_board[y][x] = number
            self.cells_left += 1
        if self.question_board[y][x] == 0 and self.user_board[y][x] == 0:
            self.user_board[y][x] = number
            self.note_board[y][x].clear()
            self.cells_left -= 1
    
    def update_note(self, x, y, number):
        if self.user_board[y][x] == 0:
            if number in self.note_board[y][x]:
                self.note_board[y][x].remove(number)
            else:
                bisect.insort(self.note_board[y][x], number)
            return True
        return False
    
    def valid_value(self, r, c, x):
        if x == 0:
            return True
        
        if x in self.user_board[r]:
            return False
                    
        for row in self.user_board:
            if row[c] == x: 
                return False
            
        box_r, box_c = (r // 3) * 3, (c // 3) * 3
        for row in range(box_r, box_r + 3): 
            for col in range(box_c, box_c + 3): 
                if x == self.user_board[row][col]:
                    return False
        return True
    
    def solve_game(self):
        self.cells_left = 0

        def find_unassign():
            for r in range(9):
                for c in range(9):
                    if self.user_board[r][c] == 0: 
                        return r, c
            return -1, -1
        
        def solve():
            r, c = find_unassign()
            if r == -1 and c == -1:
                return True
            
            for value in range(1, 10):
                if self.valid_value(r, c, value): 
                    self.user_board[r][c] = value
                    if solve():
                        return True
                    self.user_board[r][c] = 0
            return False

        return solve()
    
    def reset_board(self):
        self.cells_left = self.get_cells_left()
        self.user_board = deepcopy(self.question_board)
    
    def print(self):
        for r in self.user_board:
            print(r)
