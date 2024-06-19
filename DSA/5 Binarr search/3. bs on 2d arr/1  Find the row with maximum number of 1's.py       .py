# Find the row with maximum number of 1's


# 7

# 0
# Problem Statement: You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. All the rows are sorted in ascending order.
# Your task is to find the index of the row with the maximum number of ones.
# Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1.

# Pre-requisite: Lower Bound implementation, Upper Bound implementation, & Find the first occurrence of a number.

# Examples
# Example 1:
# Input Format:
#  n = 3, m = 3, 
# mat[] = 
# 1 1 1
# 0 0 1
# 0 0 0
# Result:
#  0
# Explanation:
#  The row with the maximum number of ones is 0 (0 - indexed).

# Example 2:
# Input Format:
#  n = 2, m = 2 , 
# mat[] = 
# 0 0
# 0 0
# Result:
#  -1
# Explanation:
#   The matrix does not contain any 1. So, -1 is the answer.


# brute  
# tc O(n X m), sc 1

def f(mat):
    maxi = -1
    for i in range(len(mat)):
        cnt = 0 
        for j in range(len(mat[0])):
            if mat[i][j] == 1 :
                cnt += 1 
        if cnt > maxi :
            maxi = cnt     
            indx = i

    return indx           

mat =  [[1,1,1],[0,1,1],[0,1,1],[1,1,1]]
print(f(mat))

# also repr 

def f(mat):
    maxi = -1
    for i in range(len(mat)):
        cnt = 0 
        for j in range(len(mat[i])):
            cnt += mat[i][j] 
        if cnt > maxi :
            maxi = cnt     
            indx = i

    return indx           

mat =  [[3,1,1],[0,1,1],[1,1,1],[4,1,1]]
print(f(mat))

# optimal 

def lowerBound(arr, x):
    n = len(arr)
    low = 0
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

def f(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

matrix = [[0, 0, 1], [1, 1, 1], [0, 0, 0]]
n = 3
m = 3
print("T is:", f(matrix, n, m))

# using build in fucntion Also Repre .

from bisect import bisect_left as lb  

def lowerBound(arr, x):
    indx = lb(arr, x) 
    return indx 

def f(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

matrix = [[0, 0, 1], [1, 1, 1], [0, 0, 0]]
n = 3
m = 3
print("T is:", f(matrix, n, m))













