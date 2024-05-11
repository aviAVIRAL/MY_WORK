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
    
    for x in mp: 
        if mp[x] % 2 == 0 :
            ans += x*mp[x] 
    # for key, value in mp.items(): 
    #     if value % 2 == 0:
    #         ans += value * key  
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
