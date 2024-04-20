
# Rotate Image by 90 degree
# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

# Note: Rotate matrix 90 degrees anticlockwise

# Examples
# Example 1:

# Input: [[1,2,3],[4,5,6],[7,8,9]]

# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.

# Example 2:

# Input: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# Output:[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix


# .........   concept  temp [0] * n  in matrix   ........

# mat = [[1, 2, 3,4,5],
#        [1, 2, 3,4,5],
#        [1, 2, 3,4,5]]

# n = len(mat)
# m = len(mat[0])
    
# temp = [ [0] * m for _ in range(n) ]


# for i in range(len(temp)):
#     for j in range(len(temp[0])):
#         print(temp[i][j], end=" ")
#     print()

# # op 
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# .................               ............


# brute  tc n^2  sc n^2

def f(matrix):
    n = len(matrix)

    temp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = matrix[i][j]
    return temp


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = f(mat)   
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end=" ")
        print()
# als orep 
if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = f(mat)   
    for row in k : 
        for x in row : 
            print(x, end = " ")
        print()

print()
# optimal  tc same  but sc  1

def f(matrix):
    n = len(matrix)
                    #   col ki len no need  
# 1.transpose
    for i in range(n):
        for j in range( i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# 2 revrse each  row  :  not full matrix caerfull
    for i in range(n):
        matrix[i].reverse()
    
    return matrix 

if __name__ == "__main__":
    mat = [[1, 2, 3],
           [4, 5, 6], 
           [7, 8, 9]]
    k = f(mat)
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end= " ")
        print()


print("hfr ")



# .......................................
# # leedcode 
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         matrix.reverse()
#         for i in range(len(matrix)):
#             for j in range(i+1, len(matrix[i])):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# ........................................






