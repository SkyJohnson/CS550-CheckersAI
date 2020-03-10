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
        self.minplayer = board.other_player(player)

        countPlayerPawns = board.get_pawnsN()[board.playeridx(player)]
        countPlayerKings = board.get_kingsN()[board.playeridx(player)]
        countOtherPawns = board.get_pawnsN()[board.playeridx(self.minplayer)]
        countOtherKings = board.get_kingsN()[board.playeridx(self.minplayer)]

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
        self.maxPlayer = maxPlayer # Will be storing which player is the max or min searching one
        self.minPlayer = minPlayer
        self.maxPlies = maxPlies
        self.action_utils = dict()

    # state being a board state representation
    def alphaBetaSearch(self,state):
        depth = 0
        best_action = []
        max_util = self.maxValue(state, -1*math.inf, math.inf, self.maxPlies, depth)
        for key,value in self.action_utils.items():
            if value == max_util:
                best_action = key

            #print(key, value)

        return best_action

    def maxValue(self, state, alpha, beta, maxplies, depth): 
        if state.is_terminal()[0] or depth >= maxplies:    # board is at a terminal state or we have reach max search depth
            v = Strategy.utility(Strategy, state, self.maxPlayer)
        else:
            depth += 1
            v = -1*math.inf
            for action in state.get_actions(self.maxPlayer):
                v = max((v, self.minValue(state.move(action), alpha, beta, maxplies, depth)))
                if depth == 1:
                    self.action_utils[tuple(action)] = v
                if v >= beta:
                    break
                else:
                    alpha = max((alpha, v))
        return v
    def minValue(self, state, alpha, beta, maxplies, depth):
        if state.is_terminal()[0] or depth >= maxplies:    # board is at a terminal state or we have reach max search depth
            v = Strategy.utility(Strategy, state, self.minPlayer)
        else:
            depth += 1
            v = math.inf
            for action in state.get_actions(self.minPlayer):
                v = min((v, self.maxValue(state.move(action), alpha, beta, maxplies, depth)))
                if v <= alpha:
                    break
                else:
                   beta = min((beta, v))
        return v


    
