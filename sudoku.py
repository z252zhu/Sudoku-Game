import pygame
import time
from gameboard import GameBoard

BOARD_SIZE = 630

class Sudoku:
    def __init__(self):
        # set up basic game parameters
        self.game = GameBoard()
        self.difficulty = 0
        self.board_id = 0
        self.draw_status = 0
        self.max_board_id = len(self.game.boards[self.difficulty])
        self.x = 0
        self.y = 0
        self.msg = ""
        self.set_msg_timer = 0
        self.not_auto_solve = True
        self.game_finished = False
        self.cell = int(BOARD_SIZE / 9)
        self.box = 3 * self.cell + 1
        self.msg_pos = (10, BOARD_SIZE + 15)

        # initiate pygame
        pygame.font.init()
        self.number_font = pygame.font.SysFont("Helvetica", 35)
        self.msg_font = pygame.font.SysFont("Helvetica", 20, bold = True)
        self.title_font = pygame.font.SysFont("Helvetica", 50, bold = True)
        self.main_window = pygame.display.set_mode((BOARD_SIZE + 2, BOARD_SIZE + 50))
        pygame.display.set_caption("SUDOKU GAME")
        sudoku_icon = pygame.image.load("icon/sudoku_icon.png")
        pygame.display.set_icon(sudoku_icon)
        
        # set up cell and box selection parameters
        self.selectbox = pygame.Rect((0, 0, self.cell + 1, self.cell + 1))
        self.h_background = pygame.Rect((0, 0, self.cell + 1, BOARD_SIZE))
        self.v_background = pygame.Rect((0, 0, BOARD_SIZE, self.cell + 1))
        self.cell_background = pygame.Rect((0, 0, self.cell + 1, self.cell + 1))
        self.box_background = pygame.Rect((0, 0, self.box, self.box))
    
    def draw_msg(self):
        if time.time() - self.set_msg_timer < 5:
            text = self.msg_font.render(self.msg, 1, (0, 0, 0))
            self.main_window.blit(text, self.msg_pos)
    
    def draw_title(self):
        self.main_window.fill((255,255,255))
        # game title
        game_title = self.title_font.render("Sudoku Game", 1, (0, 0, 0))
        self.main_window.blit(game_title, (110, 250))
        # selection hint
        hint = self.msg_font.render("Press ENTER to select: ", 1, (0, 0, 0))
        self.main_window.blit(hint, (10, 600))
    
    def select_difficulty(self, selection):
        self.difficulty += selection
        if self.difficulty < 0:
            self.difficulty = 0
        elif self.difficulty > 4:
            self.difficulty = 4
    
    def draw_difficulty(self):
        str_difficulty = ["EASY", "MEDIUM", "HARD", "EXPERT", "EVIL"]
        if self.difficulty == 0:
            msg = " " * 4 + str_difficulty[self.difficulty] + " ->"
        elif self.difficulty in range(1, 4):
            msg = "<- " + str_difficulty[self.difficulty] + " ->"
        else:
            msg = "<- " + str_difficulty[self.difficulty]
        text = self.msg_font.render(msg, 1, (0, 0, 0))
        self.main_window.blit(text, self.msg_pos)

    def select_board(self, selection):
        self.board_id += selection
        self.max_board_id = len(self.game.boards[self.difficulty])
        if self.board_id < 0:
            self.board_id = 0
        elif self.board_id > self.max_board_id - 1:
            self.board_id = self.max_board_id
    
    def draw_board_id(self):
        str_board_id = str(self.board_id + 1)
        if self.board_id == 0: 
            msg = " " * 4 + str_board_id + " ->"
        elif self.board_id in range(1, self.max_board_id - 1):
            msg = "<- " + str_board_id + " ->"
        else:
            msg = "<- " + str_board_id
        text = self.msg_font.render(msg, 1, (0, 0, 0))
        self.main_window.blit(text, self.msg_pos)
    
    def update_selection_box(self, x, y, mouse_input):
        # mouse input
        if mouse_input:
            if x < BOARD_SIZE and y < BOARD_SIZE:
                self.x = int(x // self.cell)
                self.y = int(y // self.cell)
        # keyboard input
        else:
            if x < 0:
                self.x = max(0, self.x - 1)
            elif x > 0:
                self.x = min(8, self.x + 1)
            if y < 0:
                self.y = max(0, self.y - 1)
            elif y > 0:
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
    
    def try_number(self, number):
        if (self.game.question_board[self.y][self.x] != 0 or 
            self.game.user_board[self.y][self.x] != 0):
            self.msg = "Choose a different cell."
            self.set_msg_timer = time.time()
        elif not self.game.valid_value(self.y, self.x, number):
            self.msg = "Invalid number."
            self.set_msg_timer = time.time()
        else:
            self.game.update_cell(self.x, self.y, number)
    
    def try_note(self, number):
        if not self.game.update_note(self.y, self.x, number):
            self.msg = "Choose a different cell."
            self.set_msg_timer = time.time()
    
    def draw_selectbox(self):
        pygame.draw.rect(self.main_window, (0, 0, 0), self.selectbox, 1)
    
    def draw_background(self):
        self.main_window.fill((255,255,255))
        pygame.draw.rect(self.main_window, (210, 210, 210), self.h_background)
        pygame.draw.rect(self.main_window, (210, 210, 210), self.v_background)
        pygame.draw.rect(self.main_window, (210, 210, 210), self.box_background)
        pygame.draw.rect(self.main_window, (180, 180, 180), self.cell_background)
        self.draw_msg()

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
        for i in range(9): 
            for j in range(9): 
                if not self.game.note_board[i][j]:
                    color = (10, 100, 200)
                    text = self.number_font.render(str(self.game.user_board[i][j]), 1, color)
                    self.main_window.blit(text, (j * self.cell + 26, i * self.cell + 20))
    
    def check_result(self):
        if self.draw_status == 2 and self.game.cells_left == 0:
            self.draw_status += 1

    def solve_sudoku(self):
        self.not_auto_solve = False
        self.game.solve_game()
    
    def cheat_sudoku(self):
        # actually for debugging
        self.game.solve_game()

    def reset_sudoku(self):
        self.difficulty = 0
        self.board_id = 0
        self.draw_status = 0
        self.max_board_id = len(self.game.boards[self.difficulty])
        self.x = 0
        self.y = 0
        self.not_auto_solve = True
        self.game_finished = False

        # update selection box
        self.selectbox.x = 0
        self.selectbox.y = 0
        # update horizontal background
        self.h_background.x = 0
        self.h_background.y = 0
        # update vertical background
        self.v_background.x = 0
        self.v_background.y = 0
        # update box background
        self.box_background.x = 0
        self.box_background.y = 0
        # update cell background
        self.cell_background.x = 0
        self.cell_background.y = 0

    def draw_sudoku(self):
        self.check_result()
        self.draw_background()
        self.draw_board()
        self.draw_selectbox()
    
    def draw_result(self):
        self.main_window.fill((255,255,255))
        self.draw_board()
        if self.not_auto_solve:
            msg = "You Win!"
        else:
            msg = "Game Finished!"
        text = self.msg_font.render(msg, 1, (0, 0, 0))
        self.main_window.blit(text, self.msg_pos)


def main():
    sudoku = Sudoku()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            match sudoku.draw_status:
                case 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            sudoku.draw_status += 1
                        if event.key == pygame.K_LEFT:
                            sudoku.select_difficulty(-1)
                        if event.key == pygame.K_RIGHT:
                            sudoku.select_difficulty(1)
                case 1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sudoku.board_id = 0
                            sudoku.draw_status -= 1
                        if event.key == pygame.K_RETURN:
                            sudoku.draw_status += 1
                            sudoku.game.select_board(sudoku.difficulty, sudoku.board_id)
                        if event.key == pygame.K_LEFT:
                            sudoku.select_board(-1)
                        if event.key == pygame.K_RIGHT:
                            sudoku.select_board(1)
                case 2:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        sudoku.update_selection_box(pos[0], pos[1], True)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            sudoku.update_selection_box(-1, 0, False)
                        if event.key == pygame.K_RIGHT:
                            sudoku.update_selection_box(1, 0, False)
                        if event.key == pygame.K_UP:
                            sudoku.update_selection_box(0, -1, False)
                        if event.key == pygame.K_DOWN:
                            sudoku.update_selection_box(0, 1, False)
                        if event.key == pygame.K_BACKSPACE:
                            sudoku.game.update_cell(sudoku.x, sudoku.y, 0)
                        if event.key == pygame.K_1:
                            sudoku.try_number(1)
                        if event.key == pygame.K_2:
                            sudoku.try_number(2)
                        if event.key == pygame.K_3:
                            sudoku.try_number(3)
                        if event.key == pygame.K_4:
                            sudoku.try_number(4)
                        if event.key == pygame.K_5:
                            sudoku.try_number(5)
                        if event.key == pygame.K_6:
                            sudoku.try_number(6)
                        if event.key == pygame.K_7:
                            sudoku.try_number(7)
                        if event.key == pygame.K_8:
                            sudoku.try_number(8)
                        if event.key == pygame.K_9:
                            sudoku.try_number(9)
                        if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            sudoku.solve_sudoku()
                        if event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            sudoku.cheat_sudoku()
                        if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            sudoku.game.reset_board()
                        if event.key == pygame.K_ESCAPE:
                            sudoku.reset_sudoku()
                case 3:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sudoku.reset_sudoku()
                        if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            sudoku.draw_status = 2
                            sudoku.game.reset_board()
        match sudoku.draw_status:
            case 0:
                sudoku.draw_title()
                sudoku.draw_difficulty()
            case 1:
                sudoku.draw_title()
                sudoku.draw_board_id()
            case 2:
                sudoku.draw_sudoku()
            case 3:
                sudoku.draw_result()
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
