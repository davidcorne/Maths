#!/usr/bin/env python
# Written by: DGC

# python imports
import unittest

# local imports
from matrix import *
from Life import *

#==============================================================================
class utest_Life(unittest.TestCase):
    
    def test_under_population(self):
        zero = SquareMatrix(3)
        grid = SquareMatrix(3)
        grid[1][1] = 1
        
        grid = life(grid)
        self.assertEqual(grid, zero)

        # one neighbour
        grid = SquareMatrix(3)
        grid[1][1] = 1
        grid[2][1] = 1
        grid = life(grid)
        self.assertEqual(grid, zero)

        # both have no neighbours
        grid = SquareMatrix(3)
        grid[0][0] = 1
        grid[2][1] = 1
        grid = life(grid)
        self.assertEqual(grid, zero)

    def test_survival(self):
        grid = SquareMatrix(4)
        grid[1][1] = 1
        grid[1][2] = 1
        grid[2][1] = 1

        grid = life(grid)
        # they all have 2 neighbours, they all live
        self.assertEqual(grid[1][1], 1)
        self.assertEqual(grid[1][2], 1)
        self.assertEqual(grid[2][1], 1)

        grid = SquareMatrix(4)
        grid[1][1] = 1
        grid[1][2] = 1
        grid[2][1] = 1
        grid[2][2] = 1

        grid = life(grid)
        # they all have 3 neighbours, they all live
        self.assertEqual(grid[1][1], 1)
        self.assertEqual(grid[1][2], 1)
        self.assertEqual(grid[2][1], 1)
        self.assertEqual(grid[2][2], 1)

    def test_overpopulation(self):
        grid = SquareMatrix(4)
        # 0 0 0 0    0 0 0 0
        # 0 1 0 0 -> 0 1 0 0
        # 0 1 1 1 -> 1 1 0 0 
        # 0 1 0 0    0 1 0 0
        grid[1][1] = 1 # has 2 neighbours - survives
        grid[1][2] = 1 # has 3 neighbours - survives
        grid[1][3] = 1 # has 2 neighbours - survives
        grid[2][2] = 1 # has 4 neighbours - going to die
        grid[3][2] = 1 # has 1 neighbour  - going to die
        grid[0][2] = 0 # has 3 neighbours - going to live
        
        grid = life(grid)
        
        self.assertEqual(grid[1][1], 1)
        self.assertEqual(grid[1][2], 1)
        self.assertEqual(grid[1][3], 1)
        self.assertEqual(grid[2][2], 0)
        self.assertEqual(grid[3][2], 0)
        self.assertEqual(grid[0][2], 1)

        grid = SquareMatrix(3, lambda a,b: 1)
        grid = life(grid)
        self.assertEqual(grid[1][1], 0)

    def test_reproduction(self):
        grid = SquareMatrix(2, lambda a,b: 1)
        grid[1][1] = 0
        grid = life(grid)
        self.assertEqual(grid[1][1], 1)

#==============================================================================
class utest_Patterns(unittest.TestCase):
    
    def test_block(self):
        """
        Block is a stable pattern

        0 0 0 0
        0 1 1 0
        0 1 1 0
        0 0 0 0
        """
        grid = SquareMatrix(4)
        grid[1][1] = 1
        grid[2][1] = 1
        grid[1][2] = 1
        grid[2][2] = 1

        original_grid = copy.copy(grid)
        
        self.assertEqual(original_grid, grid, "Check they start the same.")
        grid = life(grid)
        self.assertEqual(original_grid, grid)
        grid = life(grid)
        self.assertEqual(original_grid, grid)

    def test_beehive(self):
        """
        Beehive is a stable pattern

        0 0 0 0 0 0
        0 0 1 1 0 0
        0 1 0 0 1 0
        0 0 1 1 0 0
        0 0 0 0 0 0
        """
        grid = Matrix(6, 5)
        grid[2][1] = 1
        grid[3][1] = 1
        grid[1][2] = 1
        grid[4][2] = 1
        grid[2][3] = 1
        grid[3][3] = 1
        
        original_grid = copy.copy(grid)
        
        self.assertEqual(original_grid, grid, "Check they start the same.")
        grid = life(grid)
        self.assertEqual(original_grid, grid)
        grid = life(grid)
        self.assertEqual(original_grid, grid)

    def test_loaf(self):
        """
        Loaf is a stable pattern

        0 0 0 0 0 0
        0 0 1 1 0 0
        0 1 0 0 1 0
        0 0 1 0 1 0
        0 0 0 1 0 0
        0 0 0 0 0 0
        """
        grid = SquareMatrix(6)
        grid[2][1] = 1
        grid[3][1] = 1
        grid[1][2] = 1
        grid[4][2] = 1
        grid[2][3] = 1
        grid[4][3] = 1
        grid[3][4] = 1
        
        original_grid = copy.copy(grid)
        
        self.assertEqual(original_grid, grid, "Check they start the same.")
        grid = life(grid)
        self.assertEqual(original_grid, grid)
        grid = life(grid)
        self.assertEqual(original_grid, grid)

    def test_boat(self):
        """
        boat is a stable pattern.
        
        0 0 0 0 0 
        0 1 1 0 0
        0 1 0 1 0
        0 0 1 0 0
        """
        grid = SquareMatrix(5)
        grid[1][1] = 1
        grid[2][1] = 1
        grid[1][2] = 1
        grid[3][2] = 1
        grid[2][3] = 1
        
        original_grid = copy.copy(grid)
        
        self.assertEqual(original_grid, grid, "Check they start the same.")
        grid = life(grid)
        self.assertEqual(original_grid, grid)
        grid = life(grid)
        self.assertEqual(original_grid, grid)

    def test_blinker(self):
        """
        Blinker is a periodic pattern with period 2.
        
        It switches between
        
        0 0 0 0 0 
        0 0 1 0 0 
        0 0 1 0 0 
        0 0 1 0 0 
        0 0 0 0 0 

        and
        
        0 0 0 0 0 
        0 0 0 0 0 
        0 1 1 1 0 
        0 0 0 0 0 
        0 0 0 0 0 
        """
        grid = blinker(5, 5)
        
        original_grid = copy.copy(grid)
        grid = life(grid)
        second = copy.copy(grid)
        grid = life(grid)
        self.assertEqual(grid, original_grid)
        grid = life(grid)
        self.assertEqual(grid, second)

    def test_pulsar(self):
        """
        Pulsar is a periodic pattern with period 3.
        """
        grid = pulsar(30, 30)
        self.assertEqual(grid.x, 30)
        self.assertEqual(grid.y, 30)

        original_grid = copy.copy(grid)
        grid = life(grid)
        second = copy.copy(grid)
        grid = life(grid)
        third = copy.copy(grid)
        grid = life(grid)
        self.assertEqual(grid, original_grid)
        grid = life(grid)
        self.assertEqual(grid, second)
        grid = life(grid)
        self.assertEqual(grid, third)

#==============================================================================
if (__name__ == "__main__"):
    unittest.main(verbosity=2)
