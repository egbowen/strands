#make object with 6x8 board
import boards
from typing import Dict, List, Optional, Set, Tuple

board = boards.day_11_19 #should not be global at some point 
SOLUTION = boards.solution_11_19 #compare against this is global?
WIDTH = 6
HEIGHT = 8
MAX_SIZE = 10
        
def dfsSolver(board: List[int]):
    '''
    solver is DFS or custom
    '''
    # display board
    
    domains = [] #all possible word combinations
    neighbors = [[] for i in range(WIDTH*HEIGHT)] #letters on each side (should we prune this as we fill in?)
    
    #get domains
        #recurse to get all possible combos of letters 
    
    #get neighbors
    
     
    
    return solution

def getDomains(board, neighbors):
    #ass possible combinations of letters
    #need the neighbors to get the domains
    return
    
    
    
def getNeighbors(board:List[int]):
    moves = [-1, #left
             1, #right
             -6, #up
             6, #down
             -5, #upright
             5, #downleft
             -7, #upleft
             7] #downright
    
    neighbors = []
    for i in range (WIDTH*HEIGHT):
        single_neighbor = []
        for m in moves:
            single_neighbor.append(i + m)
        neighbors.append(single_neighbor)
    
     





def customSolver(board: List[int]):
    
    return solution

    
def displayBoard(self): 
    '''
    function to print board and display letters
    '''
    #print " | " and join with row
    #print " _ " and join with column
    # or just have letters in grid..
    

        
        
    
    