from tictactoe import *

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """#tre sa puna O
    return [[EMPTY,     O,      X],
            [O,         X,      X],
            [EMPTY,     X,      O]]

            # [O,         O,      X],        [EMPTY,      O,      X],          
            # [O,         X,      X],        [O,          X,      X],
            # [EMPTY,     X,      O]]        [O,          X,      O]]    

            
            # [O,         O,      X],        [x,          O,      X],          
            # [O,         X,      X],        [O,          X,      X],
            # [X,         X,      O]]        [O,          X,      O]]              

board=initial_state()

# print(actions(board))
print(minimax(board))
