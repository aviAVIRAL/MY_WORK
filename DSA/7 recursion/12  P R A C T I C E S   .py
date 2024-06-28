class Solution:
    def CHECK__(self, row, col, board, n):
        # Check upper diagonal on left side
        duprow, dupcol = row, col
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        # Check left side
        row, col = duprow, dupcol
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        # Check lower diagonal on left side
        row, col = duprow, dupcol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        return True

    def f(self, col, board, ans, n):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if self.CHECK__(row, col, board, n):
                board[row][col] = 'Q'
                self.f(col + 1, board, ans, n)
                board[row][col] = '.'
# ....................................................
    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.f(0, board, ans, n)
        return ans

# Example usage
if __name__ == "__main__":
    n = 4  # We are taking 4*4 grid and 4 queens
    obj = Solution()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print(f"Arrangement {i + 1}")
        for row in ans[i]:
            print(row)
        print()
