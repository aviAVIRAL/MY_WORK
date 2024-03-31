# Search Insert Position
# Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

# If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

# Pre-requisite: Lower Bound & Binary Search

# Example 1:
# Input Format: arr[] = {1,2,4,7}, x = 6
# Result: 3
# Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

# Example 2:
# Input Format: arr[] = {1,2,4,7}, x = 2
# Result: 1
# Explanation: 2 is present in the array and so we will return its index i.e. 1.




# ...........................

# just similar to lower bound 

# ...........................


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
# import bisect as bs
# from bisect import bisect_left
print ( )   
print ( )   
# ...................................................
    # concept to inser the elm in arr 


import bisect

def lowerBound(arr, x):
    index = bisect.bisect_left(arr, x)
    arr.insert(index, x)
    return index

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 15, 15, 19, 20]
    x = 15
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
    print("Updated arr after insertion:", arr)
# The lower bound is the index: 3
# Updated arr after insertion: [3, 5, 8, 15,
# 15, 15, 15, 19, 20

print()

import bisect

def lowerBound(arr, x):
    index = bisect.bisect_right(arr, x)
    arr.insert(index, x)
    return index

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 15, 15, 19, 20]
    x = 15 
    ind = lowerBound(arr, x)
    print("The upper bound is the index:", ind)
    print("Updated arr after insertion:", arr)

# The upper bound is the index: 6
# Updated arr after insertion: [3, 5, 8, 15,
# 15, 15, 15, 19, 20]
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
    

   


import bisect

arr = [1, 2, 3, 3, 3, 4, 5]

# Using bisect_left
print("Using bisect_left:")
print("Insertion point for 3:", bisect.bisect_left(arr, 3))  # Output: 2
print("Insertion point for 6:", bisect.bisect_left(arr, 6))  # Output: 7 (since 6 would be inserted at index 7 to maintain sorting)

# Using bisect_right
print("\nUsing bisect_right:")
print("Insertion point for 3:", bisect.bisect_right(arr, 3))  # Output: 5 (since 3 would be inserted at index 5 to maintain sorting)
print("Insertion point for 6:", bisect.bisect_right(arr, 6))  # Output: 7 (since 6 would be inserted at index 7 to maintain sorting)

print()
print()


import bisect

arr = [1, 2, 3, 4, 5]

# Using bisect_left
print("Using bisect_left:")
print("Insertion point for 3:", bisect.bisect_left(arr, 3))  # Output: 2
print("Insertion point for 6:", bisect.bisect_left(arr, 6))  # Output: 7 (since 6 would be inserted at index 7 to maintain sorting)

# Using bisect_right
print("\nUsing bisect_right:")
print("Insertion point for 3:", bisect.bisect_right(arr, 3))  # Output: 5 (since 3 would be inserted at index 5 to maintain sorting)
print("Insertion point for 6:", bisect.bisect_right(arr, 6))  # Output: 7 (since 6 would be inserted at index 7 to maintain sorting)



