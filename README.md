# Strands
### Liz Bowen, Elli Sterling, Abe Merino
### AI Final Project
#### Solvers for the NYT game "Strands" for CSCI311: Artificial Intelligence with Prof. Linderman

Our project aims to assess the accuracy of heuristic based solvers in comparison to a simple depth first search (DFS) solver for the NYT game Strands. Strands is a word search game in which you are given a clue and a board with words that pertain to that clue. Each guess is verified as correct or incorrect. Before we guess, we verify each word against a list of all English words. If that search fails, we run a brute force search to find the rest of the words (bigrams or unusual words like 'spork'). The textfile of the list of words comes from this GitHub repo: https://github.com/dwyl/english-words.