#make object with 6x8 board
import boards
from typing import Dict, List, Optional, Set, Tuple

board = boards.day_11_19 #should not be global at some point 
SOLUTION = boards.solution_11_19 #compare against this is global?
WIDTH = 6
HEIGHT = 8
MAX_SIZE = 10
MAX_LEN = 10
        
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
    '''
    Get all possible combinations of letters from 4 letters to MAX_LEN
    
    Args:
        board List(char): List of letters at ea position
        neighbors: List(List(int)): indices of neighbors
    '''
    neighbors = getNeighbors() #this is the same for all boards
    domains = []
    for i in range(len(board)):
        domains.extend(explore(i, [i]))
    return domains

def explore(index:int, path:List[int], neighbors):
    '''
    Recursive function to explore all possible paths
    Used in getDomains
    
    Args:
        index (int): index at which we are at in the path
        path List(int): indices of letters currently in the path
        neighbors List(List(int)): indices for each neighbor
    '''
    if len(path) > MAX_LEN:
        return
    result = [tuple(path)]
    
    for neighbor in neighbors[index]:
        if neighbor not in path:
            result.extend(explore(neighbor, path + [neighbor], neighbors))
            
    return result
    
def getNeighbors():
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
    return neighbors
    
     






def customSolver(board: List[int]):
    
    return solution

    
def displayBoard(self): 
    '''
    function to print board and display letters
    '''
    #print " | " and join with row
    #print " _ " and join with column
    # or just have letters in grid..
    

        
        
    
    