#Implementation of the game
import numpy as np 

class Grid: 

    def __init__(self, length, width): 
        
        self.length = length
        self.width = width

    def generate_random_grid(self, seed=42):
        # this method generates a random grid of dimensions length x width

        #we generate n=42 methods for generating random numbers
        rng = np.random.RandomState(seed)

        #we create our matrix grid (Length x Width)
        grid = np.zeros((self.length, self.width))

        for i in range(self.length): 
            for j in range(self.width): 
                random_number = rng.randint(0, 9)
                grid[i][j] = random_number

        return grid

    def generate_custom_grid(self, *argv):
        # this method generates a specific grid with predefined values

        grid = np.zeros((self.length, self.width))
        index = 0 

        for i in range(self.length): 
            for j in range(self.width): 
                grid[i][j] = argv[index]
                index += 1

        return grid
