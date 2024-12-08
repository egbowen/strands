import main
import time

#run greedy
dfs = False
wordy = False
dicty = True

if dfs:
    print("\n----------------------------------------\nGREEDY SOLVER")
    main.displayBoard(main.board)
    dfs_solver = main.dfsSimple(main.board, main.SOLUTION) 
    greedy_starttime = time.time()  
    dfs_solved = dfs_solver.greedySolver() 
    greedy_recursion_count = dfs_solver.recursion_count
    greedy_incorrect_guesses = dfs_solver.incorrect_guesses
    greedy_endtime = time.time() 

    greedy_time = greedy_endtime - greedy_starttime


# run word rules
if wordy:  
    print("\n----------------------------------------\nWORD_RULES SOLVER")
    main.displayBoard(main.board)
    wordy_solver = main.WordRules(main.board, main.SOLUTION)  
    wordy_starttime = time.time() 
    word_solved = wordy_solver.wordRulesSolver() 
    wordy_recursions = wordy_solver.recursion_count
    wordy_incorrect_guesses = wordy_solver.incorrect_guesses
    wordy_endtime = time.time() 

    wordy_time = wordy_endtime - wordy_starttime

#run dictionary
if dicty:
    print("\n----------------------------------------\nDICTIONARY SOLVER")
    main.displayBoard(main.board)
    dict_solver = main.DictionarySearch(main.board, main.SOLUTION)
    dict_starttime = time.time()
    dict_solved = dict_solver.dictionarySolver()
    dict_recursion_count = dict_solver.recursion_count 
    dict_incorrect_guesses = dict_solver.incorrect_guesses 
    dict_endtime = time.time()

    dict_time = dict_endtime - dict_starttime


#final outcomes
def print_results(solver_name, time_taken, recursions, incorrect_guesses, solved):
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


# print_results("Greedy Solver", greedy_time, greedy_recursion_count, greedy_incorrect_guesses, dfs_solved)
# print_results("Word Rules Solver", wordy_time, wordy_recursions, wordy_incorrect_guesses, word_solved)
print_results("Dictionary Solver", dict_time, dict_recursion_count, dict_incorrect_guesses, dict_solved)