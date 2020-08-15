import eel
import time
import random

# Set public file folder
eel.init('public')

bd = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

speedInfo = {
    "Slow": 0.3,
    "Medium": 0.1,
    "Fast": 0
}

@eel.expose
def generateNewBoard(level):
    easy = [
        [9, 0, 2, 0, 0, 0, 3, 0, 8],
        [0, 8, 5, 6, 0, 0, 0, 2, 0],
        [3, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 6, 5, 1, 7, 0, 0, 0],
        [2, 1, 0, 0, 3, 0, 7, 0, 5],
        [7, 5, 0, 8, 0, 4, 1, 0, 6],
        [0, 0, 1, 0, 6, 2, 0, 8, 4],
        [0, 0, 7, 4, 5, 0, 0, 0, 0],
        [6, 4, 0, 3, 0, 1, 0, 0, 7]
    ]

    medium = [
        [0, 0, 1, 6, 0, 0, 0, 8, 9],
        [0, 0, 0, 0, 0, 0, 3, 1, 0],
        [0, 4, 0, 0, 0, 0, 7, 5, 0],
        [0, 0, 0, 0, 5, 7, 2, 3, 0],
        [0, 1, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 6, 9, 1],
        [0, 0, 0, 7, 6, 3, 0, 0, 0],
        [9, 6, 0, 4, 0, 0, 8, 0, 3],
        [3, 0, 0, 0, 0, 8, 0, 0, 5]
    ]

    hard = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 9, 6],
        [0, 0, 0, 0, 5, 3, 0, 8, 0],
        [0, 4, 8, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 4, 9, 0, 0, 1],
        [6, 0, 0, 0, 0, 0, 5, 0, 9],
        [4, 0, 0, 1, 0, 0, 7, 0, 0],
        [0, 8, 0, 9, 0, 0, 4, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 2, 0]
    ]
    global bd
    
    for i in range(0, 9):
        for j in range(0, 9):
            if level == "Easy":
                bd[i][j] = easy[i][j]
            elif level == "Medium":
                bd[i][j] = medium[i][j]
            else:
                bd[i][j] = hard[i][j]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - - - ')
    
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Tuple (y, x)
    
    return None

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and i != pos[1]:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and i != pos[0]:
            return False
    
    # Check box
    box_y = pos[0] // 3
    box_x = pos[1] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

@eel.expose
def solve(speed, board=bd):
    find = find_empty(board)
    if not find:
        return True


    for num in range(1, 10):
        if valid(board, num, find):
            board[find[0]][find[1]] = num
            eel.updateSquareValue(find[0], find[1], num)
            time.sleep(speedInfo[speed])

            if solve(speed, board):
                return True

            board[find[0]][find[1]] = 0
            eel.updateSquareValue(find[0], find[1], 0)
            time.sleep(speedInfo[speed])

    return False



# Print the board to the website
@eel.expose
def print_board_to_web():
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            eel.generateBox(bd[i][j], i, j)



eel.start('index.html')

