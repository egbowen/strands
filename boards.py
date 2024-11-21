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


# code to check the boards
for i in solution_11_19:
    for num in i:
        print(day_11_19[num])