
def print_grid(grid):
    for row in grid:
        print(*row)


def is_valid(grid, row, col, num):
    for j in range(9):
        if grid[row][j] == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        if solve(grid):
                            return True

                        grid[row][col] = 0

                return False

    return True


grid = []

print("Enter the Sudoku grid (use 0 for empty cells):")

for i in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

if solve(grid):
    print("Solved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists.")
