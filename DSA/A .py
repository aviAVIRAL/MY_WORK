def f(matrix):
    n = len(matrix)
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = matrix[i][j]
    return temp

# if __name__ == "__main__":
#     mat = [[1, 2, 3], 
#            [4, 5, 6], 
#            [7, 8, 9]]
#     k = f(mat)   
#     for i in range(len(k)):
#         for j in range(len(k[0])):
#             print(k[i][j], end=" ")
#         print()

# print("......... ")


# k = [[9, 2, 3, 4 , 5 ], [4, 5, 6, 6 , 8 ], [7, 8, 9, 9 ,  9]]

# for i in range(len(k)):
#     for j in range(len(k)):
#         print(k[i][j], end=" ")
#     print()

# print()

k = [[9, 2, 3, 4, 5], [4, 5, 6, 6, 8], [7, 8, 9, 9, 9]]

for i in range(len(k)):
    for j in range(len(k[0])):
        print(k[i][j], end=" ")
    print()




