# 1.  simliar to previous quetion concept check by urSELf


# 2.  brute forces  tc = 0(n)   sc = 0(n)
 
def Left_rotate_by_k_place(arr, n, k):
    
    k = k % n  # Calculate k modulo n to handle cases where k is greater than n
    temp = []

    for i in range(0, k):
        temp.append(arr[i])

    # for i in range(k, n):             
        # arr[i - k] = arr[i]
    j = 0
    for i in range(k, n):
        arr[j] = arr[i]
        j += 1    
    

    # for i in range(n - k, n):
        # arr[i] = temp[i - (n-k)] 
    j = 0
    for i in range(n - k, n):
        arr[i] = temp[j]
        j += 1    
       

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
ans = Left_rotate_by_k_place(arr, n, k)
print(ans)


# 2.  brute forces  tc = 0(n)   sc = 0(n)
 
def Left_rotate_by_k_place(arr, n, k):
    k = k % n  # Calculate k modulo n to handle cases where k is greater than n
    temp = []

    for i in range(0, k):
        temp.append(arr[i])

    for i in range(k, n):
        arr[i - k] = arr[i]

    j = 0
    for i in range(n - k, n):
        arr[i] = temp[j]
        j += 1  # Increment j to get the next element from temp

    return arr
arr = [   1, 2, 3,      4, 5, 6, 7]
print("input ", arr)
n = 7
k = 3  # output [4, 5, 6, 7,      1, 2, 3   ]
ans = Left_rotate_by_k_place(arr, n, k)
print("output", ans)


# 1.  simliar to previous quetion concept check by urSELf

# 2.  brute forces  tc = 0(n)   sc = 0(n)
 
def Left_rotate_by_k_place(arr, n, k):
    k = k % n  # Calculate k modulo n to handle cases where k is greater than n
    temp = []

    for i in range(0, k):
        temp.append(arr[i])

    for i in range(k, n):             
        arr[i - k] = arr[i]
    #   j = 0
    #   for i in range(k, n):
    #      arr[j] = arr[i]
    #      j += 1    :- ye be use kr sakte hai
    

    for i in range(n - k, n):
        arr[i] = temp[i - (n-k)] 
    #  j = 0
    # for i in range(n - k, n):
    #     arr[i] = temp[j]
    #     j += 1    :- ye be use kr sakte hai
       

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
ans = Left_rotate_by_k_place(arr, n, k)
print(ans)


# Slicing methoud ka use kr ke 

# Tc= O(n)  sc = O(n) *

def right_rotate_by_k_places(arr,n,k):

    k = k % n
    arr[::] = arr[k:] + arr[:k]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
ans = right_rotate_by_k_places(arr, n, k)
print(ans)




# ......................................

# drey run kr ke appna dimangn laga kr ke 
# aapna mid laga ke kiya 

# aapna mid laga ke kiya 
# by using dry run pen ppr ka use kr ke 
# tc =o(n) sc = o(n) due to r 

def rotate(arr,n,k):
    r = arr[::-1]  #  sc = o(n) another list " r " is use 
    j = n-k-1
    for i in range (0,  n-k -2):
        r[i ], r[ j ] = r[j] , r[i]
        j-=1 


    j = n-1
    for i in range (n-k,n-1):
        r[i],r[j] = r[j],r[i]
        j-=1
        
    return r

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
ans = rotate(arr, n, k)
print(ans)

# concpet  I M P O
# 
#  revrse :- return in original list no extra space 
#  Slicing [::-1] :- return in NEW_List mein extra space use 

# tc =o(n) [ [ sc = o( N ) ] ]  usi arr mein reverse kiy hai  

def rotate(arr,n,k):
    arr = arr[::-1]   #  sc = o(1)
    j = n-k-1
    for i in range (0,  n-k -2):
        arr[i ], arr[ j ] = arr[j] , arr[i]
        j-=1 


    j = n-1
    for i in range (n-k,n-1):
        arr[i],arr[j] = arr[j],arr[i]
        j-=1
        
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
ans = rotate(arr, n, k)
print(ans)


print()
print()
# tc =o(n)   sc = o(1)  usi arr mein reverse kiy hai  

def rotate(arr,n,k):
    arr.reverse()   #  sc = o(1)
    j = n-k-1
    for i in range (0,  n-k -2):
        arr[i ], arr[ j ] = arr[j] , arr[i]
        j-=1 


    j = n-1
    for i in range (n-k,n-1):
        arr[i],arr[j] = arr[j],arr[i]
        j-=1
        
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
ans = rotate(arr, n, k)
print(ans)


print()
print()
print()


# Optimum approach     tc = O(2n)   sc = O(1) *

def reverse(arr, i, j):   
    # i = 0                nhi INTIALIZE kr yaha
    # j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def rotate_left_(arr, n, k):
    reverse(arr, 0, k - 1)   # i & j ko yaha intialize kr # jab reverse function call kiya
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
# n = len(arr)
# k = 3

ans = rotate_left_(arr, 7 , 3)
print(ans)
