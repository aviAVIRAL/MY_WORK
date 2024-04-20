
# ip 
#   matrix = [
#         [2, 4, 6],
#         [6, 8, 10],
#         [1, 12, 10]  ]

# op  6*2 + 10*2 => 32
    #   jo elm even baar aye usko uski freq se multiple kr ke summ dede bus 
# easy hai


def f(mat):
    n = len(mat)
    m = len(mat[0])
    mp = {}
    for i in range(n):
        for j in range(m):
            if mat[i][j] not in mp:
                mp[mat[i][j]] = 1
            else:
                mp[mat[i][j]] += 1 

    cnt = 0
    for x,y in mp.items(): 
        if y%2 == 0:
            cnt += y*x 
    return cnt 
    # cnt = 0
    # for x in mp : 
    #     if mp[x]%2 == 0:
    #         cnt += mp[x]*x 
    # return cnt 

matrix = [
        [2, 4, 6],
        [6, 8, 10],
        [1, 12, 10]  ]
print( f(matrix) ) 


# mp = {10: 2, 6: 2, 8: 1}
# cnt = 0
# for x, y in mp.items():  # Iterate over key-value pairs using items()
#     if y % 2 == 0:
#         cnt += y * x
# print(cnt)  # Adjust this line if it's inside a function


print()

arr = [ 1, 2, 3, 4 ]
for x,y in enumerate(arr) : 
    print(x, y, end =  " ")


print()
print()
mp = {10: 2, 6: 2, 8: 1}
items = mp.items()
print(items)
for x, y in items: 
    print(x, y , end = " ")

# Output: dict_items([(10, 2), (6, 2), (8, 1)])
print(".......")
print()
mp = {10: 2, 6: 2, 8: 1}
dol  = [(x,y) for x, y in mp.items()]
print(dol)


print( )
print("...?.." )
arr =  [1,2,3, 4]
items =list( enumerate(arr)  ) 
print(items)
for x, y in items: 
    print(x, y , end = " ")

