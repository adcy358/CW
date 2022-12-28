from Strategies import *

game = Shortest_Path(3, 3)
seed = 9 

# Generate grid
grid = game.generate_random_grid(seed)
print("-------------------------------")
print('GRID')
print("-------------------------------")
print('Grid: ')
print(grid)
print("-------------------------------")

# Dijkstra's algorithm
shortest_path, timestep, previous_nodes, shortest_path_grid = game.dijkstra_algorithm(grid)
print("DIJKSTRA'S ALGORITHM")
print("-------------------------------")
print('Shortest path: ')
print(shortest_path)
print('')
print('Previous nodes:')
print(previous_nodes)
print('')
print('Timesteps: ')
print(timestep)
print("-------------------------------")

# Heuristic algorithm
shortest_path, timestep  = game.heuristic_algorithm(grid)
print("HEURISTIC ALGORITHM")
print("-------------------------------")
print('Shortest path: ')
print(shortest_path)
print('')
print('Timesteps: ', timestep)
print("-------------------------------")