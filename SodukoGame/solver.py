class SudokuSolver:
    def find_next_empty(self, puzzle):
        for r in range(9):
            for c in range(9):
                if puzzle[r][c] == -1:
                    return r, c
        return None, None

    def is_valid(self, puzzle, guess, row, col):
        if guess in puzzle[row]:
            return False

        col_vals = [puzzle[i][col] for i in range(9)]
        if guess in col_vals:
            return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if puzzle[r][c] == guess:
                    return False

        return True

    def solve(self, puzzle):
        row, col = self.find_next_empty(puzzle)
        if row is None:
            return True

        for guess in range(1, 10):
            if self.is_valid(puzzle, guess, row, col):
                puzzle[row][col] = guess
                if self.solve(puzzle):
                    return True
                puzzle[row][col] = -1

        return False
