from Node import Node
from Search import SearchStrategy


class UCS(SearchStrategy):
    def search(self, node: Node, h: callable):
        actions = []
        frontier = [(0, node)]
        goal_state = node.get_food_location()
        goal_state_lowest = super().find_food_lowest_cost(goal_state, node)
        while goal_state:
            explored = []
            while frontier is not None:
                cost, state = frontier.pop(0)
                explored.append(state.get_initial_state())
                if state.get_initial_state() == goal_state_lowest[0][1]:
                    frontier = [(0, state)]
                    actions, path = super().find_action(state)
                    goal_state = super().check_food(
                        goal_state, goal_state_lowest[0][1], path)
                    goal_state_lowest = super().find_food_lowest_cost(goal_state, state)
                    break
                successors = state.get_successors()
                for successor in successors:
                    value_heuristic = h(
                        successor.get_initial_state(), goal_state_lowest[0][1])
                    cost += value_heuristic
                    if successor.get_initial_state() not in explored and super().check_frontier(frontier, successor):
                        frontier = super().heap_push((cost, successor), frontier)
        actions.append('Stop')
        return actions


class A_star(SearchStrategy):
    def search(self, node: Node, h: callable):
        actions = []
        frontier = [(0, 0, node)]
        goal_state = node.get_food_location()
        goal_state_lowest = super().find_food_lowest_cost(goal_state, node)
        while goal_state:
            explored = []
            while frontier is not None:
                cost, cost_path, state = frontier.pop(0)
                explored.append(state.get_initial_state())
                if state.get_initial_state() == goal_state_lowest[0][1]:
                    frontier = [(0, 0, state)]
                    actions, path = super().find_action(state)
                    goal_state = super().check_food(
                        goal_state, goal_state_lowest[0][1], path)
                    goal_state_lowest = super().find_food_lowest_cost(goal_state, state)
                    break
                successors = state.get_successors()
                for successor in successors:
                    value_heuristic = h(
                        successor.get_initial_state(), goal_state_lowest[0][1])
                    value_cost = super().find_cost(state.get_initial_state(),
                                                   successor.get_initial_state())
                    cost_a = cost_path + value_cost
                    cost = cost_a + value_heuristic
                    if successor.get_initial_state() not in explored and self.check_frontier(frontier, successor):
                        frontier = self.heap_push(
                            (cost, cost_a, successor), frontier)
        actions.append('Stop')
        return actions

    def heap_push(self, cost_and_successor, frontier):
        cost, cost_a, successor = cost_and_successor
        frontier.append((cost, cost_a, successor))
        frontier = super().sort_cost(frontier)
        return frontier

    def check_frontier(self, frontier, successor):
        for i in frontier:
            cost, cost_a, node = i
            if node.get_initial_state() == successor.get_initial_state():
                return False
        return True
