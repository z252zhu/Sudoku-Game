from boarddata import BoardData
from copy import deepcopy

class GameBoard:
    def __init__(self, board):
        self.boards = BoardData().boards
        self.user_board = deepcopy(self.boards[0][0])
        self.question_board = deepcopy(self.boards[0][0])
    
    def select_board(self, diffculty, map_id):
        self.user_board = deepcopy(self.boards[diffculty][map_id])
        self.question_board = deepcopy(self.boards[diffculty][map_id])
    
    def update_cell(self, x, y, number):
        if number == 0:
            self.user_board[y][x] = number
        if self.question_board[y][x] == 0 and self.user_board[y][x] == 0:
            self.user_board[y][x] = number
    
    def validvalue(self, r, c, x): 
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
    
    def solvegame(self):
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
                if self.validvalue(r, c, value): 
                    self.user_board[r][c] = value
                    if solve():
                        return True
                    self.user_board[r][c] = 0
            return False

        return solve()
    
    def print(self):
        for r in self.user_board:
            print(r)
