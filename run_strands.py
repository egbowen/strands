import main
import time
import matplotlib.pyplot as plt
import numpy as np

class TestClass:
# run word rules  
    def init(self):
        self.wordy_time = 0
        self.greedy_time = 0
        self.dict_time = 0

    def test(self):
        print("WORD_RULES SOLVER")
        main.displayBoard(main.board)
        self.wordy_solver = main.WordRules(main.board, main.SOLUTION)  
        wordy_starttime = time.time() 
        word_solved = self.wordy_solver.wordRulesSolver() 
        wordy_endtime = time.time() 

        self.wordy_time = wordy_endtime - wordy_starttime

        #run greedy
        print("GREEDY SOLVER")
        main.displayBoard(main.board)
        self.dfs_solver = main.dfsSimple(main.board, main.SOLUTION) 
        greedy_starttime = time.time()  
        dfs_solved = self.dfs_solver.greedySolver() 
        greedy_endtime = time.time() 

        self.greedy_time = greedy_endtime - greedy_starttime

        # run dictionary
        print("DICTIONARY SOLVER")
        main.displayBoard(main.board)
        self.dict_solver = main.DictionarySearch(main.board, main.SOLUTION)
        dict_starttime = time.time()
        dict_solved = self.dict_solver.dictionarySolver()
        dict_endtime = time.time()

        self.dict_time = dict_endtime - dict_starttime

        # final outcomes:
        print(f"Word Rules Solver: Time taken = {self.wordy_time:.2f} seconds, Solved = {word_solved}")
        print(f"Greedy Solver: Time taken = {self.greedy_time:.2f} seconds, Solved = {dfs_solved}")
        print(f"Dictionary Solver: Time taken = {self.dict_time:.2f} seconds, Solved = {dict_solved}")

# n = 3
# interval = np.arange(n)
# width = 0.25

# xval = [wordy_time, greedy_time, dict_time]
# zval = [wordy_solver.recursion_count, dfs_solver.recursion_count, dict_solver.recursion_count]
# values3 = [wordy_solver.incorrect_guesses, dfs_solver.incorrect_guesses, dict_solver.incorrect_guesses]
# bar1 = plt.barh(interval, xval, width, color='#f8cd05ff')
# bar2 = plt.barh(interval, zval, width, color='#aedfeeff')
# bar3 = plt.barh(interval, wval, width, color='#c0ddd9ff')
# plt.ylabel("Algorithm")
# plt.yticks(interval+width,labels)
# plt.xlabel('something')
# plt.legend( (bar1, bar2, bar3), ('Time', 'Recursions', 'Errors') )

# plt.show()