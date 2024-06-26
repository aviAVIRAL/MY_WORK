
# # Set Matrix Zero
# # Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

# # Examples
# # Examples 1:

# # Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

# # Output: [[1,0,1],[0,0,0],[1,0,1]]

# # Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
# # Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# # Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# # Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0



# # brute  Tc: O((N*M)*(N + M)) + O(N*M)  ~ n^3   and  sc = O(1)

# def markRow(matrix, n, m, i):
#     # set all non-zero elements as -1 in the row i:
#     for j in range(m):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1

# def markCol(matrix, n, m, j):
#     # set all non-zero elements as -1 in the col j:
#     for i in range(n):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1

# def zeroMatrix(matrix, n, m):
#     # Set -1 for rows and cols
#     # that contains 0. Don't mark any 0 as -1:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 markRow(matrix, n, m, i)
#                 markCol(matrix, n, m, j)
    
#     # Finally, mark all -1 as 0:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = 0
    
#     return matrix


# if __name__ == "__main__":
# 	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 	n = len(matrix)
# 	m = len(matrix[0])
# 	ans = zeroMatrix(matrix, n, m)
# 	print("The Final matrix is:")
# 	for row in ans:
# 	    for ele in row:
# 	        print(ele, end=" ")
# 	    print()  
# # see no error is coming print() but showing red underline 

# # o/p rep
# # The Final matrix is:
# # 1 0 1
# # 0 0 0
# # 1 0 1

# also   
# if __name__ == "__main__":
#     matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
#     n = len(matrix)
#     m = len(matrix[0])
#     k = zeroMatrix(matrix, n, m)
#     for i in range(len(k)):
#         for j in range(len(k[0])):
#             print(k[i][j], end= " ")
#         print()
# # o/p rep
# # The Final matrix is:
# # 1 0 1
# # 0 0 0
# # 1 0 1

# # also rep main function

# if __name__ == "__main__":
# 	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 	n = len(matrix)
# 	m = len(matrix[0])
# 	ans = zeroMatrix(matrix, n, m)

# 	print(ans)

# # o/p  rep
#     # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# # ................................................

# #  better  Tc: O( 2* ( N*M ) )  Sc: O(N) + O(M) hashing track


# def zeroMatrix(matrix, n, m):
#     row = [0] * n  #  keep track
#     col = [0] * m  

#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 row[i] = 1
#                 col[j] = 1

#     for i in range(n):
#         for j in range(m):
#             if row[i] or col[j]: # if row[i] == 1 or col[j] == 1: also represent as 
#                 matrix[i][j] = 0  

#     return matrix

# if __name__ == "__main__":
# 	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 	n = len(matrix)    # n is for row  and  m -> col
# 	m = len(matrix[0])
# 	ans = zeroMatrix(matrix, n, m)

# 	print("The Final matrix is:")

# 	for row in ans:
# 	    for ele in row:
# 	        print(ele, end=" ")
# 	    print()

# ..................
# # optimal i hold abhi bus sc ko i kiya hai tc is same as better 

# Complexity Analysis
# Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
# Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

# Space Complexity: O(1) as we are not using any extra space.

# def zeroMatrix(matrix, n, m):
#     # int row[n] = {0}; --> matrix[..][0]
#     # int col[m] = {0}; --> matrix[0][..]

#     col0 = 1
#     # step 1: Traverse the matrix and
#     # mark 1st row & col accordingly:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 # mark i-th row:
#                 matrix[i][0] = 0

#                 # mark j-th column:
#                 if j != 0:
#                     matrix[0][j] = 0
#                 else:
#                     col0 = 0

#     # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
#     for i in range(1, n):
#         for j in range(1, m):
#             if matrix[i][j] != 0:
#                 # check for col & row:
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0

#     #step 3: Finally mark the 1st col & then 1st row:
#     if matrix[0][0] == 0:
#         for j in range(m):
#             matrix[0][j] = 0
#     if col0 == 0:
#         for i in range(n):
#             matrix[i][0] = 0

#     return matrix


# if __name__ == "__main__":
	# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	# n = len(matrix)
	# m = len(matrix[0])
	# ans = zeroMatrix(matrix, n, m)

	# print("The Final matrix is:")
	# for row in ans:
	#     for ele in row:
	#         print(ele, end=" ")
	#     print()


# .................
# CP 


def f(n,m, mat):
    row = [0] * n  #  keep track
    col = [0] * m  
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]: # if row[i] == 1 or col[j] == 1: also represent as 
                mat[i][j] = 0  
    return mat

    
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

k = f(n,m , mat)

for x in k:     
    print(*x)  

# op representation 
# 3 4 5
# 2 4 6
# 4 6 7












        