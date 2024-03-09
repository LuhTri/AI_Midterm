from Node import Node
from Heuristic import Heuristic


class SearchStrategy:
    def find_food_lowest_cost(self, goal_state, node: Node):
        cost_food = []
        for i in goal_state:
            cost_food.append(
                (Heuristic.euclideanDistance(node.get_initial_state(), i), i))
        cost_food.sort()
        return cost_food

    def cost_sort(self, n):
        return n[0]

    def sort_cost(self, frontier):
        return sorted(frontier, key=self.cost_sort)

    def heap_push(self, cost_and_successor, frontier):
        cost, a, successor = cost_and_successor
        frontier.append((cost, a, successor))
        frontier = self.sort_cost(frontier)
        return frontier

    def check_frontier(self, frontier, successor):
        for i in frontier:
            cost, action, node = i
            if node.get_initial_state() == successor.get_initial_state():
                return False
        return True

    def remove(self, goal_node, goal_state):
        for i in goal_node:
            if i == goal_state:
                goal_node.remove(i)
                break
        return goal_node

    def find_cost(self, state, successor_state):
        Px, Py = state
        Fx, Fy = successor_state
        return (((Px - Fx) ** 2 + (Py - Fy) ** 2) ** (1/2))

    def find_action(self, goal_node):
        path = []
        path_a = []
        current_node = goal_node
        while current_node.parent:
            path.insert(0, current_node.get_action())
            path_a.insert(0, current_node.get_initial_state())
            current_node = current_node.parent
        return path, path_a

    def check_food(self, goal_state, node_remove, path):
        goal_state = self.remove(goal_state, node_remove)
        for i in path:
            if i in goal_state:
                goal_state = self.remove(goal_state, i)
        return goal_state

    def is_goal(self, goal_state, current_state):
        if current_state.get_initial_state() in goal_state:
            return True
        return False
