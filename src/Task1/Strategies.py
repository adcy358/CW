from Implementation import Grid
import random
import sys

class Shortest_Path(Grid):

    def __init__(self, length, width): 

        super().__init__(length, width)


    def heuristic_algorithm(self):

        # create the grid 
        plot_grid = self.generate_grid(random.randint(0, 1000))
        grid = self.transform_grid_into_tuple(plot_grid)

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

        #add the values for the last node
        timestep += grid[i_max][j_max]
        steps.append(grid[i_max][j_max])     
        
        return timestep, plot_grid, steps


    def transform_grid_into_tuple(self, grid_array):
        
        grid = tuple(map(tuple, grid_array))

        return grid
    
    
    def transform_grid_into_dict(self, grid_array):
        
        #transform the grid into a dict
        grid_tuple = self.transform_grid_into_tuple(grid_array)
        grid_dict = {}
        
        for i in range(self.length):
            for j in range(self.width):
                grid_dict["node_{}{}".format(i,j)] = grid_tuple[i][j]

        return grid_dict


    def get_neighbours(self, grid_array): 
        
        #transform the grid into a dict where:
        # - keys: correspond to the nodes
        # - values: correspond to dict: {adjacent_node: value}
        
        grid_tuple = self.transform_grid_into_tuple(grid_array)
        
        neighbours = {}
        
        for i in range(self.length-1):
            for j in range(self.width-1):
                neighbours["node_{}{}".format(i,j)] = {
                                                "node_{}{}".format(i+1,j) : grid_tuple[i+1][j] ,
                                                "node_{}{}".format(i,j+1) : grid_tuple[i][j+1]
                                                    }
        
        
        #we add the neighbours of the border nodes
        i_max = self.length-1
        j_max = self.width-1
    
        for j in range(j_max):
            neighbours["node_{}{}".format(i_max, j)] = {"node_{}{}".format(i_max, j+1) : grid_tuple[i_max][j+1]}
        
        for i in range(i_max):
            neighbours["node_{}{}".format(i, j_max)] = {"node_{}{}".format(i+1,j_max) : grid_tuple[i+1][j_max]}

        return neighbours


    def dijkstra_algorithm(self):
        # create the grid 

        plot_grid = self.generate_grid(random.randint(0, 1000))

        grid = self.transform_grid_into_dict(plot_grid)
        #print(grid)

        #list with names of unvisited nodes
        unvisited_nodes = list(grid.keys())
        
        # dict where we store the order of nodes
        previous_nodes = {}
        
        # dict where we store the tentative distances
        shortest_path = {}
        #max_value to initialize the inf value of unvisited nodes
        max_value = sys.maxsize

        for node in unvisited_nodes: 
            shortest_path[node] = max_value
        
        #initialize the starting node's value to zero:
        shortest_path['node_00'] = 0 
        #print(shortest_path)

        # The algorithm executes until we visit all nodes

    #Until here it works fine

        while unvisited_nodes: 
            
            #find the node with the lowest value
            current_min_node = None 

            for node in unvisited_nodes: 
                if current_min_node == None: 
                    current_min_node = node 

                elif shortest_path[node] < shortest_path[current_min_node]: 
                    current_min_node = node

            print("current min node: ", current_min_node)
            neighbours = self.get_neighbours(plot_grid)
            
            '''
            for key, value in neighbours.items():
                print(key, ' : ', value)
            '''

            # The code block below retrieves the current node's neighbors and updates their distances
            
            current_neighbours = list(neighbours[current_min_node].keys()) # list with names of the current node's neighbours
            print(current_neighbours)

            for neighbour in current_neighbours: 

                tentative_value = shortest_path[current_min_node] + neighbours[current_min_node][neighbour]

                if tentative_value < shortest_path[neighbour]: 
                    shortest_path[neighbour] = tentative_value

                    # We also update the best path to the current node
                    previous_nodes[neighbour] = current_min_node

                # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path, plot_grid





game = Shortest_Path(3, 3)
grid = game.dijkstra_algorithm()

'''
timestep, grid, steps  = game.heuristic_algorithm()
print(grid)
print(steps)
print(timestep)

'''


'''
TODO: 

- add condition for when two cells are the same
- transform_grid_into_dict doesn't work for asymmetric grids

'''