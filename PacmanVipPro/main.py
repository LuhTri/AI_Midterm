from Node import Node
from Solve import UCS, A_star
from Heuristic import Heuristic
import time


def read_maze(maze_file):
    with open(maze_file, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze
mazeSize = ['small', 'medium', 'big', 'mediumClassic']
path = f'layouts\\{mazeSize[2]}Maze.lay'


problem = Node(read_maze(path))

def testUCS(sleep):
    time1 = time.time()
    action = UCS()
    path, cost = action.search(problem)
    
    problem.visualize(path, 0.5)
    print('Cost:', cost)
    time2 = time.time()
    print('Executed time:', time2 - time1)

def testAStart():
    h = Heuristic.euclideanDistance
    path = action.search(problem, h)
    
    time1 = time.time()
    action = A_star()
    print(len(path))
    problem.visualize(path, 0.2)
    time2 = time.time()
    print('Executed time:', time2 - time1)


# testUCS()
# testAStart()
