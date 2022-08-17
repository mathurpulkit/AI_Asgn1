#implements the iterative deepening search algorithm on the n-tile puzzle
#duplicates are not handled
import ntile

initial_depth = 1
max_depth = 20

def search(initial_state: ntile, depth: int):
    if depth == 0:
        if initial_state.is_solved():
            return []
        else:
            return None
    for move in ['U', 'D', 'L', 'R']:
        new_state = initial_state.newBoardMove(move)
        result = search(new_state, depth-1)
        if result is not None:
            return [move] + result # we return this, as list of moves is traced in reverse order
    return None

def ids(initial_state: ntile):
    for depth in range(initial_depth, max_depth+1):
        result = search(initial_state, depth)
        if result is not None:
            return result
    return None