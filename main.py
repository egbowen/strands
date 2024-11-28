#make object with 6x8 board
import boards
from typing import Dict, List, Optional, Set, Tuple

board = boards.day_11_19 #should not be global at some point 
SOLUTION = boards.solution_11_19 #compare against this is global?
WIDTH = 6
HEIGHT = 8
MAX_SIZE = 10
MAX_LEN = 6

MIN_ONE = 10000
MAX_ONE = -1
        
def dfsSolver(board: List[int]):
    '''
    solver is DFS or custom
    '''
    # display board
    neighbors = getNeighbors() #letters on each side (should we prune this as we fill in?) 
    domains = getDomains(neighbors) #all possible word combinations
    
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
        domains.append(explore(i, [i], neighbors))
    return domains

def explore(index: int, path: List[int], neighbors: List[List[int]]) -> List[List[int]]:
    '''
    Recursive function to explore all possible paths
    Used in getDomains
    
    Args:
        index (int): index at which we are at in the path
        path (List[int]): indices of letters currently in the path
        neighbors (List[List[int]]): indices for each neighbor
    
    Returns:
        List[List[int]]: All possible paths explored from the current index
    '''
    if len(path) >= MAX_LEN:
        return []
    
    all_paths = []
    if 4 <= len(path) <= MAX_LEN:
        all_paths.append(path)


    for neighbor in neighbors[index]:
        if neighbor not in path:
            print(f"Exploring neighbor {neighbor} from index {index} with path {path}") 
            new_path = path + [neighbor]  
            all_paths.extend(explore(neighbor, new_path, neighbors))  # Add all resulting paths to the list
    
    return all_paths
    
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
    
     
# run    
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
    

        
        
    
    