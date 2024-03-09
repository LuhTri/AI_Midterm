import math
import os
import time

class MultiFoodSearchProblem:
    def __init__(self, maze_file):
        self.maze = self.read_maze(maze_file)
        self.initial_state = self.get_initial_state()
        self.goal_state = self.get_food_location()

    def read_maze(self, maze_file):
        with open(maze_file, "r") as f:
            maze = [[char for char in line.strip()] for line in f]
        return maze

    def get_initial_state(self):
        for i, x in enumerate(self.maze):
            if "P" in x:
                return (i, x.index("P"))

    def get_food_location(self):
        all_food = []
        for i, x in enumerate(self.maze):
            index = 0
            for j in x:
                if j == ".":
                    all_food.append((i, index))
                index += 1
        return all_food

    def get_successors(self, state):
        x, y = state
        successors = []
        if x > 0 and self.maze[x - 1][y] != "%":  # Check Up
            successors.append(((x - 1, y), 1, "N"))
        if y < len(self.maze[0]) - 1 and self.maze[x][y + 1] != "%":  # Check Right
            successors.append(((x, y + 1), 1, "E"))
        if x < len(self.maze) - 1 and self.maze[x + 1][y] != "%":  # Check Down
            successors.append(((x + 1, y), 1, "S"))
        if y > 0 and self.maze[x][y - 1] != "%":  # Check Left
            successors.append(((x, y - 1), 1, "W"))
        successors.sort()
        return successors

    def is_goal(self, state):
        return state in self.goal_state

    def get_cost(self, state, action, next_state):
        return action[1]

    def print_maze(self):
        os.system("cls" if os.name == "nt" else "clear")
        for x in self.maze:
            print("".join(x))

    def animate(self, actions):
        os.system("cls" if os.name == "nt" else "clear")
        self.print_maze()
        # input("Press Enter to continue...")
        current_state = self.get_initial_state()
        for action in actions:
            os.system("cls" if os.name == "nt" else "clear")

            # remove pacman from current location
            self.maze[current_state[0]][current_state[1]] = " "
            if action == "N":
                current_state = (current_state[0] - 1, current_state[1])
            elif action == "S":
                current_state = (current_state[0] + 1, current_state[1])
            elif action == "E":
                current_state = (current_state[0], current_state[1] + 1)
            elif action == "W":
                current_state = (current_state[0], current_state[1] - 1)

            # add pacman to new location
            self.maze[current_state[0]][current_state[1]] = "P"
            self.print_maze()
            if action == "Stop":
                print("Pacman has reached all goals!")
                break
            time.sleep(0.01)
