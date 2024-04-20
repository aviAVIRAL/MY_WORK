

# brute  Tc: O((N*M)*(N + M)) + O(N*M)  ~ n^3   and  sc = O(1)

def markRow(matrix, n, m, i):
    # set all non-zero elements as -1 in the row i:
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n, m, j):
    # set all non-zero elements as -1 in the col j:
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zeroMatrix(matrix, n, m):
    # Set -1 for rows and cols
    # that contains 0. Don't mark any 0 as -1:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    
    # Finally, mark all -1 as 0:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    n = len(matrix)
    m = len(matrix[0])
    k = zeroMatrix(matrix, n, m)
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end= " ")
        print()




    




	# for row in ans:
	#     for ele in row:
	#         print(ele, end=" ")
	#     print()
    
    
    
    
    
    
        # # see no error is coming print() but showing red underline 

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
