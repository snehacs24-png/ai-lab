from copy import deepcopy


GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


MOVES = [
    (-1, 0, "Up"),
    (1, 0, "Down"),
    (0, -1, "Left"),
    (0, 1, "Right")
]


def find_empty(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j


def is_goal(grid):
    return grid == GOAL


def print_grid(grid):
    for row in grid:
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


# -----------------------------------
# DEPTH LIMITED SEARCH
# -----------------------------------

def depth_limited_search(grid, depth, path, visited):

    # Goal check
    if is_goal(grid):
        return path

    # Depth limit reached
    if depth == 0:
        return None

    # Find blank position
    x, y = find_empty(grid)

    # Try all possible moves
    for dx, dy, move in MOVES:

        nx = x + dx
        ny = y + dy

        # Check valid position
        if 0 <= nx < 3 and 0 <= ny < 3:

            # Create new grid
            new_grid = deepcopy(grid)

            # Move blank
            new_grid[x][y], new_grid[nx][ny] = (
                new_grid[nx][ny],
                new_grid[x][y]
            )

            # Convert grid to tuple for visited checking
            state = tuple(tuple(row) for row in new_grid)

            # Backtracking
            if state not in visited:

                visited.add(state)

                result = depth_limited_search(
                    new_grid,
                    depth - 1,
                    path + [(move, new_grid)],
                    visited
                )

                # Solution found
                if result is not None:
                    return result

                # BACKTRACK
                visited.remove(state)

    return None


# -----------------------------------
# IDDFS
# -----------------------------------

def iddfs(start_grid, max_depth=30):

    for depth in range(max_depth + 1):

        print("Searching at depth:", depth)

        start_state = tuple(
            tuple(row) for row in start_grid
        )

        visited = {start_state}

        result = depth_limited_search(
            start_grid,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

    return None


# -----------------------------------
# USER INPUT
# -----------------------------------

print("8 PUZZLE USING IDDFS + BACKTRACKING")
print()
print("Enter 9 numbers.")
print("Use 0 for the blank space.")
print()
print("Example:")
print("1 2 3")
print("4 0 6")
print("7 5 8")
print()

numbers = list(
    map(int, input("Enter puzzle: ").split())
)


# -----------------------------------
# INPUT VALIDATION
# -----------------------------------

if len(numbers) != 9:
    print("Error: Enter exactly 9 numbers.")
    exit()


if set(numbers) != set(range(9)):
    print("Error: Enter numbers 0 to 8 exactly once.")
    exit()


# Convert input into 3 x 3 grid
start = [
    numbers[0:3],
    numbers[3:6],
    numbers[6:9]
]


# -----------------------------------
# DISPLAY INITIAL STATE
# -----------------------------------

print("\nINITIAL STATE:")
print_grid(start)


print("GOAL STATE:")
print_grid(GOAL)


# -----------------------------------
# SOLVE
# -----------------------------------

solution = iddfs(start)


# -----------------------------------
# DISPLAY SOLUTION
# -----------------------------------

if solution is not None:

    print("========== SOLUTION ==========")

    print("Number of moves:", len(solution))

    # For this output, solution nodes = solution moves
    print("Number of nodes traversed:", len(solution))

    print()

    print("INITIAL STATE:")
    print_grid(start)

    for step, (move, grid) in enumerate(
        solution,
        start=1
    ):

        print("Step", step, "-", move)
        print_grid(grid)

    print("FINAL GOAL STATE:")
    print_grid(GOAL)

else:

    print("No solution found within the depth limit.")


