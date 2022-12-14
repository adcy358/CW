from Implementation import Grid
import numpy as np 
import random
import sys

class Shortest_Path(Grid):
    """ This class contains two methods that find the shortest path 
        and the helper functions to execute them """
    def __init__(self, length, width): 
        super().__init__(length, width)

    def heuristic_algorithm(self, plot_grid):
        """ This method implements the Heuristic Algorithm """
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
        """ This method transforms the grid as an array into a tuple  """
        grid = tuple(map(tuple, grid_array))
        return grid
    
    def transform_grid_into_dict(self, grid_array):   
        """ This method transform the grid as an array into a dictionary """
        grid_tuple = self.transform_grid_into_tuple(grid_array)
        grid_dict = {}
        for i in range(self.length):
            for j in range(self.width):
                grid_dict[f"node_{i}{j}"] = grid_tuple[i][j]

        return grid_dict

    def transform_dict_into_grid(self, grid_dict):
        """ This method transforms the dictionary into a grid for display"""
        grid = np.zeros((self.length, self.width))
        for i in range(self.length): 
            for j in range(self.width): 
                grid[i][j] = grid_dict[f"node_{i}{j}"]

        return grid

    def get_neighbours(self, grid_array):    
        """ This method transforms the grid into a dict where:
                - keys: correspond to the nodes
                - values: correspond to another dict: {adjacent_node: value} """
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
        """ This method implements the Dijkstra Algorithm """
        # Reference used: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
        grid = self.transform_grid_into_dict(plot_grid)

        unvisited_nodes = list(grid.keys()) #list with names of unvisited nodes
        previous_nodes = {} # dict where we store the order of nodes
        shortest_path = {} # dict where we store the tentative distances
        max_value = sys.maxsize # max_value to initialize the inf value of unvisited nodes
        for node in unvisited_nodes: 
            shortest_path[node] = max_value
        
        # initialize the starting node's value to the corresponding one:
        shortest_path['node_00'] = grid['node_00']

        # the algorithm executes until we visit all nodes
        last_node = list(grid)[-1]
        while last_node in unvisited_nodes: 
            # this code block finds the node with the lowest value
            current_min_node = None 
            for node in unvisited_nodes: 
                if current_min_node == None: 
                    current_min_node = node 

                elif shortest_path[node] < shortest_path[current_min_node]: 
                    current_min_node = node

            # the code block below retrieves the current node's neighbors and updates their distances
            neighbours = self.get_neighbours(plot_grid) 
            current_neighbours = list(neighbours[current_min_node].keys()) # list with names of the current node's neighbours
            for neighbour in current_neighbours: 
                tentative_value = shortest_path[current_min_node] + neighbours[current_min_node][neighbour]
                if tentative_value < shortest_path[neighbour]: 
                    shortest_path[neighbour] = tentative_value
                    # we also update the best path to the current node
                    previous_nodes[neighbour] = current_min_node
            # after visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)

        timestep = shortest_path[last_node]
        shortest_path_grid = self.transform_dict_into_grid(shortest_path)

        return shortest_path, timestep, previous_nodes, shortest_path_grid


