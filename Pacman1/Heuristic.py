class Heuristic:
    def euclideanDistance(state, goalsState) -> float:
        Px, Py = state
        Fx, Fy = goalsState

        return (((Px  - Fx )** 2 + (Py  - Fy ) ** 2) ** (1/2))
    
    def manhattanDistance(state, goalsState):
        Px, Py = state
        Fx, Fy = goalsState

        return abs(Px - Fx) + abs(Py - Fy)