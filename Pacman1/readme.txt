class: Node
    init(maze, action, parent):
        maze
        action
        parent
        initial_state
        goal_state
    
    get_action()
    get_initial_state()
    get_food_location()
    get_successors() (Như của thầy)
    get_successors()
    visualize(action. sleepTime) (vẽ maze)
    printMaze()

class: SearchStrategy
    find_food_lowest_cost(goal_state, node) (tìm chi phí của tất cả food)
    find_cost(goal_node) (tìm đường đi và tọa đồ các đường đi)
    check_food(goal_state, node_remove, path) (kiểm tra trong đường đi có đi qua food không)
    + class: UCS:
        search(node, h) (tìm kiếm, node là trạng thái bắt đầu, h là hàm heuristic)
    + class A_star:
        search(node, h) (tìm kiếm chi phí)
    dấu cộng là có kế thừa

class: heuristic
    def eculid(state, goal_state) 
    def manhattan(state, goal_state)
    => trả về chi phí hàm heuristic

Main:
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
action = UCS()
b = action.search(a, h)
# a.visualize(b, 0.005)
print(len(b))
# # print(a.get_food_location())

# import time
# time1 = time.time()
# action = A_star()
# b = action.search(a, h)
# # a.visualize(b,0.5)

# print(len(b))
# print(time.time() - time1)