


# reverse arr in recursion 
def f(arr, i, j):
    
    if i>j : 
        return arr
    arr[i], arr[j] = arr[j], arr[i]
    return f(arr, i+1 , j-1 )

arr = [ 1,2, 3,4]
n = len(arr)
print(f(arr, 0 ,3))


print(",,,")


# reverse arr in recursion 
def f(arr, i, j):
    
    if i>j : 
        return 
    arr[i], arr[j] = arr[j], arr[i]
    f(arr, i+1 , j-1 )

arr = [ 1,2, 3]
n = len(arr)
# print(f(arr, 0 ,3)) op is none  reason niche hai 
f(arr, 0 ,n-1)
print(arr)  # op is correct 
# The error you're encountering arises because the 
# print function is trying to print the result 
# of f, but f doesn't return anything. Instead, 
# f modifies the list arr in place. To correct this, you should first call f to modify arr, and then print arr separately.




# reverse arr in recursion  
def f(arr, i, j):
    
    if i>j : 
        return arr
    arr[i], arr[j] = arr[j], arr[i]
    f(arr, i+1 , j-1 )

arr = [ 1,2, 3]
n = len(arr)
# print(f(arr, 0 ,3)) op is none  reason niche hai 
f(arr, 0 ,n-1)
print(arr)  # op is correct 
# The error you're encountering arises because the 
# print function is trying to print the result 
# of f, but f doesn't return anything. Instead, 
# f modifies the list arr in place. To correct this, you should first call f to modify arr, and then print arr separately.














