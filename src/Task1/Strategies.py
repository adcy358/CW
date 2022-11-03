from tkinter import X
from turtle import xcor
from Implementation import Grid

class Shortest_Path(Grid):

    def __init__(self, length, width): 

        super().__init__(length, width)

    def heuristic_algorithm(self):

        # create the grid 
        grid = self.convert_to_tuple()

        i = 0 
        j = 0 
        timestep = grid[i][j]
        
        #keep track of steps
        steps = []
        steps.append(grid[i][j])

        i_max = self.length - 1
        j_max = self.width - 1

        while i != i_max and j!= j_max:

            new_i = i 
            new_j = j+1

            if grid[new_i][new_j] > grid[i+1][j]: 
                new_i = i + 1
                new_j = j 
            
            timestep += grid[new_i][new_j]
            
            steps.append(grid[new_i][new_j])

            i = new_i #update i 
            j = new_j #update j 

            # if they reach a border
            if i == i_max: 
                for y in range(1,j_max-j):
                    timestep += grid[i][j+y]
                    steps.append(grid[i][j+y])

            if j == j_max: 
                for x in range(1, i_max-i):
                    timestep += grid[i+x][j]
                    steps.append(grid[i+x][j])

        timestep += grid[i_max][j_max]
        
        steps.append(grid[i_max][j_max])     
        print(steps)
        
        return timestep 


game = Shortest_Path(11, 15)
print(game.heuristic_algorithm())
game.plot()


'''
TODO: 


'''