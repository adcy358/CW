#Implementation of the game
import numpy as np 

class Grid: 

    def __init__(self, length, width): 
        
        self.length = length
        self.width = width

    def generate_grid(self, number_random_states=42):

        #we generate n=42 methods for generating random numbers
        rng = np.random.RandomState(number_random_states)

        #we create our matrix grid (Length x Width)
        grid = np.zeros((self.length, self.width))

        for i in range(self.length): 
            for j in range(self.width): 
                random_number = rng.random_integers(0,9)
                grid[i][j] = random_number

        return grid
    
    def convert_to_tuple(self):
        
        grid = tuple(map(tuple, self.generate_grid()))

        return grid

    def plot(self): 
        
        grid = self.generate_grid()
        
        return(print(grid))


'''
TODO: 
- Fix generate_grid()
    It always generates the same grid for values (width, length)
'''