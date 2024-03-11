from Node import Node
from Search import SearchStrategy


class UCS(SearchStrategy):

    def search(self, node: Node):
        actions = []
        frontier = [(0, [], node)]
        goal_state = node.get_food_location()
        ex = 0

        while len(goal_state) > 0:
            explored = []

            while len(frontier) != 0:
                cost, action, state = frontier.pop(0)
                if super().is_goal(goal_state, state):
                    goal_state = super().remove(goal_state, state.get_initial_state())
                    ex += len(explored)
                    frontier = [(0, [], state)]
                    break

                explored.append(state.get_initial_state())
                successors = state.get_successors()
                for successor in successors:
                    if successor.get_initial_state() not in explored:
                        newCost = cost + 1
                        newAction = action + [successor.get_action()]
                        frontier = super().heap_push(
                            (newCost, newAction, successor), frontier)

            actions += action
        actions.append("Stop")
        return actions, ex


class A_star(SearchStrategy):
    def search(self, node: Node, h: callable):
        actions = []
        goal_state = node.get_food_location()
        frontier = [(0, 0, node)]

        while goal_state:
            explored = []

            while frontier is not None:
                cost, cost_path, state = frontier.pop(0)
                explored.append(state.get_initial_state())
                if super().is_goal(goal_state, state):
                    frontier = [(0, 0, state)]
                    actions, path = super().find_action(state)
                    goal_state = super().check_food(goal_state, state.initial_state, path)
                    break

                successors = state.get_successors()

                for successor in successors:
                    value_heuristic = h(
                        successor.get_initial_state(), goal_state)
                    cost_a = cost_path + 1
                    cost = cost_a + value_heuristic

                    if successor.get_initial_state() not in explored and super().check_frontier(frontier, successor):
                        frontier = super().heap_push((cost, cost_a, successor), frontier)

        actions.append('Stop')
        return actions
