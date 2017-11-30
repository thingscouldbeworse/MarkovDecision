
our_grid = [[0, 0, 3, 10],
            [0, 5, 0, 60],
            [5, 10, 5, 0],
            [45, 0, 0, 5]]

sx_grid = [ [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

directions = {'right': '->', 'left': '<-', 'up': '/\\', 'down': '\\/'}
go = .7
go_back = .2
stay = .1

# a number (1-16) to block coordinates in `our_grid`
def translate(sx): 
    column = (sx % 4) - 1
    if column == -1:
        column = 3
    if sx < 5:
        row = 0
    elif sx < 9:
        row = 1
    elif sx < 13:
        row = 2
    elif sx < 17:
        row = 3

    return row, column

# calculate the expected value based on the given `go`, `go_back`, and `stay` constants
def calculate(current, objective, opposite):
    value = current + (objective * go) + (opposite * go_back) + (current * stay)
    return value

# find the blocks contiguous to the current block, with options to bounce off walls
def direction_taker(sx, opposite=False, bounce=False):
    row, column = translate(sx)
    objectives = []
    flip = 1
    if opposite:
        flip = -1

    for direction in directions:
        column_change = 0
        row_change = 0
        if direction == 'up':
            row_change = -1 * flip
        elif direction == 'down':
            row_change = 1 * flip
        elif direction == 'right':
            column_change = 1 * flip
        elif direction == 'left':
            column_change = -1 * flip
        if (row + row_change) < 4 and (row + row_change) > -1 and (column + column_change) < 4 and (column + column_change) > -1:
            objective = [row + row_change, column + column_change, direction]
            objectives.append(objective)
        elif bounce:
            objective = [row, column, direction]  
            objectives.append(objective)

    return objectives

# base case, V1
def v1(sx, value_grid):
    row, column = translate(sx)
    current_value = value_grid[row][column]
    best_value = 0
    best_direction = 'none'
    objectives = direction_taker(sx, opposite=False, bounce=True)
    opposites = direction_taker(sx, opposite=True, bounce=True)

    for i in range(0,len(objectives)):
        obj_value = value_grid[objectives[i][0]][objectives[i][1]]
        ops_value = value_grid[opposites[i][0]][opposites[i][1]]
        value = calculate(current_value, obj_value, ops_value)

        direction = objectives[i][2]

        if value > best_value:
            best_value = value
            best_direction = direction
    return best_value, best_direction

# the recursive generalized case
def vn(sx, n, value_grid):
    if n == 1:
        value, direction = v1(sx, value_grid)
    else: # recursively find adjacent blocks and count down
        for i in range(0, n):
            adjacent_blocks = direction_taker(sx)
            for block in adjacent_blocks:
                value, direction = vn(sx_grid[block[0]][block[1]], n-1, value_grid)
                value_grid[block[0]][block[1]] = value

    if direction != 'none':
        #return round(value, 3), directions[str(direction)]
        return value, direction
    else:
        return value, 'T'

def value_iteration(n, value_grid):
    output = [[0 for i in range(4)] for j in range(4)] 
    for i in range(1,17):
        row, column = translate(i)
        output[row][column] = vn(i, n, value_grid)
    return output

def pretty_print(policy_grid):
    for line in array:
        output = ""
        for item in line:
            for small in item:
                try:
                    test = int(small)
                    small = round(small, 3)
                except:
                    if small == 'none':
                        small = 'T'
                    else:
                        small = directions[small]
                output = output + str(small).ljust(8) + "\t"
        print(output)

#array = value_iteration(2, our_grid)
#pretty_print(array)

