def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 21)

def is_valid(num, row, col, board):
    for c in range(9):
        if board[row][c] == num:
            return False
    for r in range(9):
        if board[r][col] == num:
            return False
    box_left = (col // 3) * 3
    box_top = (row // 3) * 3
    for r in range(box_top, box_top + 3):
        for c in range(box_left, box_left + 3):
            if board[r][c] == num:
                return False
    return True

def solve(board):
    empty_spots = find_empty_spots(board)
    if not empty_spots:
        return True  # Puzzle solved
    row, col = empty_spots[0]  # Try the first empty spot
    for i in range(1, 10):
        if is_valid(i, row, col, board):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack
    return False  # Dead end

def find_empty_spots(board):
    empty_spots = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty_spots.append((i, j))
    return empty_spots

def main():
    # Example Sudoku board
    hard_board = [
        [0, 6, 0, 0, 1, 0, 8, 7, 0],
        [0, 9, 0, 0, 8, 0, 6, 0, 0],
        [0, 0, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 0, 9, 6, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 2],
        [0, 7, 9, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 8, 0],
        [8, 0, 0, 0, 0, 0, 0, 5, 1],
    ]

    print("Original Sudoku board:")
    print_board(hard_board)
    print()

    if solve(hard_board):
        print("Solution found:")
        print_board(hard_board)
    else:
        print("Unsolvable puzzle.")


if __name__ == "__main__":
    main()
