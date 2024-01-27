"""
Tic Tac Toe Player
"""
import copy
import math
import random

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    sum_plays = sum(1 for sublist in board for element in sublist if element == X or element == O)
    sum_Null = sum(1 for sublist in board for element in sublist if element == EMPTY)
    if sum_plays %2 == 0:
        return X
    elif sum_plays %2 == 1:
        return O
    elif sum_Null == 0:
        print('Game over, board full.')
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    height = len(board)
    width = max(len(line) for line in board)
    possible_actions = set()
    for row in range(height):
        for column in range(width):
            if board[row][column] == EMPTY:
                possible_actions.add((row,column))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise NameError('Move Invalid. Board Cell Not Empty.')
    else:
        new_board = copy.deepcopy(board)
        new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_conditions = [[(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)],
                      [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
                      [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)] ]

    for line in win_conditions:
        triplets = [board[row][col] for row, col in line]
        # print("triplets = ", triplets)
        if all(value == X for value in triplets):
            return X
        elif all(value == O for value in triplets):
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flattened_board = [item for sublist in board for item in sublist]
    if EMPTY not in flattened_board or winner(board) is not None:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        if board == initial_state():
            return random.choice(list(actions(board)))
        v = float('-inf')
        opt_action = None
        for action in actions(board):
            min_val = Min_Value(result(board,action))
            if min_val > v:
                v = min_val
                opt_action = action
        return opt_action

    if player(board) == O:
        v = float('inf')
        opt_action = None
        for action in actions(board):
            max_val = Max_Value(result(board,action))
            if max_val < v:
                v = max_val
                opt_action = action
        return opt_action



def Max_Value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, Min_Value(result(board,action)))
    return v

def Min_Value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, Max_Value(result(board,action)))
    return v

