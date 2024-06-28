#  [[1,2,],[22,3],[2]]  list of list hai and set mein
#  list nhi enter kr thi but tuple enter kr jate hai 

# ..........

# brute  using set data strture 
res = set()
def f(arr, brr , i , k):
    if i  == len(arr):
        if k == 0:      
            res.add(tuple(brr))
        return
    
    if arr[i] <= k :
        brr.append(arr[i])
        f(arr, brr ,i+1, k - arr[i])
        brr.pop()
    f(arr, brr , i+1, k)

arr = [1,1,1,2 ,2]
f(arr, [], 0, 4 )
print(res)

# ...........

# trick to convert tuple in to list  

# for x in res : 
#     print(list(x), end = " ")

# .............

print()
# also represent as

res = []
def f(arr, brr , i , k):
    if i  == len(arr):
        if k == 0:      
            res.append(brr[:])
        return
    
    if arr[i] <= k :
        brr.append(arr[i])
        f(arr, brr ,i+1, k - arr[i])
        brr.pop()
    f(arr, brr , i+1, k)

arr = [1,1,1,2 ,2]
f(arr, [], 0, 4 )
sol = set(tuple(x)  for x in res) #  impo 
print(sol)

print()
print()

# optimal

def f(i, k, ds):
    if k == 0:
        print(ds)
        return
    for j in range(i, len(arr)):
        if j > i and arr[j] == arr[j - 1]:
            continue
        if arr[j] > k:
            break
        ds.append(arr[j])
        f(j + 1, k - arr[j], ds)
        ds.pop()

arr= [1,1,1,2,2]
f(0, 4, [])

# ..........................
# leet code repre  
def combinationSum2(arr, k):
    res = []
    arr.sort()
    def f(i, k, ds):
        if k == 0:
            res.append(ds[:])
            return
        for j in range(i, len(arr)):
            if j > i and arr[j] == arr[j - 1]:
                continue
            if arr[j] > k:
                break
            ds.append(arr[j])
            f(j + 1, k - arr[j], ds)
            ds.pop()
    f(0, k, [])
    return res
if __name__ == "__main__":
    v = [1,1,1,2,2]
    comb = combinationSum2(v, 4)
    print(*comb)



# ... .. .... . .  ... .. ... .. ... .. ... . ...
# leet code reprer + striver 


# def combinationSum2(arr: List[int], k: int) -> List[List[int]]:
#     ans = []
#     ds = [] # see 
#     arr.sort()


#     def f(ind: int, k: int):
#         if k == 0:
#             ans.append(ds[:])
#             return
#         for i in range(ind, len(arr)): # i m p 
#             if i > ind and arr[i] == arr[i - 1]:
#                 continue
#             if arr[i] > k:
#                 break
#             ds.append(arr[i])
#             f(i + 1, k - arr[i])
#             ds.pop()


#     f(0, k)
#     return ans

# if __name__ == "__main__":
#     v = [10, 1, 2, 7, 6, 1, 5]
#     comb = combinationSum2(v, 8)
#     print(*comb)
# Output:

# [ [ 1 1 6 ][ 1 2 5 ][ 1 7 ][ 2 6 ] ]


# ......................






















