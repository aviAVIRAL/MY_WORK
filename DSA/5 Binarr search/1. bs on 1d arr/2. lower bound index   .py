
# Implement Lower Bound
# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

# Pre-requisite: Binary Search algorithm

# Examples
# Example 1:
# Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
# Result: 1
# Explanation: Index 1 is the smallest index such that arr[1] >= x.

# Example 2:
# Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] >= x.

# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# What is Lower Bound
# The lower bound algorithm finds the first or the smallest elm index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
# .........................................

# brute    linear search tc = 0 (n)

def lowerBound(arr, n, x) -> int:
    for i in range(n):
        if arr[i] >= x:
            #lower bound found
            return i
    return n
if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9 # op  lower bound is the index: 3 
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)  


# optimal  binary seach  TC  O(logN) : SC 1

def lowerBound(arr ,x ) -> int:
    n = len(arr)
    low = 0    # low, high = 0, n - 1
    high = n - 1   

    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:  # if x  <= arr[mid] :
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    x = 9
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
# op  lower bound is the index: 3

# ....repre .....  skdate  : reip ans to upturn low ya high
# optimal  binary seach  TC  O(logN) : SC 1

def lowerBound(arr ,x ) -> int:
    n = len(arr)
    low = 0    # low, high = 0, n - 1
    high = n - 1   

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:  
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return low

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    x = 9
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
# op  lower bound is the index: 3
if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    x = 1111119
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
if __name__ == "__main__":
    arr = [3, 5, 8, 9 , 15, 19]
    x = 9
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
# op  lower bound is the index: 3


# cp  

# build in liberary/module => bisect | same tc sc as binary search  
# tc log n : sc 1 

import bisect

def lowerBound(arr, x):

    return bisect.bisect_left(arr, x)

if __name__ == "__main__":
    arr = [3, 5, 8, 15,15,15, 19]
    x = 9  # op The lower bound is the index: 3
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)


# ..................representation..............
# import bisect
# import bisect as bl
# from bisect import bisect_left
# from bisect import bisect_left as bl
    
# ...................................................
    # concept to inser the elm in arr 

import bisect

def lowerBound(arr, x):
    index = bisect.bisect_left(arr, x)
    arr.insert(index, x)
    return index

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 15, 15, 19]
    x = 9
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
    print("Updated arr after insertion:", arr)
# ........................................
    
# rep resentation 
    
from bisect import bisect_left

def lowerBound(arr, x):
    index = bisect_left(arr, x)
    arr.insert(index, x)
    return index

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 15, 15, 19]
    x = 9
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
    print("Updated arr after insertion:", arr)
# ........................................
# from bisect import bisect_left as bl
    
from bisect import bisect_left as bl

def lowerBound(arr, x):

    return bl(arr, x)

if __name__ == "__main__":
    arr = [ 1,2,3, 15,15,15,18,19]
    x = 15 # op The lower bound is the index: 3
    ind = lowerBound(arr, x)
    print("Thesndex:", ind)


# .................... CONCEPT ..............
    #  x not found in arr , by defalut value is len(arr)
import bisect

def f(arr, x):

    lb = bisect.bisect_left(arr, x)
    ub = bisect.bisect_right(arr, x)
    return lb , ub 

if __name__ == "__main__":
    arr = [0, 1, 2, 8,8,8, 14, 21,22]  # 9 len of arr
    x = 11111118  
    print(f(arr, x))
    # op  9 , 9 

print()
# .................... CONCEPT ..........
   # u can modify the op if x not found in arr  : acc 2 que need
import bisect 

def f(arr, x):
    
    n = len(arr)
    lb= bisect.bisect_left(arr, x)
    ub= bisect.bisect_right(arr, x)

    if lb == n :   # modify according to que need 
        lb = -9995
    if ub == n :
        ub = -19877    
    return lb , ub 

if __name__ == "__main__":
    arr = [0, 1, 2, 8,8,8, 14, 21,22]  # 9 len of arr
    x = 11111118  
    print(f(arr, x))
# op (-9995, -19877)
    

   