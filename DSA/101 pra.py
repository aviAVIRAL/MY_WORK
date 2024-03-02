def f(matrix):
    n = len(matrix)
    
    ans = [[0] * n for _ in range(n)]  # Initialize ans with zeros of size n*n
    
    for i in range(n):
        for j in range(n):
            ans[j][n - i - 1] = matrix[i][j]
    return ans

if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = f(mat)   
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end=" ")
        print()