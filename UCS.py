import heapq

N = 5  

def is_safe(state, row, col):
    for r, c in enumerate(state):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def successors(state):
    next_row = len(state)
    children = []

    for col in range(N):
        if is_safe(state, next_row, col):
            new_state = state + [col]
            children.append(new_state)

    return children


def ucs_5_queen():
    priority_queue = []
    heapq.heappush(priority_queue, (0, []))  

    while priority_queue:
        cost, state = heapq.heappop(priority_queue)

        
        if len(state) == N:
            return state

        
        for child in successors(state):
            heapq.heappush(priority_queue, (cost + 1, child))

    return None


def print_board(solution):
    for row in range(N):
        line = ""
        for col in range(N):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

solution = ucs_5_queen()

if solution:
    print("Solution found:")
    print(solution)
    print("\nBoard:")
    print_board(solution)
else:
    print("No solution found.")