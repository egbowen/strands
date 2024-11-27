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
    

    neighbors = getNeighbors() #letters on each side (should we prune this as we fill in?) 
    # domains = getDomains(neighbors) #all possible word combinations
    print(neighbors)
    
    return 

def getDomains(neighbors):
    '''
    Get all possible combinations of letters from 4 letters to MAX_LEN
    
    Args:
        board List(char): List of letters at ea position
        neighbors: List(List(int)): indices of neighbors
    '''
    domains = []
    for i in range(WIDTH*HEIGHT):
        domains.extend(explore(i, [i], neighbors))
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
        return []
    result = [tuple(path)]
    
    for neighbor in neighbors[index]:
        if neighbor not in path:
            result.extend(explore(neighbor, path + [neighbor], neighbors))
            
    return result
    
def getNeighbors():
    moves = [-1, 1, -WIDTH, WIDTH, -WIDTH - 1, -WIDTH + 1, WIDTH - 1, WIDTH + 1]
    neighbors = []
    
    for i in range(WIDTH * HEIGHT):
        row = i // WIDTH
        col = i % WIDTH
        single_neighbor = []

        for m in moves:
            neighbor = i + m
            if 0 <= neighbor < WIDTH * HEIGHT:
                neighbor_row = neighbor // WIDTH
                neighbor_col = neighbor % WIDTH
                
                # Only add neighbors where row and column are within +-1 range of current
                if abs(neighbor_row - row) <= 1 and abs(neighbor_col - col) <= 1:
                    single_neighbor.append(neighbor)
        
        neighbors.append(single_neighbor)
    
    return neighbors
    
     
     
dfsSolver(board)  
     
     


##################################################3
def customSolver(board: List[int]):
    
    return solution

    
def displayBoard(self): 
    '''
    function to print board and display letters
    '''
    #print " | " and join with row
    #print " _ " and join with column
    # or just have letters in grid..
    

        
        
    
    