#make object with 6x8 board
import boards
from typing import Dict, List, Optional, Set, Tuple
import time

board = boards.day_11_19 #should not be global at some point 
SOLUTION = boards.solution_11_19 #compare against this is global?
SOLUTION_TOT = len(SOLUTION)
WIDTH = 6
HEIGHT = 8
MAX_LEN = 11 #upping this number makes it take a long time

SOLUTION_COUNT = 0

class dfsSimple:
    def __init__(self, board, solution):
        self.board = board  
        self.solution = solution
        self.solution_tot = len(solution)
        self.solution_count = 0
        self.found_indices = []
    
    def greedySolver(self):
        '''
        solver is DFS or custom
        '''
        # display board
        neighbors = self.getNeighbors() #letters on each side (should we prune this as we fill in?) 
        
        #run the tests
        for i in range(WIDTH*HEIGHT):
            # self.explore(i, [i], neighbors)
            if (self.solution_count < SOLUTION_TOT): #stops when we find all solutions
                if i not in self.found_indices:
                    self.explore(i, [i], neighbors)
            else:
                break
            
        print("You are done!")
        if self.solution_count >= SOLUTION_TOT:
            print("You solved the puzzle! Good job!")
            return True
        print("You did not solve the puzzle. Better luck next time :(")
        return False 

    def explore(self, index: int, path: List[int], neighbors: List[List[int]]) -> List[List[int]]:
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
        found_something = False
        
        while not found_something:
            if len(path) >= MAX_LEN:
                return []
            
            #right now, this is checking every time we come across a path
            if 4 <= len(path) <= MAX_LEN:
                if path in self.solution :
                    self.solution_count += 1
                    print(f"I found solution {self.solution_count}! Path: {path}")
                    self.found_indices += path
                    found_something = True
                    break
                
                    #get rid of the values in all neighbors
                    new_neighbors = []
                    for n in neighbors:
                        # Create a new list excluding the values that are in the path
                        new_n = [val for val in n if val not in path]
                        new_neighbors.append(new_n)
                    neighbors = new_neighbors

            for neighbor in neighbors[index]:
                if neighbor not in path and neighbor not in self.found_indices:
                    #print(f"Exploring neighbor {neighbor} from index {index} with path {path}") 
                    new_path = path + [neighbor]  
                    self.explore(neighbor, new_path, neighbors)
            found_something = True
        return []
        
    def getNeighbors(self):
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
    
