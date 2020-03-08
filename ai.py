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
class Strategy():

    '''utility.Takes
       a CheckerBoard and determines
       the strength related to player.For example, a strong red board
       should return a high score if the constructor was invoked with ‘r’,
       and a low score with ‘b’.Note that this is not implemented in the abstract class.'''


    def utility(self, board, player):
        return 0

    '''
    play. Takes a checkerboard and determines the best move with respect to alpha-beta search for the player 
    associated with the class instance. This must also be implemented in the derived clas
    '''

    def play(self, board):
        #Need to implement the alpha-beta search to finish this method
        return 0

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
        return self.maxValue(state, -1*math.inf, math.inf, 0)



    def minValue(self, state, alpha, beta, depth):
        return 0


    def maxValue(self, state, alpha, beta, depth):




        return 0