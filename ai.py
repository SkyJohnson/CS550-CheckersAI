import math
import abstractstrategy
# Might need to import from the checkerboard class to access checkerboard functionality and implement
from checkerboard import * #Importing all the file has to offer

'''
Need a class that does minimax with alpha and beta pruning. Something along the lines of:
class AlphaBetaMinimax:
    code
    def minValue(state of checkerboard, alpha, beta):
        stuff
        stuff
        return the good stuff
    code
    def maxValue(state of checkerboard, alpha, beta):
        similar as minValue, but to the max!
    code
    ree
and another one called Strategy that has a subclass used for the utility calculation of each player and their moves
class Strategy:
    blah
    blah
    def utility:
    blah
    squee
'''


############## UNTESTED ###############


class Strategy(abstractstrategy.Strategy):

    '''utility.Takes
       a CheckerBoard and determines
       the strength related to player.For example, a strong red board
       should return a high score if the constructor was invoked with ‘r’,
       and a low score with ‘b’.Note that this is not implemented in the abstract class.'''


    def utility(self, board, player):
        # Very basic utility function for testing purposes
        self.min_player = board.other_player(player)

        #Plan on using a linear weight model:
        # Utility = weight * pieces_found + weight * king_pieces + weight * position_of_piece
        #Still deciding on how to value the different weights for the different terms.

        #Set up the utility variables for each player, might need one more to evaluate the position for distoking
        player_pieces = 0
        player_king_pieces = 0
        player_piece_position = 0 # Will be used for the score evaluation of where the piece is at currently and
                                    # maybe to how far away the king row is to a piece. Still planning it out.

        opponent_pieces = 0
        opponent_king_pieces = 0
        opponent_piece_position = 0


        for info in board:
            (player_id, king_piece) = board.identifypiece(info[2])

            # board is a tuple of three elements: (row, column, player)
            # Where: info[0] = row value, info[1] = column value, info[2] = player = 'r' or 'b'

            if player_id == board.playeridx(player): # Piece belongs to player
                player_pieces += 1
                print("Found player piece!") #Testing purposes

                if king_piece: # Here, check if it's also a king piece
                    player_king_pieces += 1
                    print("Found player king piece!")

            else:
                opponent_pieces += 1
                print("Found opponent piece!")

                if king_piece:
                    opponent_king_pieces += 1
                    print("Found opponent king piece!")

        countPlayerPawns = board.get_pawnsN()[board.playeridx(player)]
        countPlayerKings = board.get_kingsN()[board.playeridx(player)]
        countOtherPawns = board.get_pawnsN()[board.playeridx(self.min_player)]
        countOtherKings = board.get_kingsN()[board.playeridx(self.min_player)]

        print(countPlayerPawns)
        print(countPlayerKings)
        print(countOtherPawns)
        print(countOtherKings)


        return (countPlayerPawns - countOtherPawns) + (countPlayerKings - countOtherKings)


    '''
    play. Takes a checkerboard and determines the best move with respect to alpha-beta search for the player 
    associated with the class instance. This must also be implemented in the derived clas
    '''

    def play(self, board):
        #Need to implement the alpha-beta search to finish this method
        search = MinimaxAlphaBetaSearch(self.maxplayer, self.minplayer, self.maxplies)
        # Search will return utility of best move
        # need to call board.move() and pass in the action with utility given from search
        best_move = search.alphaBetaSearch(board)
        #return best_move
        return (board.move(best_move), best_move)

class MinimaxAlphaBetaSearch:
# In this class, the alpha-beta pruning action shall take place with the functions
# minValue and maxValue. They will be created according to the pseudocode on page 14, slide 28

    # Initialize a search
    def __init__(self, maxPlayer, minPlayer, maxPlies):
        self.max_player = maxPlayer # Will be storing which player is the max or min.
        self.min_player = minPlayer
        self.max_plies = maxPlies
        self.action_utils = dict()

    # state being a board state representation
    def alphaBetaSearch(self,state):
        depth = 0
        best_action = [] # store the best action found for the max player
        max_util = self.maxValue(state, -1*math.inf, math.inf, self.max_plies, depth)
        for key,value in self.action_utils.items():
            if value == max_util:
                best_action = key

            #print(key, value)

        return best_action

    def maxValue(self, state, alpha, beta, max_plies, depth):
        if state.is_terminal()[0] or depth >= max_plies:    # board is at a terminal state or we have reach max search depth
            v = Strategy.utility(Strategy, state, self.max_player)
        else:
            depth += 1
            v = -1*math.inf
            for action in state.get_actions(self.max_player):
                v = max((v, self.minValue(state.move(action), alpha, beta, max_plies, depth)))
                if depth == 1:
                    self.action_utils[tuple(action)] = v
                if v >= beta:
                    break
                else:
                    alpha = max((alpha, v))
        return v
    def minValue(self, state, alpha, beta, max_plies, depth):
        if state.is_terminal()[0] or depth >= max_plies:    # board is at a terminal state or we have reach max search depth
            v = Strategy.utility(Strategy, state, self.min_player)
        else:
            depth += 1
            v = math.inf
            for action in state.get_actions(self.min_player):
                v = min((v, self.maxValue(state.move(action), alpha, beta, max_plies, depth)))
                if v <= alpha:
                    break
                else:
                   beta = min((beta, v))
        return v
