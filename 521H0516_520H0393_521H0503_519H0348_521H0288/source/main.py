from cgi import test
from problems import SingleFoodSearchProblem, MultiFoodSearchProblem
from fringes import Queue, Stack, PriorityQueue
# from testsearch import bfs, dfs, ucs
from searchAgents import astar, bfs, dfs, euclidean_dis, manhattan_dis, multi_heuristic, ucs, gbfs
import os
os.system('cls')

sizeOfMaze = ['small', 'medium', 'big']
path = f'C:\TDTU\HK4\AI\Midterm\pacman\layouts\{sizeOfMaze[2]}Maze.lay'

# create the problem instance
singleproblem = SingleFoodSearchProblem(path)
multiproblem = MultiFoodSearchProblem(path)
# print(multiproblem.animate())



print(multiproblem.goal_state)


# test UCS algorithm
# actions = ucs(singleproblem)
# singleproblem.animate(actions)
# print(actions)

# actions = ucs(multiproblem)
# multiproblem.animate(actions)
# print(len(actions))


# test astar algorithm
# actions = astar(singleproblem, manhattan_dis)
# singleproblem.animate(actions)
# print(actions)

# actions = astar(multiproblem, multi_heuristic)
# multiproblem.animate(actions)
# print(len(actions))
