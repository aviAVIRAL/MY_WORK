def setZeroes(mat):
    rows = len(mat)
    cols = len(mat[0])
    first_col_zero = 1

    for i in range(rows):
        if mat[i][0] == 0:
            first_col_zero = 0
        for j in range(1, cols):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
        if first_col_zero == 0:
            mat[i][0] = 0

n, m = map(int, input().split())
assert 1 <= n <= 100
assert 1 <= m <= 100

mat = [list(map(int, input().split())) for _ in range(n)]

setZeroes(mat)

for row in mat:
    print(*row)


# 3 3
# 4 6 0
# 8 2 1
# 3 1 5