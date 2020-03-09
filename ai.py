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
        minPlayer = board.other_player(player)

        countPlayerPawns = board.get_pawnsN()[board.playeridx(player)]
        countPlayerKings = board.get_kingsN()[board.playeridx(player)]
        countOtherPawns = board.get_pawnsN()[board.playeridx(minPlayer)]
        countOtherKings = board.get_kingsN()[board.playeridx(minPlayer)]

        return (countPlayerPawns - countOtherPawns) + (countPlayerKings - countOtherKings)


    '''
    play. Takes a checkerboard and determines the best move with respect to alpha-beta search for the player 
    associated with the class instance. This must also be implemented in the derived clas
    '''

    def play(self, board):
        #Need to implement the alpha-beta search to finish this method
        search = MinimaxAphaBetaSearch(self.maxPlayer, self.minPlayer, self.maxPlies)
        # Search will return utility of best move
        # need to call board.move() and pass in the action with utility given from search
        return search

class MinimaxAphaBetaSearch:
# In this class, the alpha-beta pruning action shall take place with the functions
# minValue and maxValue. They will be created according to the pseudocode on page 14, slide 28

    # Initialize a search
    def __init__(self, maxPlayer, minPlayer, maxPlies):
        self.maxPlayer = maxPlayer # Will be storing which player is the max or min searching one
        self.minPlayer = minPlayer
        self.maxPlies = maxPlies

    # state being a board state representation
    def alphaBetaSearch(self,state):
        depth = 0
        return self.maxValue(state, -1*math.inf, math.inf, self.maxPlies, depth)

    def minValue(self, state, alpha, beta, maxplies, depth):
        if state.is_terminal() or depth >= maxplies:    # board is at a terminal state or we have reach max search depth
            v = Strategy.utility(state, self.maxPlayer)
        else:
            depth += 1
            v = math.inf
            for action in state.get_actions(self.maxPlayer):
                v = min((v, maxValue(state.move(action), alpha, beta, maxplies, depth)))
                if v <= alpha:
                    break
                else:
                   beta = min((beta, v))
        return v


    def maxValue(self, state, alpha, beta, maxplies, depth): 
        if state.is_terminal() or depth >= maxplies:    # board is at a terminal state or we have reach max search depth
            v = Strategy.utility(state, self.maxPlayer)
        else:
            depth += 1
            v = -1*math.inf
            for action in state.get_actions(self.maxPlayer):
                v = max((v, minValue(state.move(action), alpha, beta, maxplies, depth)))
                if v >= beta:
                    break
                else:
                   alpha = max((alpha, v))
        return v
