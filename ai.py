import math
import abstractstrategy
# Might need to import from the checkerboard class to access checkerboard functionality and implement
from checkerboard import * #Importing all the file has to offer
import random

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
        player_piece_position = 0 # Will be used for the score evaluation of where the piece is at currently and
                                    # maybe to how far away the king row is to a piece. Still planning it out.
        opponent_piece_position = 0

        player_sum_dist_to_king = 0
        other_sum_dist_to_king = 0

        # Forming bridges makes pieces immune to being captured 
        player_num_bridges = 0
        other_num_bridges = 0


        for info in board:
            (player_id, king_piece) = board.identifypiece(info[2])

            # board is a tuple of three elements: (row, column, player)
            # Where: info[0] = row value, info[1] = column value, info[2] = player = 'r' or 'b'

            if player_id == board.playeridx(player): # Piece belongs to player

                ### TODO: Check for bridges (e.q. mutiple pieces of same player stacked diagonally) ###
                # Check board locations surrounding given piece
                # If piece at that location matches player -> player_num_bridges += 1
                # Can also keep track of size of bridges

                if not king_piece: # Here, check if it's also a king piece
                    player_sum_dist_to_king += board.disttoking(player, info[0])    # How many moves for player to get a king

            else:
                if not king_piece:
                    other_sum_dist_to_king += board.disttoking(self.min_player, info[0])    # How many moves for opponent to get a king

        # Count player and opponent pieces on board (kings weighted higher)
        countPlayerPawns = board.get_pawnsN()[board.playeridx(player)]
        countPlayerKings = board.get_kingsN()[board.playeridx(player)]
        countOtherPawns = board.get_pawnsN()[board.playeridx(self.min_player)]
        countOtherKings = board.get_kingsN()[board.playeridx(self.min_player)]

        # print(countPlayerPawns)
        # print(countPlayerKings)
        # print(countOtherPawns)
        # print(countOtherKings)


        return (countPlayerPawns - countOtherPawns) + (2*(countPlayerKings - countOtherKings)) + (5*(other_sum_dist_to_king - player_sum_dist_to_king))


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
        max_util = self.maxValue(state, -1*math.inf, math.inf, self.max_plies, depth)   # Max utility for given player

        # List all possible actions with max utility
        possible_best_actions = []
        for key,value in self.action_utils.items():
            
            if value == max_util:
                possible_best_actions.append(key)

            #print(key, value)

        # If multiple actions have the same max utility select one at random
        best_action = random.choice(possible_best_actions)

        return best_action

    def maxValue(self, state, alpha, beta, max_plies, depth):
        # board is at a terminal state or we have reached max search depth -> return utility
        if state.is_terminal()[0] or depth >= max_plies:
            v = Strategy.utility(Strategy, state, self.max_player)
        # Continue down the search tree
        else:
            depth += 1
            v = -1*math.inf
            for action in state.get_actions(self.max_player):
                v = max((v, self.minValue(state.move(action), alpha, beta, max_plies, depth)))
                # At the top of the search tree add possible moves and their associated utility to a dictionary
                if depth == 1:
                    self.action_utils[tuple(action)] = v
                # Utility falls outside of range -> No need to continue searching
                if v >= beta:
                    break
                else:
                    alpha = max((alpha, v))
        return v
    def minValue(self, state, alpha, beta, max_plies, depth):
        # board is at a terminal state or we have reach max search depth -> return utility
        if state.is_terminal()[0] or depth >= max_plies:
            v = Strategy.utility(Strategy, state, self.min_player)
        # Continue down search tree
        else:
            depth += 1
            v = math.inf
            for action in state.get_actions(self.min_player):
                v = min((v, self.maxValue(state.move(action), alpha, beta, max_plies, depth)))
                # Utility falls outside of range -> No need to continue searching
                if v <= alpha:
                    break
                else:
                   beta = min((beta, v))
        return v
