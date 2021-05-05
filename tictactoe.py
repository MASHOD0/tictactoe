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