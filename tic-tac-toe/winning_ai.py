from game import *
import random

def random_ai(board, player):
    coordinates = [None, None]
    while True:
        x_coordinate = random.randint(0,2)
        y_coordinate = random.randint(0,2)
        if board[x_coordinate][y_coordinate] == None:
            coordinates[0], coordinates[1] = x_coordinate, y_coordinate
            return coordinates

# makes a copy of the given board
def copy_board(board):
    copy_board = new_board()
    for row in range(3):
        for column in range(3):
            copy_board[row][column] = board[row][column]
    return copy_board

# finds a winning move for current player, if not found, it returns a random move
def finds_winning_moves_ai(board, player):
    coordinates = [None, None]
    temporary_board = copy_board(board)
    for row in range(3):
        for column in range(3):
            if temporary_board[row][column] == None:
                temporary_board[row][column] = player
                if get_winner(temporary_board) == player:
                    coordinates = [row, column]
                    return coordinates
                else:
                    temporary_board[row][column] = None
    # below code runs if no winner is found by adding current player using the above method
    # returns None if no winning move is found
    return None