"""
Tic Tac Toe Player
"""

import math
import copy
import sys


X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    x_counter = 0
    o_counter = 0
    for row in board:
        x_counter += row.count(X)
        o_counter += row.count(O)

    if x_counter == o_counter:
        return X 
    return O

    def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
                
    return possible_moves


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
                
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)

    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise Exception
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
            return boardcopy
    except Exception:
        print('Spot already occupied')

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows

    new_board = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            new_board[i][j] = new_board[j][i]
    
    for row in board:
        x_counter = row.count(X)
        o_counter = row.count(O)
        if x_counter == 3:
            return X
        if o_counter == 3:
            return O
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O
        
        # checking diagonals
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False

    return True

    def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action = (1, 1)
    if board == initial_state():
        return optimal_action

    if terminal(board):
        return None
 
    currentPlayer = player(board)
    if currentPlayer == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def max_value(board):

    if terminal(board):

        return (utility(board), None)

    value = -2

    optimal_action = None
    for action in actions(board):

        possible_result = min_value(result(board, action))

        if possible_result[0] > value:

            value = possible_result[0]

            optimal_action = action

        if value == 1:
            break

    return (value, optimal_action)

def min_value(board):

    if terminal(board):

        return (utility(board), None)

    value = 2

    optimal_action = None

    for action in actions(board):

        possible_result = max_value(result(board, action))

        if possible_result[0] < value:

            value = possible_result[0]

            optimal_action = action

        if value == -1:
            break

    return (value, optimal_action)