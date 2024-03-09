from copy import deepcopy
import os
import time
class Node:
    def __init__(self, maze: list, action: list = None, parent = None):
        self.maze = maze
        self.action = action
        self.parent = parent
        self.initial_state = self.get_initial_state() # Position of Pacman
        self.goal_state = self.get_food_location()

    # Getter
    def get_action(self) -> list:
        return self.action


    def get_initial_state(self) -> tuple:
        """
        Get position of Pacman in maze
        """
        for i, x in enumerate(self.maze):
            if 'P' in x:
                return (i, x.index('P'))
            

    def get_food_location(self) -> list:
        foods = []
        for row, col in enumerate(self.maze):
            colIndex = 0
            for j in col:
                if j == '.':
                    foods.append((row, colIndex) )
                colIndex += 1

        # Considering corner as a food and append to 'foods'
        corner = [(1, 1), (1, len(self.maze[1]) - 2), ((len(self.maze) - 2), 1), (len(self.maze) - 2, len(self.maze[1]) - 2)]
        for i in corner:
            if i not in foods and self.maze[i[0]][i[1]] != '%':
                foods.append((i[0], i[1]))
        return foods
    

    def get_successors(self) -> list:
        successors = []
        actions = ['N', 'E', 'W', 'S']

        for action in actions:
            successor_state = self.get_successor(action, deepcopy(self.maze))
            if successor_state is not None:
                successors.append(Node(successor_state, action, self))

        return successors
    
    
    def get_successor(self, action, state) -> list | None:
        # Check at position x, y of maze is a barrier or not
        isBarrier = lambda x, y: self.maze[x][y] == '%'

        x, y = self.initial_state # x is row index, y is column index
        rowLenght , colLength = len(self.maze), len(self.maze[0]) - 1
        flag = False

        if 0 <= x and x < rowLenght and 0 <= y and y < colLength:
            # Check go UP
            if action == 'N' and not isBarrier(x - 1, y):
                state[x - 1][y] = state[x][y]
                flag = True
            # Check go RIGHT
            if action == 'E' and not isBarrier(x, y + 1):
                state[x][y + 1] = state[x][y]
                flag = True
            # Check go DOWN
            if action == 'S' and not isBarrier(x + 1, y):
                state[x + 1][y] = state[x][y]
                flag = True
            # Check go LEFT
            if action == 'W' and not isBarrier(x, y - 1):
                state[x][y - 1] = state[x][y]
                flag = True

            if flag:
                state[x][y] = ' '
                return state
        return None
    
    
    def printMaze(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in self.maze:
            print("".join(x))

    
    def visualize(self, actions, sleepTime=1) -> None:
        # Postion of Pacman in initial state wherr x is row index, y is column index
        x, y = self.get_initial_state() 

        os.system('cls' if os.name == 'nt' else 'clear')
        self.printMaze()

        for action in actions:
            os.system('cls' if os.name == 'nt' else 'clear')

        # Update pacman's postion after action
            self.maze[x][y] = ' '

            # Check action
            if action == 'N': # Go UP
                x -= 1
            elif action == 'E': # Go RIGHT
                y += 1
            elif action == 'S': # Go DOWN
                x += 1
            elif action == 'W': # GO LEFT
                y -= 1
            else: # STOP
                self.printMaze()
                break

            # New pacman's position
            self.maze[x][y] = 'P'

            self.printMaze()
            time.sleep(sleepTime) 


