#make object with 6x8 board
import boards
from typing import Dict, List, Optional, Set, Tuple

board = boards.day_11_19 #should not be global at some point 
SOLUTION = boards.solution_11_19 #compare against this is global?
SOLUTION_TOT = len(SOLUTION)
WIDTH = 6
HEIGHT = 8
MAX_LEN = 10

SOLUTION_COUNT = 0
        
def greedySolver(board: List[int]):
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
    
    #right now, this is checking every time we come across a path
    if path in SOLUTION :
        global SOLUTION_COUNT
        SOLUTION_COUNT += 1
        print(f"I found solution {SOLUTION_COUNT}! Path: {path}")
        
        # when we have found all solutions
        if SOLUTION_COUNT == SOLUTION_TOT:
            print("Congrats! You found all the solutions!")
            return 
        
        #get rid of the values in all neighbors
        new_neighbors = []
        for n in neighbors:
            # Create a new list excluding the values that are in the path
            new_n = [val for val in n if val not in path]
            new_neighbors.append(new_n)
        neighbors = new_neighbors
    
    all_paths = []
    if 4 <= len(path) <= MAX_LEN:
        all_paths.append(path)


    for neighbor in neighbors[index]:
        if neighbor not in path:
            #print(f"Exploring neighbor {neighbor} from index {index} with path {path}") 
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
greedySolver(board)  
     
     





##################################################

'''
Liz's notes:

DFS SOLVER:
    done!

CSP solver: 
    what we want to do:
    use word rules to generate domains that are valid words
        we dont explore paths that obviously lead to invalid words
    tbh i'm still struggling with the CSP way as working which is 
    somewhat contridictary to our origional proposal
        -i think we should go to office hours (i can also just go)
        to ask linderman some q's about it 
        
optimized DFS:
    i think this is likely to be the best solver
    we basically use work rules to chop off paths for future words
        only follow legit word combos 
'''




def generateDomains(board: List[str], neighbors: List[List[int]]): 
    '''
    generate domain of possible words for each letter tile
    '''
    domains = [] 
    for i in range(WIDTH * HEIGHT): 
        all_paths = explore(i, [i], neighbors) #explore paths starting at index 'i' 
        words = ["".join(board[j] for j in path) for path in all_paths] 
        domains.append(words) 
    return domains 


def customSolver(board: List[str], neighbors: List[List[int]], solution: List[List[int]]): 
    '''
    custom solver modeled as CSP
    '''
    domains = generateDomains(board, neighbors)
    assignment = {} 

    def backtrack(): 
        if len(assignment) == WIDTH * HEIGHT: 
            return assignment 
        
        #select an unassigned tile 
        var = selectUnassignedTile(domains, assignment) 
        if var is None: 
            return None 
        
        #try assigning word from its domain 
        for word in domains[var]: 
            if isConsistent(word, assignment): 
                #assign and propagate constraints 
                assignment[var] = word 
                propagateConstraints(domains, word) 

                result = backtrack() 
                if result is not None: 
                    return result 
                
                del assignment[var] 
        return None 

    return backtrack() 

def selectUnassignedTile(domains: List[List[str]], assignment: Dict[int, str]) -> Optional[int]: 
    '''
    select next UNASSIGNED tile... use heuristic? 
    '''
    for i in range(WIDTH * HEIGHT): 
        if i not in assignment: 
            return i 
    return None 

def isConsistent(word: str, assignment: Dict[int, str]) -> bool: 
    '''
    check consistency, apply constraints 
    '''
    # check letters are adjacent, not reused from already verified words 
    return True 

def propagateConstraints(domains: List[List[str]], word: str): 
    ''' 
    propagate constraints after assigning a word
    ex: remove letters of verified word from other domains, 
    '''
    pass
    
def displayBoard(board: List[str]): 
    '''
    function to print board and display letters
    '''
    print("\nCurrent Board:") 
    print("-" * (WIDTH * 4 + 1)) #horizontal border 
    for i in range(HEIGHT): 
        row = board[i * WIDTH:(i + 1) * WIDTH] 
        print("| " + " | ".join(row) + " |") # rows with letters 
        print("_" * (WIDTH * 4 + 1)) #horizontal border

    

        
        
    
    