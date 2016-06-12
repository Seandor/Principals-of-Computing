"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
# EMPTY = 1
# PLAYERX = 2
# PLAYERO = 3
board = provided.TTTBoard(3) 
#print str(board)
#board.move(1, 1, provided.PLAYERO)
#board.move(1, 0, provided.PLAYERO)
#board.move(1, 2, provided.PLAYERO)
#print board.square(1, 1)
#print board.check_win()
#print board.get_empty_squares()

def mc_trial(board, player):
    """
    Play a game on the given board starting 
    with the given player by making random moves.
    Until the game end.
    """
    while board.check_win() is None:
        position = random.choice(board.get_empty_squares())
        board.move(position[0], position[1], player)
        player = provided.switch_player(player)
    # return the current player
    return player

def mc_update_scores(scores, board, player):
    """
    Score the board, a finished board.
    """
    if board.check_win() == provided.DRAW:
        scores = [[0 for dummy in range(board.get_dim())] 
                     for dummy in range(board.get_dim())]
    if board.check_win() == player:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == provided.EMPTY:
                    scores[row][col] = 0
                elif board.square(row, col) == player:
                    scores[row][col] = SCORE_CURRENT
                else:
                    scores[row][col] = -SCORE_OTHER
    else:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == provided.EMPTY:
                    scores[row][col] = 0
                elif board.square(row, col) == player:
                    scores[row][col] = -SCORE_OTHER
                else:
                    scores[row][col] = SCORE_CURRENT
        
def get_best_move(board, scores):
    """ 
    Find all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple. 
    
    """
    if len(board.get_empty_squares()) == 0:
        return
    candidate = []
    score = []
    for position in board.get_empty_squares():
        row = position[0]
        col = position[1]
        score.append(scores[row][col])
    highest = sorted(score)[-1]
    for position in board.get_empty_squares():
        row = position[0]
        col = position[1]
        if scores[row][col] == highest:
            candidate.append((row, col))
    return random.choice(candidate)

def mc_move(board, player, trials):
    """
    Using Monte Carlo method to find a machine move.
    """
    scores = [[0 for dummy in range(board.get_dim())] 
                 for dummy in range(board.get_dim())]
    moves = {}
    for dummy in range(trials):
        player = mc_trial(board, player)
        mc_update_scores(scores, board, player)
        move = get_best_move(board, scores)
        if move not in moves.keys():
            moves[move] = 1
        else:
            moves[move] += 1
    sorted_move = sorted(moves.items(), key=lambda x: x[1], reverse=True)
    return sorted_move[0][0]

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
