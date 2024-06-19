
# ..........

# reverse arr in recursion 

def f(arr, i, j):
    
    if i>j : 
        return arr
    arr[i], arr[j] = arr[j], arr[i]
    return f(arr, i+1 , j-1 )

arr = [ 1,2, 3,4]
n = len(arr)
print(f(arr, 0 ,3))
# ......


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


# ..........

# reverse arr  without recursion 
# i/p = arr = [ 1, 2, 3, 4 ]
# 0/p = arr =  [4, 3, 2, 1]

# m- 1 
# rep - 1
# simple methoud with logic 

def reverse_func(arr):
    n = len( arr)
    i = 0
    j = n - 1 
    
    while i <= j:   # or  i <= n//2
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1    
        
    return arr  

if __name__=="__main__":

    arr = [ 1, 2, 3, 4 ]
    reverse_func(arr)
    print( arr )


# or

# if __name__=="__main__":
 
#     arr = [ 1, 2, 3, 4, 5 ]
#     Result = reverse_func(arr)
#     print( Result )


# or 

# if __name__=="__main__":

#     arr = [ 1, 2, 3, 4 ]
#     print(reverse_func(arr))

# ..............

# m-1 
# rep - 2
# simple methoud { No use of recursion}

def f (arr):

    n = len(arr)
    
    for i in range(n//2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr 

if __name__=="__main__":
    arr=[11,12,13,14]
    print(f(arr))


# .....................................

# m-2 
# python build in function

    arr = [1, 2, 3, 4, 5, 6, 7]

    arr.reverse()

    print(arr)


# m 3 rep2 

arr = [1, 2, 3, 4, 5, 6]

arr[:] = arr[::-1]    # update to original arr 
 
print(arr)

# m-3

arr = [1, 2, 3, 4, 5, 6, 7]

reversed_arr = arr[::-1]

print(reversed_arr)
