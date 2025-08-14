"""
Tic Tac Toe Player
"""

import math

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
    if initial_state() == board:
        return X
    else:
        totalx=0
        totalo=0    
        for row in board:
            for item in row:
                if item==X:
                    totalx=totalx+1
                elif item==O:
                    totalo=totalo+1
        if totalx>totalo:
            return O
        else:
            return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves=set()
    for i,row in enumerate(board):
        for j,item in enumerate(row):
            if item==EMPTY:
                moves.add((i,j))
    return moves


    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Out of bounds")
    if board[action[0]][action[1]] is not None:
        raise Exception("Cell taken")
    
    board_copy=[row[:]for row in board]
    turn=player(board)
    if turn==X:
        board_copy[action[0]][action[1]]=X
    else:
        board_copy[action[0]][action[1]]=O
    
    return board_copy
    

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row.count(X)==3:
            return X
        elif row.count(O)==3:
            return O
    
    for column in range(3):
        columns=[board[row][column] for row in range(3)]
        if columns.count(X)==3:
            return X
        elif columns.count(O)==3:
            return O 

    diag=[board[i][i] for i in range(len(board))]
    sec_diag=[board[i][len(board)-1-i] for i in range(len(board))]
    if diag.count(X)==3 or sec_diag.count(X)==3:
        return X
    elif diag.count(O)==3 or sec_diag.count(O)==3:
        return O     
    

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flat_board=[item for row in board for item in row]
    total=0
    for item in flat_board:
        if item!=EMPTY:
            total+=1
    if total==9 or winner(board)==O or winner(board)==X:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board)==True:
        return None

    best_set=None
    if(player(board)==X):
        max=-5
        moves=actions(board)
        for move in moves:
            test_board=result(board,move)
            score = minimax_score(test_board)
            if score > max:
                max = score
                best_set = move

    elif(player(board)==O):
        min=5
        moves=actions(board)
        for move in moves:
            test_board=result(board,move)
            score = minimax_score(test_board)

            if score < min:
                min = score
                best_set = move

    return best_set


def minimax_score(board):
    if terminal(board)==True:
        return utility(board)
    else:
        if player(board)==X:
            max=-5
            moves=actions(board)
            for move in moves:
                test_board=result(board,move)
                score = minimax_score(test_board)
                if score > max:
                    max = score
            return max


        elif player(board)==O:
            min=5
            moves=actions(board)
            for move in moves:
                test_board=result(board,move)
                score = minimax_score(test_board)
                if score < min:
                    min = score
            return min




