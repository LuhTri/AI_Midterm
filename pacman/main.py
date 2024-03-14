from Node import Node
from Solve import UCS, A_star
from Heuristic import Heuristic
import sys


def read_maze(maze_file):
    with open(maze_file, "r") as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze


h1 = Heuristic.manhattanDistance
h2 = Heuristic.euclideanDistance


if len(sys.argv) < 4:
    _, mazeSize, searchStrategy = sys.argv
else:
    _, mazeSize, searchStrategy, heuristic = sys.argv

path = f"layouts\\{mazeSize}.lay"


if searchStrategy.upper() == 'UCS':
    problem = Node(read_maze(path))
    ucs = UCS()
    path, cost = ucs.search(problem)

elif searchStrategy.upper() == 'ASTAR':
    problem = Node(read_maze(path))

    astar = A_star()

    if heuristic == 'h1':
        path, cost = astar.search(problem, h1)
    elif heuristic == 'h2':
        path, cost = astar.search(problem, h2)


problem.visualize(path, sleepTime=0.03)
print(f'\n{searchStrategy.upper()} - {mazeSize}')
print("Total Cost:", cost)
print("Path:\n", path)
