"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    def slide(line):
        """
        Function that slides a single row or column in 2048
        """
        temp_line = [0]*len(line)
        index_s = 0
        for num in line:
            if num != 0:
                temp_line[index_s] = num
                index_s += 1
        return temp_line
    temp_line = slide(line)
    for index, num in enumerate(temp_line):
        if index < (len(temp_line)-1) and num == temp_line[index+1]:
            temp_line[index] += num
            temp_line[index+1] = 0
    mergedline = slide(temp_line)
    return mergedline

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.TILE_INDICES = {UP: [(0, col) for col in range(self.grid_width)],
                             DOWN: [(self.grid_height-1, col) for col in range(self.grid_width)],
                             LEFT: [(row, 0) for row in range(self.grid_height)],
                             RIGHT: [(row, self.grid_width-1) for row in range(self.grid_height)]}
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.grid = [[0 for col in range(self.grid_width)]
                        for row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = ''
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                grid_str += str(self.grid[row][col]) + ' '
            grid_str += '\n'
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        if direction == UP or DOWN:
            num_steps = self.grid_height
        else:
            num_steps = self.grid_width
        for start_cell in self.TILE_INDICES[direction]:
            tmp_list = []
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                tmp_list.append(self.grid[row][col])
            tmp_list = merge(tmp_list)
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                self.grid[row][col] = tmp_list[step]
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        while True:
            new_row = random.randint(0, self.grid_height-1)
            new_col = random.randint(0, self.grid_width-1)
            if (self.grid[new_row][new_col] == 0):
                self.grid[new_row][new_col] =  2 if random.randint(0, 9) < 8 else 4;
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
