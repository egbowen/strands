import main
import time
import matplotlib.pyplot as plt
import numpy as np

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

# run dictionary
print("DICTIONARY SOLVER")
main.displayBoard(main.board)
dict_solver = main.DictionarySearch(main.board, main.SOLUTION)
dict_starttime = time.time()
dict_solved = dict_solver.dictionarySolver()
dict_endtime = time.time()

dict_time = dict_endtime - dict_starttime

# final outcomes:
print(f"Word Rules Solver: Time taken = {wordy_time:.2f} seconds, Solved = {word_solved}")
print(f"Greedy Solver: Time taken = {greedy_time:.2f} seconds, Solved = {dfs_solved}")
print(f"Dictionary Solver: Time taken = {dict_time:.2f} seconds, Solved = {dict_solved}")

# labels = ["Word Rules", "Greedy", "Dictionary"]
# values = [wordy_time, greedy_time, dict_time]
# fig = plt.figure(figsize = (10, 5))
# plt.bar(labels, values)