# 1. brute forces  tc = o(n)  sc =o(n)

# r1  
def rotate_by_1_place(arr):
    n = len(arr)
    temp = [0] * n
    
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]  # This line should be outside the loop
    
    return temp

arr = [1, 2, 3, 4, 5]
print("original arr:",arr)
ans = rotate_by_1_place(arr)
print("rotaed by 1 :" ,ans)

# r2
def f(arr) : 
    n = len(arr)
    temp = [0]* n
    
    i = 1 
    while i <n:
        temp[i-1]= arr[i]
        i += 1
    temp[n-1] = arr[0]

    return temp

if __name__ == "__main__":
    arr = [1, 2,3,4,5]
    print(f(arr))

# 2 . Optimum approach  tc = o(n)  sc = o(1)

# r1 
def rotat_by_1(arr):
    n = len(arr)
    temp = arr [ 0 ]
    
    for i in range (1, n):
        arr[i - 1] = arr [i]

    arr[n - 1] = temp  # pure loop ke iterrate ke baad last mein...
    
    return arr

arr = [1, 2, 3, 4, 5]
ans = rotat_by_1(arr)
print(ans)

# r2 

def f(arr) : 
    n = len(arr)
    temp = arr[0]
    
    i = 1 
    while i < n:
        arr[i-1]= arr[i]
        i += 1
    arr[n-1] = temp 

    return arr

if __name__ == "__main__":
    arr = [1, 2,3,4,5]
    print(f(arr))

# ..............................

# build in function slicing operator

    
arr = [1 , 2, 3 ,4 ,5,6]

n = len(arr)

arr[:] = arr[1:n] + arr[:1]

print(arr)

# ........................

# slicing conept 

arr = [11 , 12, 13 ,  14  , 15 , 16,  17]
    #  0    1    2    3     4    5     6   indexing

ans = arr[ 1: 5 ][ : : -1 ]

# matlab 1 se 4 tak ki index slice kr & reversed kr do 

print(ans)

# output [15, 14, 13, 12]
