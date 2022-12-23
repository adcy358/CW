#Implementation of the game
import numpy as np 

class Grid: 

    def __init__(self, length, width): 
        
        self.length = length
        self.width = width

    def generate_random_grid(self, number_random_states=42):
        # this method generates a random grid of dimensions length x width

        #we generate n=42 methods for generating random numbers
        rng = np.random.RandomState(number_random_states)

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

#game = Grid(4, 3)

#rg = game.generate_random_grid(3)
#cg = game.generate_custom_grid(8, 3, 8, 8, 0, 5, 3, 5, 7, 6, 0, 4)

#print(rg)
#print(cg)

'''
TODO: 
- Fix generate_grid()
    It always generates the same grid for values (width, length)

    
'''

