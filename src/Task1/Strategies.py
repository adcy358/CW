from Implementation import Grid
import random

class Shortest_Path(Grid):

    def __init__(self, length, width): 

        super().__init__(length, width)

    def heuristic_algorithm(self):

        # create the grid 
        plot_grid = self.generate_grid(random.randint(0, 1000))
        grid = tuple(map(tuple, plot_grid))

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
        
        return timestep, plot_grid, steps


game = Shortest_Path(11, 15)
timestep, grid, steps  = game.heuristic_algorithm()
print(grid)
print(steps)
print(timestep)



'''
TODO: 

- add condition from when two cells are the same


'''