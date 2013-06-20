#!/usr/bin/env python
# Written by: DGC

# python imports
import time

# local imports
import matrix

# dict which has number of live neighbours as a key and returns what to do with
# a live cell
LIVE = {
    0: 0,
    1: 0,
    2: 1,
    3: 1,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    }

# dict which has number of live neighbours as a key and returns what to do with
# a dead cell
DEAD = {
    0: 0,
    1: 0,
    2: 0,
    3: 1,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    }

#==============================================================================
def life(grid):
    """
    1. Any live cell with fewer than two live neighbours dies, as if caused by 
       under-population.
    2. Any live cell with two or three live neighbours lives on to the next 
       generation.
    3. Any live cell with more than three live neighbours dies, as if by 
       overcrowding.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as
       if by reproduction.
    """
    new_grid = matrix.Matrix(grid.x, grid.y)
    for i in range(grid.x):
        for j in range(grid.y):
            neighbours = live_neighbours(i, j, grid)
            if (grid[i][j]):
                new_grid[i][j] = LIVE[neighbours]
            else:
                new_grid[i][j] = DEAD[neighbours]
    return new_grid

#==============================================================================
def live_neighbours(x, y, grid):
    """
    Returns the number of live neighbours of cell (x, y) in grid.
    """
    count = list()
    if (0 <= x-1 and 0 <= y-1):
        count.append(grid[x-1][y-1])
    if (0 <= x-1):
        count.append(grid[x-1][y])
    if (0 <= x-1 and y+1 < grid.y):
        count.append(grid[x-1][y+1])
    if (0 <= y-1):
        count.append(grid[x][y-1])
    if (y+1 < grid.y):
        count.append(grid[x][y+1])
    if (x+1 < grid.x and 0 <= y-1):
        count.append(grid[x+1][y-1])
    if (x+1 < grid.x):
        count.append(grid[x+1][y])
    if (x+1 < grid.x and y+1 < grid.y):
        count.append(grid[x+1][y+1])
    return sum(count)

#==============================================================================
def glider(x, y):
    """
    Returns an x by y matrix with the top left corner containing this
    
    0 0 0 0
    0 0 0 1
    0 1 0 1
    0 0 1 1
    
    Precondition: x > 3 and y > 3
    """
    assert x > 3 and y > 3
    glider = matrix.Matrix(x, y)
    glider[3][1] = 1
    glider[1][2] = 1
    glider[3][2] = 1
    glider[2][3] = 1
    glider[3][3] = 1
    return glider

def blinker(x, y):
    """
    Returns an x by y matrix with the top left corner containing this
    
    0 0 0 0 0
    0 0 1 0 0
    0 0 1 0 0
    0 0 1 0 0
    0 0 0 0 0
    
    Precondition: x > 4 and y > 4
    """
    assert x > 4 and y > 4
    blinker = matrix.Matrix(x, y)
    blinker[2][1] = 1
    blinker[2][2] = 1
    blinker[2][3] = 1
    return blinker

def pulsar(x, y):
    """
    Returns an x by y matrix with the top left corner containing this
    
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 
    0 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 
    0 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 
    0 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0     
    0 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 
    0 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 
    0 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 
    0 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    """
    assert x > 17 and y > 17
    
    # need to use padding to get the correct dimensions
    x_pad = (x - 17) * [0] 
    pad = x * [0]
    y_pad = (y - 17) * [pad]
    pulsar = matrix.Matrix.FromRows(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, ] + x_pad,
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, ] + x_pad,
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, ] + x_pad,
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, ] + x_pad,
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ] + x_pad,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ] + x_pad,
            ] + y_pad
        )
    return pulsar

#==============================================================================
if (__name__ == "__main__"):
    grid = pulsar(15, 15)
    for i in range(2):
        time.sleep(0.25)
        print(grid)
        print
        grid = life(grid)
