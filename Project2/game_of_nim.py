# Name: Christian Carrillo
# Date: 10-5-2025
#
# Fall 2025 CPSC 481-02 17420
# 
# Game of Nim representation

from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        # Generates moves based on row (x) and amount of available objects (y)
        moves = [(x, y) for x in range(0, len(board))
                 for y in range(1, board[x] + 1)]
        
        self.initial = GameState(to_move='X', utility=0, board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state # Illegal move has no effect
        
        row, objects = move # Unpack move
        
        new_board = state.board.copy()
        new_board[row] -= objects
        
        new_moves = [(x, y) for x in range(0, len(new_board))
                    for y in range(1, new_board[x] + 1)]
        
        to_move = 'O' if state.to_move == 'X' else 'X'
        
        if len(new_moves) == 0:
            new_utility = -1 if to_move =='O' else 1
        else:
            new_utility = 0
            
        return GameState(to_move=to_move,
                         utility=new_utility,
                         board=new_board, moves=new_moves)
        

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return len(state.moves) == 0

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
