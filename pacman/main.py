from Node import Node
from Solve import UCS, A_star
from Heuristic import Heuristic
def read_maze(maze_file):
    with open(maze_file, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze
mazeSize = ['small', 'medium', 'big', 'mediumClassic']
path = f'layouts\{mazeSize[2]}Maze.lay'
a = Node(read_maze(path))


h = Heuristic.euclideanDistance
# action = UCS()
# b = action.search(a, h)
# a.visualize(b, 0.005)
# print(a.get_food_location())
# print(len(b))


import time
time1 = time.time()
action = A_star()
b = action.search(a, h)
# a.visualize(b,0.1)

print(len(b))
print(time.time() - time1)