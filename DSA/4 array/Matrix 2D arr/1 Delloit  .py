
# ip 
#   matrix = [
#         [2, 4, 6],
#         [6, 8, 10],
#         [1, 12, 10]  ]

# op  6*2 + 10*2 => 32
    #   jo elm even baar aye usko uski freq se multiple kr ke summ dede bus 
# easy hai

# r1 
def f(matrix, n, m):
    mp = {}
    for i in range(n):  # Iterate over the rows
        for j in range(m):  # Iterate over the columns
            if matrix[i][j] not in mp:
                mp[matrix[i][j]] = 1
            else:
                mp[matrix[i][j]] += 1
    
    ans = 0  
    for key, value in mp.items(): 
        if value % 2 == 0:
            ans += value * key  

    return ans

# also rep as  concept 

#   ans = 0 
#     for x in mp : 
#         if mp[x] % 2 == 0 :
#             ans += mp[x] * x 
#     return ans 


if __name__ == "__main__":
    
    matrix = [ [2, 4, 6],[6, 8, 10],[6, 12, 10] ]

    n = len(matrix)
    m = len(matrix[0])

    ans = f(matrix, n, m)
    print(ans)



# r2 

def f(mat):
    n = len(mat) 
    m = len(mat[0])

    mp = {}
    for i in range(n):  # Iterate over the rows
        for j in range(m):  # Iterate over the columns
            if matrix[i][j] not in mp:
                mp[matrix[i][j]] = 1
            else:
                mp[matrix[i][j]] += 1
    
    ans = 0  
    for key, value in mp.items(): 
        if value % 2 == 0:
            ans += value * key  
            
    return ans

# also rep as  concept 

#   ans = 0 
#     for x in mp : 
#         if mp[x] % 2 == 0 :
#             ans += mp[x] * x 
#     return ans 


if __name__ == "__main__":
    
    matrix = [ [2, 4, 6],[6, 8, 10],[6, 12, 10] ]


    ans = f(matrix )
    print(ans)


