GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)



def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()



def is_solvable(state):

    numbers = [x for x in state if x != 0]

    inversions = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1

    return inversions % 2 == 0



def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = []

    if row > 0:
        moves.append(blank - 3)      

    if row < 2:
        moves.append(blank + 3) 

    if col > 0:
        moves.append(blank - 1)    

    if col < 2:
        moves.append(blank + 1)     

    for new_blank in moves:

        new_state = list(state)

        new_state[blank], new_state[new_blank] = \
            new_state[new_blank], new_state[blank]

        neighbors.append(tuple(new_state))

    return neighbors



def dls(state, depth, path, visited):

  
    if state == GOAL:
        return True


    if depth == 0:
        return False

    visited.add(state)

    for next_state in get_neighbors(state):

        
        if next_state not in visited:

         
            path.append(next_state)

          
            if dls(next_state,
                   depth - 1,
                   path,
                   visited):

                return True

           
            path.pop()

    visited.remove(state)

    return False



def iddfs(start, max_depth=30):

    for depth in range(max_depth + 1):

        path = [start]

        visited = set()

        if dls(start, depth, path, visited):
            return path

    return None



print("8 PUZZLE USING IDDFS + BACKTRACKING")
print("Enter numbers 0 to 8.")
print("Use 0 for the blank space.\n")

numbers = list(map(int, input("Enter puzzle: ").split()))



if len(numbers) != 9:
    print("Error: Enter exactly 9 numbers.")
    exit()


if set(numbers) != set(range(9)):
    print("Error: Enter each number from 0 to 8 exactly once.")
    exit()


start = tuple(numbers)


print("\nInitial State:")
print_puzzle(start)


print("Goal State:")
print_puzzle(GOAL)



if not is_solvable(start):

    print("This puzzle is NOT solvable.")
    exit()


print("Puzzle is solvable.")
print("Searching...\n")



solution = iddfs(start)



if solution is not None:

    print("========== SOLUTION ==========")

    for i, state in enumerate(solution):

        print("Step", i)
        print_puzzle(state)

    print("Total moves:", len(solution) - 1)

else:

    print("No solution found within the depth limit.")





