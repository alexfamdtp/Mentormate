import copy
from itertools import chain

width_length = input().split()
width = int(width_length[0])
length = int(width_length[1])

if width >= 100 or length >= 100:  # Validating width and length is below 100
    print("-1")
    exit()
total_bricks = 0  # number of bricks in each layer
level_single_line = []  # The entire level one in a single list
level_one = []  # the base level
level_two = []  # the upper level that needs to be constructed
column = 0  # column N:
row = []  # Content of the row
while column < width:  # Getting the input for each row in the given level
    column += 1
    row = input().split()
    level_single_line += row
    level_one.append(row)
    total_bricks = int(len(level_single_line) / 2)
    for brick_number in level_single_line:  # Checking if brick is 2x1 or if the brick appears elsewhere
        if level_single_line.count(brick_number) > 2:
            print("-1")
            exit()
            break
level_two = copy.deepcopy(level_one)  # Copying level one and changing the brick numbers to "x"
for i in range(len(level_two)):  # to get a visual of the layout
    for h in range(len(level_two[0])):
        level_two[i][h] = "x"
"""I divide the grid into 2x2 squares. Each square has an upper part and a lower part"""
block_A_up = []
upper = []
upper_A = []
upper_B = []
block_A_down = []
lower = []
lower_A = []
lower_B = []
number_row = 0
square = []  # The square taken from level one
square_for_placement = [["x", "x"], ["x", "x"]]  # The square created to be placed into level two
floors = [level_one, level_two]
used_bricks = []  # Bricks that have been used up
i = 0  # Variable to separate rows belonging to upper or lower level
for floor in floors:  # Creating upper part and lower part square generation of level one
    for row in floor:
        for column in row:
            if number_row == 0 or number_row % 2 == 0:
                block_A_up.append(column)
                if len(block_A_up) == 2:
                    upper.append(block_A_up)
                    block_A_up = []
            elif number_row % 2 != 0:
                block_A_down.append(column)
                if len(block_A_down) == 2:
                    lower.append(block_A_down)
                    block_A_down = []
        number_row += 1
    if i == 0:
        upper_A = copy.deepcopy(upper)
        lower_A = copy.deepcopy(lower)
        upper = []
        lower = []
        i += 1
"""Logic to generate squares:
2x2 squares have several variations
eg.
1 1    1 2    1 2    1 2
2 2    1 2    1 3    3 4
with respective equivalents in level two
1 2    1 1    1 1    3 2
1 2    2 2    2 2    3 2"""
line_upper_B = []  # All of the upper and lower parts of the squares in a single list
line_lower_B = []
for square_number in range(len(upper_A)):
    square.append(upper_A[square_number])
    square.append(lower_A[square_number])
    if len(set(square[0] + square[1])) < 4:
        if square[0][0] not in used_bricks:
            if square[0][0] == square[0][1] and square[0][0]:
                square_for_placement[0][0] = square[0][0]
                square_for_placement[1][0] = square[0][0]
                used_bricks.append(square[0][0])
                square_for_placement[0][1] = square[1][0]
                square_for_placement[1][1] = square[1][0]
                used_bricks.append(square[1][0])
            elif square[0][0] == square[1][0] and square[0][0]:
                square_for_placement[0][0] = square[0][0]
                square_for_placement[0][1] = square[0][0]
                used_bricks.append(square[0][0])
                square_for_placement[1][0] = square[0][1]
                square_for_placement[1][1] = square[0][1]
                used_bricks.append(square[0][1])
        else:
            if square[1][1] == square[0][1]:
                square_for_placement[1][1] = square[1][1]
                square_for_placement[1][0] = square[1][1]
                used_bricks.append(square[1][1])
                square_for_placement[0][1] = square[1][0]
                square_for_placement[0][0] = square[1][0]
                used_bricks.append(square[1][0])
            elif square[1][1] == square[1][0]:
                square_for_placement[1][1] = square[1][1]
                square_for_placement[0][1] = square[1][1]
                used_bricks.append(square[1][1])
                square_for_placement[1][0] = square[0][1]
                square_for_placement[0][0] = square[0][1]
                used_bricks.append(square[0][1])
    else:
        square_for_placement[1][0] = square[1][0]
        square_for_placement[0][0] = square[1][0]
        used_bricks.append(square[1][0])
        square_for_placement[0][1] = square[0][1]
        square_for_placement[1][1] = square[0][1]
        used_bricks.append(square[0][1])
    square = []
    a = copy.deepcopy(square_for_placement[0])
    b = copy.deepcopy(square_for_placement[1])
    upper_B.append(a)
    line_upper_B = list(chain.from_iterable(upper_B))
    lower_B.append(b)
    line_lower_B = list(chain.from_iterable(lower_B))

for row in range(len(level_two)):  # Clearing up level two for placement of bricks
    level_two[row] = []
line = 0  # Number of row in level two
z = 0  # Number of bricks in single row
while line != len(level_two) - 1:  # Creating level two each list is a separate row
    for line in range(len(level_two)):
        if line % 2 == 0:
            for brick_1 in line_upper_B:
                if z != len(level_one[0]):
                    level_two[line].append(brick_1)
                    z += 1
                if z == len((level_one[0])):
                    z = 0
                    for i in level_two[line]:
                        if i in line_upper_B:
                            line_upper_B.remove(i)
                    break
        else:
            for brick_2 in line_lower_B:
                if z != len(level_one[0]):
                    level_two[line].append(brick_2)
                    z += 1
                if z == len(level_one[0]):
                    z = 0
                    for i in level_two[line]:
                        if i in line_lower_B:
                            line_lower_B.remove(i)
                    break
for x in level_two:  # Formatting of the end result
    for y in x:
        print('{:2}'.format(y), end=" ")
    print(end="\n")