class WordRules(dfsSimple):
    def __init__(self, board, solution):
        super().__init__(board, solution)
        
    def wordRulesSolver(self):
        neighbors = dfsSimple.getNeighbors(self)
           
        #run the tests
        for i in range(WIDTH*HEIGHT):
            if (self.solution_count < SOLUTION_TOT): #stops when we find all solutions
                self.explore(i, [i], neighbors)
            else:
                break
            
        print("You are done!")
        if self.solution_count >= SOLUTION_TOT:
            print("You solved the puzzle! Good job!")
            return True
        print("You did not solve the puzzle. Better luck next time :(")
        return False 
        
    def explore(self, index: int, path: List[int], neighbors: List[List[int]]) -> List[List[int]]:
        '''
        Recursive function to explore all possible paths
        
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
        if path in self.solution :
            self.solution_count += 1
            print(f"I found solution {self.solution_count}! Path: {path}")
            
            # when we have found all solutions
            if self.solution_count == self.solution_tot:
                print("Congrats! You found all the solutions!")
                return []
            
            #get rid of the values in all neighbors
            # aka apply new constraint
            new_neighbors = []
            for n in neighbors:
                # Create a new list excluding the values that are in the path
                new_n = [val for val in n if val not in path]
                new_neighbors.append(new_n)
            neighbors = new_neighbors
        
        all_paths = []
        
        # need to make it so if we have returned [] we stop looking at that one
        
        if 4 <= len(path) <= MAX_LEN:
            if len(path) == 4:
                if self.preprocess(path):
                    all_paths.append(path)
                    #don't add path if doesnt pass preprocessing
            else:
                all_paths.append(path)

        for neighbor in neighbors[index]:
            if neighbor not in path:
                #print(f"Exploring neighbor {neighbor} from index {index} with path {path}") 
                new_path = path + [neighbor]  
                all_paths.extend(self.explore(neighbor, new_path, neighbors))  # Add all resulting paths to the list

        return all_paths
    
    def preprocess(self, path: List[int]) -> bool:
        #use the rules we've made to preprocess the data 
        # we will probably do this at about 4 letters 
        # if self.check_for_vowel(path) and self.check_bad_combos(path):
        if self.check_for_vowel(path):
            return True
        return False
    
    def best_next_choice():
        #chose the neighbor that is the most likely next solution
        pass
        
    def check_for_vowel(self, path: List[int]) -> bool:
        """
        Make sure there is a vowel in the path

        Args:
            path (List[int]):

        Returns:
            bool: Value indicating there is a vowel in the path or that
                we are in the first few letters
        """
        
        if len(path) < 4:
            return True
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
        return any(letter in vowels for letter in path)
    
    def check_bad_combos(self, path: List[int]) -> bool:
        """
        Check for 2 letter combinations that are unlikely or impossible
        
        Args:
            path (List[int]): path we have followed on board

        Returns:
            bool: if the path is valid
        """
        # Unlikely two-letter combinations
        two_letter_combos = { # compiled from generative AI
            'bk', 'fq', 'jc', 'jt', 'mj', 'qh', 'qx', 'vj', 'wz', 'zh',
            'bq', 'fv', 'jd', 'jv', 'mq', 'qj', 'qy', 'vk', 'xb', 'zj',
            'bx', 'fx', 'jf', 'jw', 'mx', 'qk', 'qz', 'vm', 'xg', 'zn',
            'cb', 'fz', 'jg', 'jx', 'mz', 'ql', 'sx', 'vn', 'xj', 'zq',
            'cf', 'gq', 'jh', 'jy', 'pq', 'qm', 'sz', 'vp', 'xk', 'zr',
            'cg', 'gv', 'jk', 'jz', 'pv', 'qn', 'tq', 'vq', 'xv', 'zs',
            'cj', 'gx', 'jl', 'kq', 'px', 'qo', 'tx', 'vt', 'xz', 'zx',
            'cp', 'hk', 'jm', 'kv', 'qb', 'qp', 'vb', 'vw', 'yq', 'cv',
            'hv', 'jn', 'kx', 'qc', 'qr', 'vc', 'vx', 'yv', 'cw', 'hx',
            'jp', 'kz', 'qd', 'qs', 'vd', 'vz', 'yz', 'cx', 'hz', 'jq',
            'lq', 'qe', 'qt', 'vf', 'wq', 'zb', 'dx', 'iy', 'jr', 'lx',
            'qf', 'qv', 'vg', 'wv', 'zc', 'fk', 'jb', 'js', 'mg', 'qg',
            'qw', 'vh', 'wx', 'zg'
        }
        for i in range(len(path) - 1):
            letter_pair = board[path[i]] + board[path[i + 1]]
            
            if letter_pair in two_letter_combos:
                return False

        return True
    
    def highest_freq_letter(self, index: int, my_neighbors: List[int]) -> int:
        """
        Out of the neighbors, gets the letter that occurs most 
        in english language
        Tell us which neighbor to go to next

        Args:
            index(int): index in the board at which we are choosing the best possible next letter
            my_neighbors(List[int]): valid neighboring indices

        Returns:
            int: the index we should follow next
        """
        letter_freq = {
            'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 
            'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 
            'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 
            'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 
            'J': 0.10, 'Z': 0.07
        }
        
        best_neighbor = my_neighbors[0]
        highest_freq = letter_freq.get(board[best_neighbor], 0)
        for neighbor in my_neighbors:
            letter = board[neighbor]
            freq = letter_freq.get(letter, 0)
            
            if freq > highest_freq:
                highest_freq = freq
                best_neighbor = neighbor

        return best_neighbor 
    
    
    
class DictionarySearch(dfsSimple):
    def explore(self):
        '''
        Another solving algorithm where we check each word against possible words in the dictionary.
        '''
        pass
    

class AC3Search(dfsSimple):
    def explore(self):
        '''
        Another solving algorithm where use a modification of the AC3 algorithm
        '''
        pass


##################################################
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



# run word rules  
# print("WORD_RULES SOLVER")
# displayBoard(board)
# wordy_solver = WordRules(board, SOLUTION)  
# wordy_starttime = time.time() 
# word_solved = wordy_solver.wordRulesSolver() 
# wordy_endtime = time.time() 

# wordy_time = wordy_endtime - wordy_starttime


#run greedy
print("GREEDY SOLVER")
displayBoard(board)
dfs_solver = dfsSimple(board, SOLUTION) 
greedy_starttime = time.time()  
dfs_solved = dfs_solver.greedySolver() 
greedy_endtime = time.time() 

greedy_time = greedy_endtime - greedy_starttime

#final outcomes:
#print(f"Word Rules Solver: Time taken = {wordy_time:.2f} seconds, Solved = {word_solved}")
print(f"Greedy Solver: Time taken = {greedy_time:.2f} seconds, Solved = {dfs_solved}")

