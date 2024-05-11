

# ..........concept.................

# how to sort the sub arr{matrix}.   
# by using parameter of ech subarr ki lenght 
arr = [[1, 9], [10], [4, 5, 1], [1,2,6,6,7,8]]
arr.sort(key=len)
print(arr)
# opp [[10], [1, 9], [4, 5, 1], [1, 2, 6, 6, 7, 8]]

# ............................

# concept impo 
# when matrxi is not rectanular or squar shape 

k = [[1, 2, 3], 
     [4, 5, 6, 7, 8], 
     [9, 10]]

n = len(k)
# m = len(k[0])       replac with len(k[i]) colm length 
for i in range(n):
    m = len(k[i])  # 
    for j in range(m):
        print(k[i][j], end= " ")
    print()


# # op  
# 1 2 3
# 4 5 6 7 8
# 9 10
# ......................

# ye work in all case in all type matrix 

k = [[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]

n = len(k)
# m = len(k[0])
for i in range(n):
    m = len(k[i])  # 
    for j in range(m):
        print(k[i][j], end= " ")
    print()

# # op  

# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7

# ...........................

# ye only for for square and rectangle matrix 

x =    [[1, 2, 3, 22, 22], 
        [4, 5, 6, 11, 11], 
        [7, 8, 19, 10, 11]]

n = len(x)
m = len(x[0])
for i in range(n):
    for j in range(m):
        print(x[i][j], end = " ")
    print()



