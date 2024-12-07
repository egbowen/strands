import main
import time

# run word rules  
print("WORD_RULES SOLVER")
main.displayBoard(main.board)
wordy_solver = main.WordRules(main.board, main.SOLUTION)  
wordy_starttime = time.time() 
word_solved = wordy_solver.wordRulesSolver() 
wordy_endtime = time.time() 

wordy_time = wordy_endtime - wordy_starttime



#run greedy
print("GREEDY SOLVER")
main.displayBoard(main.board)
dfs_solver = main.dfsSimple(main.board, main.SOLUTION) 
greedy_starttime = time.time()  
dfs_solved = dfs_solver.greedySolver() 
greedy_endtime = time.time() 

greedy_time = greedy_endtime - greedy_starttime

#final outcomes:
print(f"Word Rules Solver: Time taken = {wordy_time:.2f} seconds, Solved = {word_solved}")
print(f"Greedy Solver: Time taken = {greedy_time:.2f} seconds, Solved = {dfs_solved}")