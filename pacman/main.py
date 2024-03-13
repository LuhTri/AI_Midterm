from Node import Node
from Solve import UCS, A_star
from Heuristic import Heuristic
import time


def read_maze(maze_file):
    with open(maze_file, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze


mazeSize = ['small', 'medium', 'big']
path = f'layouts\\{mazeSize[2]}Maze.lay'


problem = Node(read_maze(path))


def testUCS():
    # time1 = time.time()
    action = UCS()
    path, cost = action.search(problem)

    problem.visualize(path, 0.05)
    print('Actions:\n', path)
    print('Cost:', cost)
    # time2 = time.time()
    # print('Executed time:', time2 - time1)


def testAStart(h):
    action = A_star()
    path, cost = action.search(problem, h)

    time1 = time.time()

    problem.visualize(path, 0.05)
    time2 = time.time()
    print('Actions:\n', path)
    print('Cost:', cost)
    # print('Executed time:', time2 - time1)


h = Heuristic.euclideanDistance
h1 = Heuristic.manhattanDistance
# testUCS()
testAStart(h1)
