import main
import time
import boards

class TestClass:
    def __init__(self, board=main.board, solution=main.SOLUTION, width=main.WIDTH, height=main.HEIGHT):
        self.board = board
        self.solution = solution
        self.width = width
        self.height = height
        self.dfs_solver = main.dfsSimple(board, solution, width, height) 
        self.wordy_solver = main.WordRules(board, solution, width, height)  
        self.dict_solver = main.DictionarySearch(board, solution, width, height)
        self.custom_solver = main.CustomSearch(board, solution, width, height)

    def test(self, dfs=True, wordy=True, dicty=True, custom=True):
        #run greedy
        if dfs:
            print("\n----------------------------------------\nGREEDY SOLVER")
            main.displayBoard(self.board, self.width, self.height)
            greedy_starttime = time.time()  
            dfs_solved = self.dfs_solver.greedySolver() 
            greedy_recursion_count = self.dfs_solver.recursion_count
            greedy_incorrect_guesses = self.dfs_solver.incorrect_guesses
            greedy_endtime = time.time() 

            self.greedy_time = greedy_endtime - greedy_starttime


        # run word rules
        if wordy:  
            print("\n----------------------------------------\nWORD_RULES SOLVER")
            main.displayBoard(self.board, self.width, self.height)
            wordy_starttime = time.time() 
            word_solved = self.wordy_solver.wordRulesSolver() 
            wordy_recursions = self.wordy_solver.recursion_count
            wordy_incorrect_guesses = self.wordy_solver.incorrect_guesses
            wordy_endtime = time.time() 

            self.wordy_time = wordy_endtime - wordy_starttime

        #run dictionary
        if dicty:
            print("\n----------------------------------------\nDICTIONARY SOLVER")
            main.displayBoard(self.board, self.width, self.height)
            dict_starttime = time.time()
            dict_solved = self.dict_solver.dictionarySolver()
            dict_recursion_count = self.dict_solver.recursion_count 
            dict_incorrect_guesses = self.dict_solver.incorrect_guesses 
            dict_endtime = time.time()

            self.dict_time = dict_endtime - dict_starttime
            
        if custom:
            print("\n----------------------------------------\nCUSTOM SOLVER")
            main.displayBoard(self.board, self.width, self.height)
            custom_starttime = time.time()
            custom_solved = self.custom_solver.customSolver()
            custom_recursion_count = self.custom_solver.recursion_count 
            custom_incorrect_guesses = self.custom_solver.incorrect_guesses 
            custom_endtime = time.time()

            self.custom_time = custom_endtime - custom_starttime
            


        #final outcomes
        self.print_results("Greedy Solver", self.greedy_time, greedy_recursion_count, greedy_incorrect_guesses, dfs_solved)
        self.print_results("Word Rules Solver", self.wordy_time, wordy_recursions, wordy_incorrect_guesses, word_solved)
        self.print_results("Dictionary Solver", self.dict_time, dict_recursion_count, dict_incorrect_guesses, dict_solved)
        self.print_results("Custom Solver", self.custom_time, custom_recursion_count, custom_incorrect_guesses, custom_solved)
    
    def print_results(self, solver_name, time_taken, recursions, incorrect_guesses, solved):
        """
        Prints the results for a specific solver with aligned output.

        Args:
            solver_name (str): Name of the solver (e.g., 'Greedy Solver').
            time_taken (float): Time taken by the solver in seconds.
            recursions (int): Number of recursions performed by the solver.
            incorrect_guesses (int): Number of incorrect guesses made by the solver.
            solved (bool): Whether the solver successfully solved the problem.
        """
        print(f"{solver_name}:")
        print(f"    Time taken        = {time_taken:.2f} seconds")
        print(f"    Recursions        = {recursions}")
        print(f"    Incorrect Guesses = {incorrect_guesses}")
        print(f"    Solved            = {solved}\n")

tester = TestClass(boards.stork_board, boards.stork_solution, boards.stork_width, boards.stork_height)
tester.test()