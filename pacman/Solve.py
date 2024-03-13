from Node import Node
from Search import SearchStrategy
from copy import deepcopy
import time


class UCS(SearchStrategy):
    def search(self, node: Node):
        actions = []
        cost_all = 0
        frontier = [(0, [], node)]
        goal_state = node.get_food_location()
        while len(goal_state) > 0:
            explored = dict()
            while len(frontier) != 0:
                cost, action, state = frontier.pop(0)
                if super().is_goal(goal_state, state):
                    goal_state = super().remove(goal_state, state.get_initial_state())
                    frontier = [(0, action, state)]
                    cost_all += cost
                    break
                successors = state.get_successors()
                for successor in successors:
                    if successor.get_initial_state() not in explored or (explored[successor.get_initial_state()] > cost + 1):
                        newCost = cost + 1
                        explored[successor.get_initial_state()] = newCost
                        newAction = action + [successor.get_action()]
                        frontier = super().heap_push(
                            (newCost, newAction, successor), frontier)
        actions = action
        actions.append("Stop")
        return actions, cost_all


class A_star(SearchStrategy):
    def search(self, node: Node, h: callable):
        actions = []
        cost_all = 0
        goal_state = node.get_food_location()
        frontier = [(h(node, goal_state), 0, [], node)]
        while goal_state:
            explored = []
            while frontier is not None:
                cost, cost_path, action, state = frontier.pop(0)
                explored.append(state.get_initial_state())
                if super().is_goal(goal_state, state):
                    frontier = [(h(state, goal_state), 0, action, state)]
                    explored = []
                    if cost < 0:
                        cost = cost_path
                    cost_all += cost
                    goal_state = super().remove(goal_state, state.initial_state)
                    break
                successors = state.get_successors()
                for successor in successors:
                    value_heuristic = h(successor, goal_state)
                    cost_a = cost_path + 1
                    cost = cost_a + value_heuristic
                    if successor.get_initial_state() not in explored and self.check_frontier(frontier, successor):
                        frontier = self.heap_push(
                            (cost, cost_a, action + [successor.get_action()], successor), frontier)
        actions = action
        actions.append("Stop")
        return actions, cost_all

    def heap_push(self, cost_and_successor, frontier):
        cost, cost_a, action, successor = cost_and_successor
        frontier.append((cost, cost_a, action, successor))
        frontier = super().sort_cost(frontier)
        return frontier

    def check_frontier(self, frontier, successor):
        for i in frontier:
            cost, cost_a, action, node = i
            if node.get_initial_state() == successor.get_initial_state():
                return False
        return True
