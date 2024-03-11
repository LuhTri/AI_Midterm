class Heuristic:
    def euclideanDistance(state, goalState) -> float:
        Px, Py = state
        Fx, Fy = goalState

        return ((Px - Fx) ** 2 + (Py - Fy) ** 2) ** (1/2)

    def manhattanDistance(state, goalState) -> int:
        Px, Py = state
        Fx, Fy = goalState

        return abs(Px - Fx) + abs(Py - Fy)

    def h(state, goalState):
        if state in goalState:
            return len(goalState) - 1
        return len(goalState)
