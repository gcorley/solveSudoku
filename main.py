import math


action_taken = False
# puzzle = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# hard
# testpuz = [[4, 0, 0, 0, 2, 0, 0, 0, 5],
#            [6, 1, 0, 0, 0, 0, 0, 0, 0],
#            [0, 5, 7, 0, 3, 0, 6, 0, 0],
#            [0, 0, 9, 0, 4, 0, 0, 7, 0],
#            [0, 0, 0, 8, 6, 0, 9, 1, 0],
#            [0, 0, 0, 0, 0, 0, 0, 3, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 6, 0, 0, 0, 1, 0, 0, 8],
#            [0, 0, 0, 3, 9, 8, 0, 0, 0]]
# testpuz_hard = [[0, 0, 8, 0, 0, 0, 2, 0, 9],
#            [0, 0, 6, 0, 5, 1, 8, 0, 0],
#            [0, 7, 0, 0, 0, 0, 0, 1, 0],
#            [0, 0, 0, 0, 0, 3, 0, 4, 0],
#            [7, 0, 0, 1, 0, 2, 0, 0, 3],
#            [0, 3, 0, 7, 0, 0, 0, 0, 0],
#            [0, 8, 0, 0, 0, 0, 0, 9, 0],
#            [0, 0, 5, 6, 8, 0, 3, 0, 0],
#            [9, 0, 1, 0, 0, 0, 4, 0, 0]]
#easy
testpuz = [[9, 0, 3, 8, 0, 0, 5, 0, 0],
           [5, 1, 0, 9, 3, 0, 4, 2, 0],
           [0, 0, 7, 5, 0, 2, 0, 0, 8],
           [0, 0, 6, 0, 0, 8, 0, 5, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 3, 0, 6, 0, 0, 1, 0, 0],
           [7, 0, 0, 4, 0, 3, 8, 0, 0],
           [0, 4, 5, 0, 8, 1, 0, 3, 2],
           [0, 0, 1, 0, 0, 9, 7, 0, 6]]

possiblepuz = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

inverted_possiblepuz = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

block_possiblepuz = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]

blocks = [[{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}],
          [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}],
          [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}]]

block_index = [[[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]],
               [[0,3], [0,4], [0,5], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5]],
               [[0,6], [0,7], [0,8], [1,6], [1,7], [1,8], [2,6], [2,7], [2,8]],
               [[3,0], [3,1], [3,2], [4,0], [4,1], [4,2], [5,0], [5,1], [5,2]],
               [[3,3], [3,4], [3,5], [4,3], [4,4], [4,5], [5,3], [5,4], [5,5]],
               [[3,6], [3,7], [3,8], [4,6], [4,7], [4,8], [5,6], [5,7], [5,8]],
               [[6,0], [6,1], [6,2], [7,0], [7,1], [7,2], [8,0], [8,1], [8,2]],
               [[6,3], [6,4], [6,5], [7,3], [7,4], [7,5], [8,3], [8,4], [8,5]],
               [[6,6], [6,7], [6,8], [7,6], [7,7], [7,8], [8,6], [8,7], [8,8]]]


def get_puzzle(url):
    return puzzle


def solve():
    global action_taken
    is_completed = False
    limit_loop = 0
    while is_completed == False:
        action_taken = False
        remove_possibilities()
        check_single_instance()
        check_matching_pairs()
        insert_single_possible()
        is_completed = check_solution()
        limit_loop += 1
        if action_taken == False:
            print(limit_loop)
            break
        # if limit_loop > 500:
        #     print(limit_loop)
        #     break


# ***********************************REMOVE POSSIBILITIES**************************************************
def remove_possibilities():
    global action_taken, testpuz, possiblepuz, blocks
    # remove possibilities that are within row
    for r, row in enumerate(testpuz):
        row_possibilities = {1,2,3,4,5,6,7,8,9}
        for c, cell in enumerate(row):
            if cell != 0: # if puzzle cell has a number; remove from possibilities
                row_possibilities.remove(cell)
        for c, cell in enumerate(row):
            if cell == 0:
                if possiblepuz[r][c] == 0:
                    possiblepuz[r][c] = row_possibilities
                    action_taken = True
                else:
                    previous_cell = possiblepuz[r][c]
                    possiblepuz[r][c] = row_possibilities.intersection(possiblepuz[r][c])
                    if previous_cell != possiblepuz[r][c]:
                        action_taken = True

    # remove possibilities that are within column
    col_index = 0
    row_index = 0
    while col_index < 9:
        row_index = 0
        col_possibilities = {1,2,3,4,5,6,7,8,9}
        while row_index < 9:
            if testpuz[row_index][col_index] != 0: # if puzzle cell has a number; remove from possibilities
                col_possibilities.remove(testpuz[row_index][col_index])
            row_index += 1
        row_index = 0
        while row_index < 9:
            if testpuz[row_index][col_index] == 0: # if puzzle cell is blank; merge column possibilities with row possibilities
                previous_cell = possiblepuz[row_index][col_index]
                possiblepuz[row_index][col_index] = col_possibilities.intersection(possiblepuz[row_index][col_index])
                if previous_cell != possiblepuz[row_index][col_index]:
                    action_taken = True
            row_index += 1
        col_index += 1

    # remove possibilities that are within block
    for r, row in enumerate(testpuz):
        for c, cell in enumerate(row):
            if cell != 0: # if puzzle cell has a number; remove from possibilities
                blocks[math.floor(r/3)][math.floor(c/3)].discard(cell)
    # update possibilepuz
    for r, row in enumerate(testpuz):
        for c, cell in enumerate(row):
            if cell == 0: # if puzzle cell is blank; merge block possibilities with row & column possibilities
                previous_cell = possiblepuz[r][c]
                possiblepuz[r][c] = blocks[math.floor(r/3)][math.floor(c/3)].intersection(possiblepuz[r][c])
                if previous_cell != possiblepuz[r][c]:
                    action_taken = True
