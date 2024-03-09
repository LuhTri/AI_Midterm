from Node import Node
from Search import SearchStrategy
from copy import deepcopy
import time


class UCS(SearchStrategy):
    def search(self, node: Node):
        actions = []
        frontier = [(0, [], node)]
        goal_state = node.get_food_location()

        while goal_state:
            explored = []

            while frontier is not None:
                # print(frontier)
                cost, action, state = frontier.pop(0)
                explored.append(state.get_initial_state())
                if super().is_goal(goal_state, state):
                    goal_state = super().remove(goal_state, state.get_initial_state())
                    if len(goal_state) == 0:
                        break
                    frontier = [(0, [], state)]
                    break
                successors = state.get_successors()

                for successor in successors:
                    if successor.get_initial_state() not in explored and super().check_frontier(frontier, successor):
                        cost += 1
                        newAction = action + [successor.get_action()]
                        frontier = self.heap_push(
                            (cost, newAction, successor), frontier)
            actions += action
        return actions


class A_star(SearchStrategy):
    def search_1(self, node: Node, goal, h: callable):
        actions = []
        frontier = [(0, 0, node)]
        goal_state = goal
        explored = []
        while len(frontier) != 0:
            cost, cost_path, state = frontier.pop(0)
            explored.append(state.initial_state)
            if state.initial_state == goal_state:
                actions = super().find_action(state)[0]
                break
            successors = state.get_successors()
            for successor in successors:
                value_heuristic = h(
                    successor.get_initial_state(), goal_state)
                value_cost = super().find_cost(state.initial_state,
                                               successor.get_initial_state())
                cost_a = cost_path + value_cost
                cost = cost_a + value_heuristic
                if successor.get_initial_state() not in explored and super().check_frontier(frontier, successor):
                    frontier = self.heap_push(
                        (cost, cost_a, successor), frontier)
        return actions

    def search(self, node: Node, h: callable):
        actions = []
        goal_state = node.get_food_location()
        node_temp = deepcopy(node)
        dic = []
        while goal_state:
            for i in goal_state:
                a = self.search_1(node_temp, i, h)
                dic.append((len(a), a, i))
            dic = super().sort_cost(dic)
            _, action, state = dic.pop(0)
            actions += action
            x, y = node_temp.get_initial_state()
            node_temp.maze[x][y] = ' '
            node_temp.maze[state[0]][state[1]] = 'P'
            node_temp.initial_state = node_temp.get_initial_state()
            goal_state = super().remove(goal_state, state)
            node_temp = deepcopy(node_temp)
            dic = []
        return actions
