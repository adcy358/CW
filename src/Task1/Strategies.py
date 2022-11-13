from Implementation import Grid
import random
import sys

class Shortest_Path(Grid):

    def __init__(self, length, width): 

        super().__init__(length, width)


    def heuristic_algorithm(self, plot_grid):
        
        grid = self.transform_grid_into_tuple(plot_grid)

        i = 0 
        j = 0 
        timestep = grid[i][j]
        
        #keep track of steps
        shortest_path = []
        shortest_path.append(f"node_{i}{j}")

        i_max = self.length - 1
        j_max = self.width - 1

        while i != i_max and j!= j_max:

            new_i = i 
            new_j = j+1

            if grid[new_i][new_j] > grid[i+1][j]: 
                new_i = i + 1
                new_j = j 
            
            timestep += grid[new_i][new_j]
            
            shortest_path.append(f"node_{new_i}{new_j}")

            i = new_i #update i 
            j = new_j #update j 

            # if they reach a border
            if i == i_max: 
                for y in range(1,j_max-j):
                    timestep += grid[i][j+y]
                    shortest_path.append(f"node_{i}{j+y}")

            if j == j_max: 
                for x in range(1, i_max-i):
                    timestep += grid[i+x][j]
                    shortest_path.append(f"node_{i+x}{j}")
                    

        #add the values for the last node
        timestep += grid[i_max][j_max]
        shortest_path.append(f"node_{i_max}{j_max}")  
        
        return shortest_path, timestep


    def transform_grid_into_tuple(self, grid_array):
        
        grid = tuple(map(tuple, grid_array))

        return grid
    
    
    def transform_grid_into_dict(self, grid_array):
        
        #transform the grid into a dict
        grid_tuple = self.transform_grid_into_tuple(grid_array)
        grid_dict = {}
        
        for i in range(self.length):
            for j in range(self.width):
                grid_dict[f"node_{i}{j}"] = grid_tuple[i][j]

        return grid_dict


    def get_neighbours(self, grid_array): 
        
        #transform the grid into a dict where:
        # - keys: correspond to the nodes
        # - values: correspond to dict: {adjacent_node: value}
        
        grid_tuple = self.transform_grid_into_tuple(grid_array)
        
        neighbours = {}
        
        for i in range(self.length-1):
            for j in range(self.width-1):
                neighbours[f"node_{i}{j}"] = {
                                                f"node_{i+1}{j}" : grid_tuple[i+1][j] ,
                                                f"node_{i}{j+1}" : grid_tuple[i][j+1]
                                                    }
        
        
        #we add the neighbours of the border nodes
        i_max = self.length-1
        j_max = self.width-1
    
        for j in range(j_max):
            neighbours[f"node_{i_max}{j}"] = {f"node_{i_max}{j+1}" : grid_tuple[i_max][j+1]}
        
        for i in range(i_max):
            neighbours[f"node_{i}{j_max}"] = {f"node_{i+1}{j_max}" : grid_tuple[i+1][j_max]}

        neighbours[f"node_{i_max}{j_max}"] = {f"node_{i_max}{j_max}" : 0}
        
        return neighbours


    def dijkstra_algorithm(self, plot_grid):

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
        
        #initialize the starting node's value to the corresponding one:
        shortest_path['node_00'] = grid['node_00']

        # The algorithm executes until we visit all nodes

    #Until here it works fine
        last_node = list(grid)[-1]

        while last_node in unvisited_nodes: 
            
            # This code block finds the node with the lowest value
            current_min_node = None 

            for node in unvisited_nodes: 
                if current_min_node == None: 
                    current_min_node = node 

                elif shortest_path[node] < shortest_path[current_min_node]: 
                    current_min_node = node


            # The code block below retrieves the current node's neighbors and updates their distances
            neighbours = self.get_neighbours(plot_grid) 
            current_neighbours = list(neighbours[current_min_node].keys()) # list with names of the current node's neighbours

            for neighbour in current_neighbours: 

                tentative_value = shortest_path[current_min_node] + neighbours[current_min_node][neighbour]
                
                if tentative_value < shortest_path[neighbour]: 
                    shortest_path[neighbour] = tentative_value

                    # We also update the best path to the current node
                    previous_nodes[neighbour] = current_min_node

            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
        
        timestep = shortest_path[last_node]

        return shortest_path, timestep, previous_nodes



game = Shortest_Path(5, 5)

#generate grid
grid = game.generate_grid(random.randint(0, 1000))
print(grid)

#dijkstra's algorithm
shortest_path, timestep, previous_nodes = game.dijkstra_algorithm(grid)
print('Shortest path: ')
print(shortest_path)
print('')
print('Previous nodes:')
print(previous_nodes)
print('')
print('Timestep: ')
print(timestep)

'''
#heuristic algorithm
shortest_path, timestep  = game.heuristic_algorithm(grid)
print(shortest_path)
print('heuristic: ', timestep)

'''







'''
TODO: 

- add condition for when two cells are the same
- transform_grid_into_dict doesn't work for asymmetric grids

'''

'''Notes: 

My Heuristic algorithm has several issues: 

- it doesn't take into account when two neighbour cell have the same value 

'''