# ***********************************REMOVE POSSIBILITIES END*******************************************************


# ***********************************CHECK SINGLE INSTANCE***********************************************************
def check_single_instance():
    global action_taken, testpuz, possiblepuz, inverted_possiblepuz, block_possiblepuz
    num_instances = {}
    # check rows
    possiblepuz = single_instance_loop(possiblepuz)

    # check columns
    invert_grid()
    inverted_possiblepuz = single_instance_loop(inverted_possiblepuz)
    match_grid_from_invert()  # resync

    # check blocks
    blockify_grid()
    block_possiblepuz = single_instance_loop(block_possiblepuz)
    match_grid_from_block() # resync
# ***********************************CHECK SINGLE INSTANCE END******************************************************


# ***********************************SINGLE INSTANCE LOOP***********************************************************
def single_instance_loop(puz):
    global action_taken
    num_instances = {}
    for r, row in enumerate(puz):
        num_instances.clear()
        for c, cell in enumerate(row):
            if cell != 0:
                for n in cell:
                    if n in num_instances:
                        num_instances[n] += 1
                    else:
                        num_instances[n] = 1
        for num, count in num_instances.items():
            if count == 1:
                for c, cell in enumerate(row):
                    if cell != 0 and num in cell:
                        puz[r][c] = {num}
                        action_taken = True
    return puz
# ***********************************SINGLE INSTANCE LOOP END*******************************************************


# ***********************************CHECK MATCHING PAIRS***********************************************************
def check_matching_pairs():
    global action_taken, testpuz, possiblepuz, inverted_possiblepuz, block_possiblepuz
    # check matching pairs in rows
    for r, row in enumerate(possiblepuz):
        for c, cell in enumerate(row):
            if cell != 0 and len(cell) == 2 and cell in row[:c]:
                # remove pair from other row possibilities
                for z in row:
                    if z != 0 and z != cell:
                        previous_value = z
                        z.difference_update(cell)
                        if previous_value != z:
                            action_taken = True

    insert_single_possible()

    # check matching pairs in columns
    invert_grid()
    for c, column in enumerate(inverted_possiblepuz):
        for r, cell in enumerate(column):
            if cell != 0 and len(cell) == 2 and cell in column[:r]:
                # remove pair from other column possibilities
                for z in column:
                    if z != 0 and z != cell:
                        previous_value = z
                        z.difference_update(cell)
                        if previous_value != z:
                            action_taken = True
    match_grid_from_invert()  # resync

    insert_single_possible()

    # check matching pairs in blocks
    blockify_grid()
    for b, block in enumerate(block_possiblepuz):
        for c, cell in enumerate(block):
            if cell != 0 and len(cell) == 2 and cell in block[:c]:
                # remove pair from other row possibilities
                for z in block:
                    if z != 0 and z != cell:
                        previous_value = z
                        z.difference_update(cell)
                        if previous_value != z:
                            action_taken = True
    match_grid_from_block() # resync
# ***********************************CHECK MATCHING PAIRS END*******************************************************


# ***********************************INVERT*************************************************************************
def invert_grid():
    global possiblepuz, inverted_possiblepuz
    for r, row in enumerate(possiblepuz):
        for c, cell in enumerate(row):
            inverted_possiblepuz[c][r] = cell

def match_grid_from_invert():
    global possiblepuz, inverted_possiblepuz
    for r, row in enumerate(inverted_possiblepuz):
        for c, cell in enumerate(row):
            possiblepuz[c][r] = cell
# ***********************************INVERT END*********************************************************************


# ***********************************BLOCKIFY***********************************************************************
def blockify_grid():
    global possiblepuz, block_possiblepuz
    for r, row in enumerate(possiblepuz):
        for c, cell in enumerate(row):
            dest_row = block_index[r][c][0]
            dest_col = block_index[r][c][1]
            block_possiblepuz[dest_row][dest_col] = cell

def match_grid_from_block():
    global possiblepuz, block_possiblepuz
    for r, row in enumerate(block_possiblepuz):
        for c, cell in enumerate(row):
            dest_row = block_index[r][c][0]
            dest_col = block_index[r][c][1]
            possiblepuz[dest_row][dest_col] = cell
# ***********************************BLOCKIFY END*******************************************************************


# ***********************************INSERT SINGLE POSSIBLE*********************************************************
def insert_single_possible():
    global action_taken, possiblepuz, testpuz
    for r, row in enumerate(possiblepuz):
        for c, cell in enumerate(row):
            if cell != 0 and len(cell) == 1:
                for x in cell:
                    testpuz[r][c] = x
                    action_taken = True
                possiblepuz[r][c] = 0
# ***********************************INSERT SINGLE POSSIBLE END******************************************************


# ***********************************CHECK SOLUTION******************************************************************
def check_solution():
    global testpuz
    for r, row in enumerate(testpuz):
        for c, cell in enumerate(row):
            if cell == 0:
                return False
    return True
# ***********************************CHECK SOLUTION END**************************************************************


# ***********************************PRINT
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)


if __name__ == '__main__':
    # newpuzzle = get_puzzle()
    solve()
    # print_puzzle(solvedpuzzle)
    print('Final puzzle')
    print_puzzle(testpuz)
    print('Possible puzzle')
    print_puzzle(possiblepuz)
