day_11_19 = [
    'P', 'O', 'O', 'R', 'S', 'K',
    'K', 'S', 'N', 'E', 'W', 'E',
    'R', 'O', 'F', 'S', 'P', 'R',
    'U', 'T', 'E', 'N', 'O', 'K',
    'H', 'C', 'S', 'I', 'L', 'S',
    'O', 'S', 'T', 'O', 'E', 'K',
    'P', 'K', 'C', 'N', 'F', 'N',
    'S', 'T', 'I', 'G', 'S', 'I'
]

solution_11_19 = [
    [4, 5, 11, 10, 9, 3], #skewer
    [7, 0, 1, 2, 8], #spoon
    [14, 13, 12, 6], #fork
    [15, 16, 22, 17, 23], #spork
    [18, 19, 20, 21, 26, 27, 28, 29], #utensils
    [25, 24, 30, 36, 42, 43, 44, 38, 37, 31], #chopsticks
    [32, 33, 39, 45, 46], #tongs
    [35, 41, 47, 40, 34] #knife
    ]

clue_11_19 = "Pick-Ups"
height_11_19 = 8
width_11_19 = 6

#################################################################
#sample smaller board 
small_board = ['M', 'A', 'C', 'E', 
                'O', 'R', 'N', 'S', 
                'N', 'R', 'E', 'E', 
                'E', 'G', 'M', 'M', 
                'I', 'O', 'I', 'I', 
                'R', 'S', 'C', 'F']
small_solution = [
    [5, 4, 0, 1, 2], #romance
    [13, 12, 8, 9, 10, 7], #genres
    [15, 11, 14, 17, 16, 20], #memoir
    [21, 22, 18, 23, 19] #scifi
    ]

small_clue = "reading material"

small_height = 6
small_width = 4

###################################
#stork board
stork_board = ['G', 'I', 'N', 'I', 'N', 'G', 
                'R', 'F', 'T', 'H', 'U', 'B', 
                'I', 'F', 'D', 'R', 'E', 'T', 
                'W', 'G', 'E', 'F', 'F', 'T',
                'I', 'N', 'L', 'R', 'K', 'A', 
                'E', 'Y', 'O', 'T', 'S', 'I', 
                'G', 'L', 'N', 'O', 'G', 'R', 
                'N', 'A', 'D', 'R', 'A', 'Y']

stork_solution = [
    [0, 6, 12, 13, 7, 1, 2], #GRIFFIN
    [18, 24, 25, 19, 20, 14, 8, 9, 3, 4, 5], #WINGED THINGS
    [43, 42, 36, 30, 37], #ANGEL
    [44, 45, 46, 40, 39, 38], #DRAGON
    [34, 33, 32, 27, 28], #STORK
    [22, 29, 35, 41, 47], #FAIRY
    [11, 10, 17, 23, 16, 15, 21, 26, 31] #BUTTERFLY
]

stork_clue = "soaring"

stork_width = 6
stork_height = 8




# code to check the boards
# for i in solution_11_19:
#     for num in i:
#         print(day_11_19[num])