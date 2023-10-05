import time
import pyautogui    
import csv

# Keyboard manip
def press_num(x):
    pyautogui.press(f'{x}')
    pyautogui.press('right')

def press_newRow():
    pyautogui.press('down')
    pyautogui.press('left', presses=9)

# Solver
def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def is_valid_move(board, row, col, num):
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    row, col = find_empty_cell(board)
    if row is None and col is None:
        return True
    # MRV heuristic
    for num in sorted(range(1, 10), key=lambda x: sum(1 for i in range(9) if is_valid_move(board, row, col, x))):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# Extract Sudoku board from CSV file
sudoku_board = []
with open('board.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        numeric_row = [int(cell) for cell in row]
        sudoku_board.append(numeric_row)
        
# Auto fill on website
# Alt + Tab must be connected!
if solve_sudoku(sudoku_board):
    time.sleep(2)
    pyautogui.hotkey('alt', 'tab')
    for row in range(9):
        for col in range(9):
            press_num(sudoku_board[row][col])
        time.sleep(0.5)
        press_newRow()
else:
    print("No solution exists.")