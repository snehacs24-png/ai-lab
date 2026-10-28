import random

# Calculate number of attacking queen pairs
def heuristic(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    n = len(state)

    for col in range(n):
        for row in range(n):
            if row != state[col]:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)

    return neighbors


# Display chessboard
def print_board(state):
    n = len(state)

    for row in range(n):
        for col in range(n):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# Hill Climbing algorithm
def hill_climbing():
    n = 4
    step = 1

    state = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        h = heuristic(state)

        print("=" * 40)
        print("Step:", step)
        print("Current State:", [x + 1 for x in state])
        print("Heuristic Formula: h(n) = Attacking Queen Pairs")
        print("h(n) =", h)
        print("\nCurrent Chessboard:")
        print_board(state)

        if h == 0:
            print("Goal reached! No queens attack each other.")
            return state

        neighbors = get_neighbors(state)

        # Find the neighbor with the lowest heuristic
        best_neighbor = min(neighbors, key=heuristic)
        best_h = heuristic(best_neighbor)

        print("Best Neighbor:", [x + 1 for x in best_neighbor])
        print("Heuristic of Best Neighbor:", best_h)
        print(
            f"Comparison: h(current) = {h}, "
            f"h(neighbor) = {best_h}"
        )

        if best_h >= h:
            print("Local optimum reached. Restarting...")
            state = [
                random.randint(0, n - 1)
                for _ in range(n)
            ]
            step = 1
        else:
            print("Better state found. Moving to neighbor.")
            state = best_neighbor
            step += 1


# Execute the algorithm
solution = hill_climbing()

print("\nFinal Solution:", [x + 1 for x in solution])
print("Final Heuristic h(n) =", heuristic(solution))
print("\nFinal Chessboard:")
print_board(solution)

