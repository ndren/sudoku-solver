EMPTY = 0
def get_missing_squares(unsolved_board):
    # Returns a list of the (y, x) coordinates of empty squares
    empty = []
    for y in range(9):
        for x in range(9):
            if unsolved_board[y][x] == EMPTY:
                empty.append((y,x))
    return empty
def has_error(board):
    # Returns whether the board has any error, in any row, column or square.
    return has_error_row(board) or has_error_column(board) or has_error_square(board)
def has_error_row(board):
    for row in board:
        # Board is not wrong until it has made a decision (not EMPTY)
        check = [i for i in row if i != EMPTY]
        # Verify the presence of any duplicate values
        if len(check) != len(set(check)):
            return True
    return False
def has_error_column(board):
    # Incredible zip magic. Get list of first items, list of second items, etc.
    for column in zip(*board):
        check = [i for i in column if i != EMPTY]
        if len(check) != len(set(check)):
            return True
    return False
def has_error_square(board):
    for large_square in range(9):
        # By symmetry, these calculations can be flipped for the same result.
        corner_y = large_square // 3 * 3
        corner_x = large_square % 3 * 3
        check = [board[i][j] for i in range(corner_y, corner_y + 3) for j in range(corner_x, corner_x + 3) if board[i][j] != EMPTY]
        if len(check) != len(set(check)):
            return True
    return False
def fill(board, path, missing_squares):
    # Fills the board with the given path.
    fill_count = 0
    for number in path:
        # The nth item in the path is stored at the nth missing square.
        y, x = missing_squares[fill_count]
        fill_count += 1
        board[y][x] = number
    for y, x in missing_squares[fill_count:]:
        # The path may be shorter than missing_squares.
        board[y][x] = EMPTY
    return fill_count
def find_all_solutions(board, timeout=lambda unix_time: False):
    from square import Square
    from copy import deepcopy
    from time import time
    start_time = time()
    solutions = []
    root = Square()
    missing_squares = get_missing_squares(board)
    number_to_fill = len(missing_squares)
    found_new_solution = False
    found_all_solutions = False
    while not (found_all_solutions or timeout(start_time)):
        leaf = root.get_leaf()
        number_filled = fill(board, root.get_path(), missing_squares)
        if has_error(board) or found_new_solution:
            if not leaf.increment():
                # This means that the root node has attempted to increment its (undefined) parent, so the graph has been fully searched. 
                found_all_solutions = True
            found_new_solution = False
        else:
            if number_filled == number_to_fill:
                solutions.append(deepcopy(board))
                found_new_solution = True
            else:
                leaf.set_child(Square(parent=leaf))
    return (solutions, timeout(start_time), time()-start_time)

if __name__ == "__main__":     
    sampleboard = [
        [5, 3, 0, 0, 7, 0, 9, 0, 2],
        [0, 0, 0, 1, 9, 5, 0, 4, 0],
        [0, 0, 8, 3, 0, 0, 5, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 8, 0, 3, 7, 0, 1],
        [7, 0, 3, 0, 2, 0, 0, 0, 6],
        [9, 0, 0, 0, 0, 7, 2, 0, 4],
        [0, 0, 7, 4, 1, 9, 0, 0, 5],
        [0, 0, 5, 0, 8, 0, 1, 0, 9]
    ]

    from pprint import pprint
    for solution in find_all_solutions(sampleboard)[0]:
        print("Found a solution!")
        pprint(solution)
    print("All solutions found!")