
our_grid = [[0, 0, 3, 10],
            [0, 5, 0, 60],
            [5, 10, 5, 0],
            [45, 0, 0, 5]]

directions = {'right': '->', 'left': '<-', 'up': '/\\', 'down': '\\/'}
go = .7
go_back = .2
stay = .1

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

def calculate(current, objective, opposite):
    value = current + (objective * go) + (opposite * go_back) + (current * stay)
    return value

# base case, V1
def v1(sx):
    row, column = translate(sx)
    current_value = our_grid[row][column]
    best_value = 0
    best_direction = 'none'
    for direction in directions:
        column_change = 0
        row_change = 0
        if direction == 'up':
            row_change = -1
        elif direction == 'down':
            row_change = 1
        elif direction == 'right':
            column_change = 1
        elif direction == 'left':
            column_change = -1
        if (row + row_change) < 4 and (row + row_change) > -1 and (column + column_change) < 4 and (column + column_change) > -1:
            objective = our_grid[row + row_change][column + column_change]
        else:
            objective = our_grid[row][column]
        if (row + (row_change*-1)) < 4 and (row + (row_change*-1)) > -1 and (column + (column_change*-1)) < 4 and (column + (column_change*-1)) > -1:
            opposite = our_grid[row + (row_change*-1)][column + (column_change*-1)]
        else:    
            opposite = our_grid[row][column]
        value = calculate(current_value, objective, opposite)
        if value > best_value:
            best_value = value
            best_direction = direction
    return best_value, best_direction

# the recursive generalized case
def vn(sx, n):
    if n == 1:
        value, direction = v1(sx)
        if direction != 'none':
            return round(value, 3), directions[str(direction)]
        else:
            return round(value, 3), 'T'

def value_iteration(n):
    output = [[0 for i in range(4)] for j in range(4)] 
    for i in range(1,17):
        row, column = translate(i)
        output[row][column] = vn(i, n)
    return output

array = value_iteration(1)
for line in array:
    output = ""
    for item in line:
        for small in item:
            output = output + str(small) + "\t"
    print(output)
