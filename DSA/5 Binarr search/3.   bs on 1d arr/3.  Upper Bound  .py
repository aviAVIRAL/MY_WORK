
# Implement Upper Bound
# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

# Pre-requisite: Binary Search algorithm

# Examples
# Example 1:
# Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] > x.

# Example 2:
# Input Format: N = 6, arr[] = {3,5,8,9,15,19}, x = 9
# Result: 4
# Explanation: Index 4 is the smallest index such that arr[4] > x.

# ....................................
# What is Upper Bound?
# The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.
# ....................................

# brute   linear search  tc  O(N)   sc 1

def upperBound(arr, x, n):
    for i in range(n):
        if arr[i] > x:
            # upper bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    n = 6
    x = 9
    ind = upperBound(arr, x, n)
    print("The upper bound is the index:", ind)


# optimal    (Using Binary Search)  tc O(logN)  sc 1    

def upperBound(arr, x) :
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    x = 9
    ind = upperBound(arr, x)
    print("The upper bound is the index:", ind)
    
if __name__ == "__main__":
    arr = [3, 5, 8, 15,15,15, 19]
    x = 9  # op The lower bound is the index: 3
    ind = upperBound(arr, x)
    print("The upper bound is the index:", ind)



# bisect_right ( )    