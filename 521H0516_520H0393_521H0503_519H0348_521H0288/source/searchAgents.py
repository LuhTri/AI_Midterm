import math
from fringes import Stack, Queue, PriorityQueue


def bfs(problem) -> list:
    actions = []
    frontier = Queue()
    frontier.enqueue((problem.initial_state, []))

    while len(problem.goal_state) > 0:
        explored = []
        while not frontier.is_empty():
            state, temp_actions = frontier.dequeue()
            if problem.is_goal(state):
                problem.goal_state.remove(state)
                if len(problem.goal_state) == 0:
                    break
                while not frontier.is_empty():
                    frontier.dequeue()
                frontier.enqueue((state, []))
                break
            explored.append(state)
            for successor, action_cost, move in problem.get_successors(state):
                if successor not in explored:
                    new_actions = temp_actions + [move]
                    frontier.enqueue((successor, new_actions))
        actions += temp_actions
    actions += ["Stop"]
    return actions


def dfs(problem) -> list:
    actions = []
    frontier = Stack()
    frontier.push((problem.initial_state, []))
    while len(problem.goal_state) > 0:
        explored = []
        while not frontier.is_empty():
            state, temp_actions = frontier.pop()
            if problem.is_goal(state):
                problem.goal_state.remove(state)
                if len(problem.goal_state) == 0:
                    break
                while not frontier.is_empty():
                    frontier.pop()
                frontier.push((state, []))
                break
            explored.append(state)
            for successor, action_cost, move in problem.get_successors(state):
                if successor not in explored:
                    new_actions = temp_actions + [move]
                    frontier.push((successor, new_actions))
        actions += temp_actions
    actions += ["Stop"]
    return actions


def ucs(problem) -> list:
    actions = []
    frontier = PriorityQueue()
    frontier.enqueue((problem.initial_state, [], 0), 0)
    while len(problem.goal_state) > 0:
        explored = []
        while not frontier.is_empty():
            state, temp_actions, cost_so_far = frontier.dequeue()
            if problem.is_goal(state):
                problem.goal_state.remove(state)
                if len(problem.goal_state) == 0:
                    break
                while not frontier.is_empty():
                    frontier.dequeue()
                frontier.enqueue((state, [], 0), 0)
                break
            explored.append(state)
            for successor, action_cost, move in problem.get_successors(state):
                new_actions = temp_actions + [move]
                new_cost = cost_so_far + action_cost
                if successor not in explored:
                    frontier.enqueue(
                        (successor, new_actions, new_cost), new_cost)
        actions += temp_actions
    actions += ["Stop"]
    return actions


def gbfs(problem, fn_heuristic) -> list:
    actions = []
    frontier = PriorityQueue()
    frontier.enqueue(
        (problem.initial_state, []),
        fn_heuristic(problem.initial_state, problem.goal_state)[0],
    )
    while len(problem.goal_state) > 0:
        explored = []
        while not frontier.is_empty():
            state, temp_actions = frontier.dequeue()
            if problem.is_goal(state):
                problem.goal_state.remove(state)
                if len(problem.goal_state) == 0:
                    break
                while not frontier.is_empty():
                    frontier.dequeue()
                frontier.enqueue(
                    (state, []), fn_heuristic(state, problem.goal_state)[0]
                )
                break
            explored.append(state)
            for successor, action_cost, move in problem.get_successors(state):
                new_actions = temp_actions + [move]
                if successor not in explored:
                    frontier.enqueue(
                        (successor, new_actions),
                        fn_heuristic(successor, problem.goal_state)[0],
                    )
        actions += temp_actions
    actions += ["Stop"]
    return actions


def astar(problem, fn_heuristic) -> list:
    actions = []
    frontier = PriorityQueue()
    frontier.enqueue((problem.initial_state, [], 0), 0)
    while len(problem.goal_state) > 0:
        temp_actions = []
        explored = []
        while not frontier.is_empty():
            state, temp_actions, cost_so_far = frontier.dequeue()
            if problem.is_goal(state):
                problem.goal_state.remove(state)
                if len(problem.goal_state) == 0:
                    break
                while not frontier.is_empty():
                    frontier.dequeue()
                frontier.enqueue((state, [],   0), 0)
                break
            explored.append(state)
            for successor, action_cost, move in problem.get_successors(state):
                new_actions = temp_actions + [move]
                new_cost = cost_so_far + action_cost
                if successor not in explored:
                    frontier.enqueue(
                        (successor, new_actions, new_cost),
                        new_cost +
                        fn_heuristic(successor, problem.goal_state)[0],
                    )
        actions += temp_actions
    actions += ["Stop"]
    return actions


def euclidean_dis(state, goal):
    heuristic = []
    food = goal[0]
    heuristic.append(
        math.sqrt((food[0] - state[0]) ** 2 + (food[1] - state[1]) ** 2))
    return heuristic


def manhattan_dis(state, goal):
    heuristic = []
    food = goal[0]
    heuristic.append(abs(food[0] - state[0]) + abs(food[1] - state[1]))
    return heuristic


def multi_heuristic(state, goal):
    heuristic_list = []
    for food in goal:
        temp = math.sqrt((food[0] - state[0]) ** 2 + (food[1] - state[1]) ** 2)
        heuristic_list.append(temp)
        heuristic_list.sort()
    return heuristic_list
