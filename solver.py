class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.empty_space = [0, 0]
        self.row = self.empty_space[0]
        self.col = self.empty_space[1]

    def find_empty_space(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.empty_space[0] = i
                    self.empty_space[1] = j
                    return True
        return False

    def row_check(self, row, num):
        for i in range(9):
            if num == self.grid[row][i]:
                return True
        return False

    def col_check(self, col, num):
        for i in range(9):
            if num == self.grid[i][col]:
                return True
        return False

    def grid_check(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if num == self.grid[row+i][col+j]:
                    return True
        return False

    def is_move_valid(self, row, col, num):
        return not SudokuSolver.row_check(self, row, num) and \
               not SudokuSolver.col_check(self, col, num) and \
               not SudokuSolver.grid_check(self, row - row % 3, col - col % 3, num)

    def solver(self):
        self.empty_space = [0, 0]

        if not(self.find_empty_space()):
            return True

        row = self.empty_space[0]
        col = self.empty_space[1]

        for num in range(1, 10):
            if self.is_move_valid(row, col, num):
                self.grid[row][col] = num

                if self.solver():
                    return True

                self.grid[row][col] = 0
        return False


if __name__ == "__main__":

    table = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    sudoku = SudokuSolver(table)

    if sudoku.solver():
        for rows in sudoku.grid:
            print(rows)