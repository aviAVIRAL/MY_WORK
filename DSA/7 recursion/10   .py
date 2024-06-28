class Solution:
    def isSafe1(self, row, col, board, n):
        # check upper element
        duprow = row
        dupcol = col

        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        return True

    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(list(board))
            return

        for row in range(n):
            if self.isSafe1(row, col, board, n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solve(col+1, board, ans, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def solveNQueens(self, n):
        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans

n = 4
obj = Solution()
ans = obj.solveNQueens(n)
for i in range(len(ans)):
    print(f"Arrangement {i+1}")
    for j in range(len(ans[0])):
        print(ans[i][j])
    print()



print()
print("chek.......................")
print()
class Solution:
    def isSafe(self, row, col, board, n):
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

    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(["".join(row) for row in board]) 
            # ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col] = 'Q'
                self.solve(col + 1, board, ans, n)
                board[row][col] = '.'

    def solveNQueens(self, n):
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans

# Example usage
if __name__ == "__main__":
    n = 4  # we are taking 4*4 grid and 4 queens
    obj = Solution()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print(f"Arrangement {i + 1}")
        for row in ans[i]:
            print(row)
        print()
