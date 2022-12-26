from Strategies import *

game = Shortest_Path(9, 9)

#generate grid
grid = game.generate_random_grid(9)
print(grid)


#dijkstra's algorithm
shortest_path, timestep, previous_nodes, shortest_path_grid = game.dijkstra_algorithm(grid)
print('Shortest path: ')
print(shortest_path)
print('')
print('Previous nodes:')
print(previous_nodes)
print('')
print('Timestep: ')
print(timestep)


#heuristic algorithm
shortest_path, timestep  = game.heuristic_algorithm(grid)
print(shortest_path)
print('heuristic: ', timestep)