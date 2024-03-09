from Node import Node
from Solve import UCS, A_star
from Heuristic import Heuristic
import time
def read_maze(maze_file):
    with open(maze_file, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze
mazeSize = ['small', 'medium', 'big', 'mediumClassic']
path = f'layouts\{mazeSize[2]}Maze.lay'
a = Node(read_maze(path))

# action = UCS()
# b = action.search(a)
# a.visualize(b, 0.05)
# print(len(b))
# print(a.get_food_location())

# import time
h = Heuristic.euclideanDistance
time1 = time.time()
action = A_star()
b = action.search(a, h)
# a.visualize(b,1)

print(len(b))
# print(a.get_food_location())
# print(time.time() - time1)