import pygame
from gameboard import GameBoard
from boarddata import BoardData
from copy import deepcopy

BOARD_SIZE = 630

class Sudoku:
    def __init__(self, board):
        # set up basic game parameters
        self.x = 0
        self.y = 0
        self.cell = int(BOARD_SIZE / 9)
        self.box = 3 * self.cell + 1

        # initiate pygame
        pygame.font.init()
        self.number_font = pygame.font.SysFont("Helvetica", 35)
        self.display_font = pygame.font.SysFont("Helvetica", 20, bold = True)
        self.title_font = pygame.font.SysFont("Helvetica", 50, bold = True)
        self.main_window = pygame.display.set_mode((BOARD_SIZE + 2, BOARD_SIZE + 50))
        pygame.display.set_caption("SUDOKU GAME")
        sudoku_icon = pygame.image.load("icon/sudoku_icon.png")
        pygame.display.set_icon(sudoku_icon)
        
        # set up cell and box selection parameters
        self.game = GameBoard(board)
        self.selectbox = pygame.Rect((0, 0, self.cell + 1, self.cell + 1))
        self.h_background = pygame.Rect((0, 0, self.cell + 1, BOARD_SIZE))
        self.v_background = pygame.Rect((0, 0, BOARD_SIZE, self.cell + 1))
        self.cell_background = pygame.Rect((0, 0, self.cell + 1, self.cell + 1))
        self.box_background = pygame.Rect((0, 0, self.box, self.box))
    
    def mouse_pos(self, pos):
        if pos[0] < BOARD_SIZE and pos[1] < BOARD_SIZE:
            self.x = int(pos[0] // self.cell)
            self.y = int(pos[1] // self.cell)
            print(self.x, self.y)
            # update selection box
            self.selectbox.x = self.x * self.cell
            self.selectbox.y = self.y * self.cell
            # update horizontal background
            self.h_background.x = self.x * self.cell
            self.h_background.y = 0
            # update vertical background
            self.v_background.x = 0
            self.v_background.y = self.y * self.cell
            # update box background
            self.box_background.x = (self.x // 3) * self.box
            self.box_background.y = (self.y // 3) * self.box
            # update cell background
            self.cell_background.x = self.x * self.cell
            self.cell_background.y = self.y * self.cell
    
    def move_selectbox(self, dx, dy):
        if dx < 0: 
            self.x = max(0, self.x - 1)
        elif dx > 0: 
            self.x = min(8, self.x + 1)
        if dy < 0: 
            self.y = max(0, self.y - 1)
        elif dy > 0: 
            self.y = min(8, self.y + 1)
        print(self.x, self.y)
        # update selection box
        self.selectbox.x = self.x * self.cell
        self.selectbox.y = self.y * self.cell
        # update horizontal background
        self.h_background.x = self.x * self.cell
        self.h_background.y = 0
        # update vertical background
        self.v_background.x = 0
        self.v_background.y = self.y * self.cell
        # update box background
        self.box_background.x = (self.x // 3) * self.box
        self.box_background.y = (self.y // 3) * self.box
        # update cell background
        self.cell_background.x = self.x * self.cell
        self.cell_background.y = self.y * self.cell
    
    def draw_selectbox(self):
        pygame.draw.rect(self.main_window, (0, 0, 0), self.selectbox, 1)
    
    def draw_background(self):
        self.main_window.fill((255,255,255))
        pygame.draw.rect(self.main_window, (210, 210, 210), self.h_background)
        pygame.draw.rect(self.main_window, (210, 210, 210), self.v_background)
        pygame.draw.rect(self.main_window, (210, 210, 210), self.box_background)
        pygame.draw.rect(self.main_window, (180, 180, 180), self.cell_background)

    def draw_board(self):
        for i in range(10):
            if i % 3 != 0:
                color = (150, 150, 150)
                thick = 1
                pygame.draw.line(self.main_window, color, (0, i * self.cell), (BOARD_SIZE, i * self.cell), thick)
                pygame.draw.line(self.main_window, color, (i * self.cell, 0), (i * self.cell, BOARD_SIZE), thick)
        for i in range(10):
            if i % 3 == 0:
                color = (0, 0, 0)
                thick = 2
                pygame.draw.line(self.main_window, color, (0, i * self.cell), (BOARD_SIZE, i * self.cell), thick)
                pygame.draw.line(self.main_window, color, (i * self.cell, 0), (i * self.cell, BOARD_SIZE), thick)
        for i in range(9): 
            for j in range(9): 
                if self.game.user_board[i][j] != 0: 
                    if self.game.question_board[i][j] != 0: 
                        color = (0, 0, 0)
                    else: 
                        color = (10, 100, 200)
                    text = self.number_font.render(str(self.game.user_board[i][j]), 1, color)
                    self.main_window.blit(text, (j * self.cell + 26, i * self.cell + 20))

def main():
    data = BoardData()
    sudoku = Sudoku(data.boards[0][0])
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                sudoku.mouse_pos(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sudoku.move_selectbox(-1, 0)
                if event.key == pygame.K_RIGHT:
                    sudoku.move_selectbox(1, 0)
                if event.key == pygame.K_UP:
                    sudoku.move_selectbox(0, -1)
                if event.key == pygame.K_DOWN:
                    sudoku.move_selectbox(0, 1)
                if event.key == pygame.K_1:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 1)
                if event.key == pygame.K_2:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 2)
                if event.key == pygame.K_3:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 3)
                if event.key == pygame.K_4:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 4)
                if event.key == pygame.K_5:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 5)
                if event.key == pygame.K_6:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 6)
                if event.key == pygame.K_7:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 7)
                if event.key == pygame.K_8:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 8)
                if event.key == pygame.K_9:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 9)
                if event.key == pygame.K_RETURN:
                    sudoku.game.solvegame()
                if event.key == pygame.K_BACKSPACE:
                    sudoku.game.update_cell(sudoku.x, sudoku.y, 0)
        sudoku.draw_background()
        sudoku.draw_board()
        sudoku.draw_selectbox()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
