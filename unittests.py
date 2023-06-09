from backtrack import *
if __name__ == "__main__":
    # The function get_missing_squares correctly detects all missing squares
    # It returns the y coordinate first and no extra squares
    missing_square_board = [
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
    assert sorted(get_missing_squares(missing_square_board)) == [
        (0, 2), (0, 3), (0, 5), (0, 7),
        (1, 0), (1, 1), (1, 2), (1, 6), (1, 8),
        (2, 0), (2, 1), (2, 4), (2, 5), (2, 7), (2, 8),
        (3, 0), (3, 1), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
        (4, 0), (4, 1), (4, 2), (4, 4), (4, 7),
        (5, 1), (5, 3), (5, 5), (5, 6), (5, 7),
        (6, 1), (6, 2), (6, 3), (6, 4), (6, 7),
        (7, 0), (7, 1), (7, 6), (7, 7),
        (8, 0), (8, 1), (8, 3), (8, 5), (8, 7)
    ]
    
    # The function has_error_row detects the presence of row errors
    row_error_board = [
        [4, 6, 0, 0, 2, 0, 0, 0, 7],
        [0, 0, 0, 8, 0, 4, 0, 5, 0],
        [0, 4, 1, 6, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 1, 0, 6, 2, 0, 8],
        [2, 0, 6, 0, 7, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 2, 7, 0, 5],
        [0, 0, 2, 5, 8, 0, 0, 0, 4],
        [0, 0, 4, 0, 1, 0, 8, 0, 0]
    ]
    assert has_error_row(row_error_board)
    
    # The function has_error_column detects the presence of column errors
    column_error_board = [
        [0, 0, 5, 0, 2, 3, 0, 0, 9],
        [7, 6, 3, 3, 0, 5, 6, 0, 5],
        [8, 0, 0, 0, 4, 3, 0, 1, 0],
        [7, 0, 4, 0, 0, 7, 0, 9, 0],
        [9, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 1, 0, 9, 6],
        [0, 5, 0, 0, 0, 9, 0, 0, 2],
        [0, 8, 5, 0, 0, 2, 2, 0, 0],
        [6, 4, 0, 0, 0, 0, 5, 7, 7]
    ]
    assert has_error_column(column_error_board)
    
    # The function has_error_square detects the presence of square errors
    square_error_board = [
        [2, 9, 0, 3, 0, 3, 2, 5, 0],
        [0, 0, 0, 0, 6, 0, 7, 0, 4],
        [4, 4, 0, 2, 9, 0, 6, 0, 0],
        [6, 0, 0, 3, 0, 8, 0, 1, 6],
        [4, 0, 2, 0, 0, 8, 6, 0, 0],
        [0, 0, 1, 4, 6, 0, 7, 0, 7],
        [0, 0, 1, 3, 0, 0, 0, 0, 4],
        [9, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 1, 1, 8, 3, 0, 0, 7, 0]
    ]
    assert has_error_square(square_error_board)
    
    # The function has_error detects any type of error
    
    assert has_error(row_error_board)
    assert has_error(column_error_board)
    assert has_error(square_error_board)
    
    # A board with no type of error of does satisfy any function
    
    clean_board = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 0, 0, 1, 9, 0, 0, 4, 0],
        [0, 0, 8, 3, 0, 0, 5, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [9, 0, 0, 0, 0, 7, 2, 0, 4],
        [0, 0, 7, 0, 1, 9, 0, 0, 5],
        [0, 0, 5, 0, 8, 0, 1, 0, 0]
    ]
    
    assert not has_error_column(clean_board)
    assert not has_error_row(clean_board)
    assert not has_error_square(clean_board)
    assert not has_error(clean_board)
    
    # Composing get_missing_squares and fill modifies the board in-place correctly
    # Fill inserts the path into the empty squares in order
    board_to_fill = [
        [8, 7, 6, 5, 4, 3, 2, 1, 0],
        [0, 0, 0, 8, 2, 1, 0, 5, 0],
        [0, 0, 1, 6, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 1, 0, 6, 0, 0, 8],
        [2, 0, 0, 0, 7, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 2, 7, 0, 5],
        [0, 0, 2, 0, 8, 0, 0, 0, 4],
        [0, 0, 4, 0, 1, 0, 8, 0, 0]
    ]
    path = [9, 3, 4, 5, 9, 7, 2]

    assert fill(board_to_fill, path, get_missing_squares(board_to_fill)) == 7
    assert board_to_fill == [
         [8, 7, 6, 5, 4, 3, 2, 1, 9],
         [3, 4, 5, 8, 2, 1, 9, 5, 7],
         [2, 0, 1, 6, 0, 0, 4, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 0, 1, 0, 6, 0, 0, 8],
         [2, 0, 0, 0, 7, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 2, 7, 0, 5],
         [0, 0, 2, 0, 8, 0, 0, 0, 4],
         [0, 0, 4, 0, 1, 0, 8, 0, 0]
    ]
    
    # Fill overrides cells that are not empty if they are marked as missing squares
    source_board = [
        [8, 7, 6, 5, 4, 3, 2, 1, 0],
        [0, 0, 0, 8, 2, 1, 0, 5, 0],
        [0, 0, 1, 6, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 1, 0, 6, 0, 0, 8],
        [2, 0, 0, 0, 7, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 2, 7, 0, 5],
        [0, 0, 2, 0, 8, 0, 0, 0, 4],
        [0, 0, 4, 0, 1, 0, 8, 0, 0]
    ]
    board_previously_filled = [
        [8, 7, 6, 5, 4, 3, 2, 1, 9],
        [4, 1, 4, 8, 2, 1, 0, 5, 0],
        [0, 0, 1, 6, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 1, 0, 6, 0, 0, 8],
        [2, 0, 0, 0, 7, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 2, 7, 0, 5],
        [0, 0, 2, 0, 8, 0, 0, 0, 4],
        [0, 0, 4, 0, 1, 0, 8, 0, 0]
    ]
    
    path = [9, 4, 1, 5]
    assert fill(board_previously_filled, path, get_missing_squares(source_board)) == 4
    assert board_previously_filled == [
        [8, 7, 6, 5, 4, 3, 2, 1, 9],
        [4, 1, 5, 8, 2, 1, 0, 5, 0],
        [0, 0, 1, 6, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 1, 0, 6, 0, 0, 8],
        [2, 0, 0, 0, 7, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 2, 7, 0, 5],
        [0, 0, 2, 0, 8, 0, 0, 0, 4],
        [0, 0, 4, 0, 1, 0, 8, 0, 0]
    ]
    
    # The function find_all_solutions detects when there are no solutions
    # The function returns a tuple, and its timeout related behaviour depends on computer performance
    # Therefore, the first item from this tuple (the solutions) will be tested
    
    inconsistent_board = [
        [1, 2, 3, 4, 5, 6, 7, 8, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert find_all_solutions(inconsistent_board)[0] == []
    
    # The find_all_solutions function finds the correct solution, and no other solutions
    
    single_solution_board = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 0, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]
    assert find_all_solutions(single_solution_board)[0] == [
        [
            [4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 8, 2, 5, 7, 1, 4, 9, 3],
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6, 3, 4, 1, 8, 2, 5, 9]
        ]
    ]
    
    # The find_all_solutions finds all possible solutions, and no other solutions
    # The order in which solutions are given does not matter
    
    multiple_solution_board = [
        [9, 4, 0, 0, 0, 1, 8, 5, 2],
        [0, 2, 0, 3, 0, 0, 0, 7, 1],
        [0, 7, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 7, 0, 9, 0],
        [4, 0, 0, 9, 0, 3, 0, 0, 7],
        [0, 0, 1, 5, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 4, 2, 0],
        [0, 1, 0, 0, 0, 5, 0, 6, 0],
        [3, 6, 0, 7, 0, 0, 0, 8, 0]
    ]
    
    assert sorted(find_all_solutions(multiple_solution_board)[0]) == [
        [
            [9, 4, 3, 6, 7, 1, 8, 5, 2],
            [5, 2, 6, 3, 8, 4, 9, 7, 1],
            [1, 7, 8, 2, 5, 9, 3, 4, 6],
            [6, 3, 2, 4, 1, 7, 5, 9, 8],
            [4, 8, 5, 9, 6, 3, 2, 1, 7],
            [7, 9, 1, 5, 2, 8, 6, 3, 4],
            [8, 5, 7, 1, 9, 6, 4, 2, 3],
            [2, 1, 4, 8, 3, 5, 7, 6, 9],
            [3, 6, 9, 7, 4, 2, 1, 8, 5],
        ],
        [
            [9, 4, 3, 6, 7, 1, 8, 5, 2],
            [5, 2, 6, 3, 8, 4, 9, 7, 1],
            [1, 7, 8, 2, 5, 9, 3, 4, 6],
            [6, 3, 5, 4, 1, 7, 2, 9, 8],
            [4, 8, 2, 9, 6, 3, 5, 1, 7],
            [7, 9, 1, 5, 2, 8, 6, 3, 4],
            [8, 5, 7, 1, 9, 6, 4, 2, 3],
            [2, 1, 4, 8, 3, 5, 7, 6, 9],
            [3, 6, 9, 7, 4, 2, 1, 8, 5],
        ],
        [
            [9, 4, 3, 6, 7, 1, 8, 5, 2],
            [5, 2, 6, 3, 8, 4, 9, 7, 1],
            [1, 7, 8, 2, 5, 9, 6, 3, 4],
            [6, 3, 2, 4, 1, 7, 5, 9, 8],
            [4, 8, 5, 9, 6, 3, 2, 1, 7],
            [7, 9, 1, 5, 2, 8, 3, 4, 6],
            [8, 5, 7, 1, 9, 6, 4, 2, 3],
            [2, 1, 4, 8, 3, 5, 7, 6, 9],
            [3, 6, 9, 7, 4, 2, 1, 8, 5],
        ],
        [
            [9, 4, 3, 6, 7, 1, 8, 5, 2],
            [5, 2, 6, 3, 8, 4, 9, 7, 1],
            [1, 7, 8, 2, 5, 9, 6, 3, 4],
            [6, 3, 5, 4, 1, 7, 2, 9, 8],
            [4, 8, 2, 9, 6, 3, 5, 1, 7],
            [7, 9, 1, 5, 2, 8, 3, 4, 6],
            [8, 5, 7, 1, 9, 6, 4, 2, 3],
            [2, 1, 4, 8, 3, 5, 7, 6, 9],
            [3, 6, 9, 7, 4, 2, 1, 8, 5],
        ],
        [
            [9, 4, 3, 6, 7, 1, 8, 5, 2],
            [6, 2, 5, 3, 8, 4, 9, 7, 1],
            [1, 7, 8, 2, 5, 9, 3, 4, 6],
            [5, 3, 6, 4, 1, 7, 2, 9, 8],
            [4, 8, 2, 9, 6, 3, 5, 1, 7],
            [7, 9, 1, 5, 2, 8, 6, 3, 4],
            [8, 5, 7, 1, 9, 6, 4, 2, 3],
            [2, 1, 4, 8, 3, 5, 7, 6, 9],
            [3, 6, 9, 7, 4, 2, 1, 8, 5],
        ],
        [
            [9, 4, 3, 6, 7, 1, 8, 5, 2],
            [6, 2, 5, 3, 8, 4, 9, 7, 1],
            [1, 7, 8, 2, 5, 9, 6, 3, 4],
            [5, 3, 6, 4, 1, 7, 2, 9, 8],
            [4, 8, 2, 9, 6, 3, 5, 1, 7],
            [7, 9, 1, 5, 2, 8, 3, 4, 6],
            [8, 5, 7, 1, 9, 6, 4, 2, 3],
            [2, 1, 4, 8, 3, 5, 7, 6, 9],
            [3, 6, 9, 7, 4, 2, 1, 8, 5],
        ],
    ]
