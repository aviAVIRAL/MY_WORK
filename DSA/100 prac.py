




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
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
# .........................................

# brute    linear search tc = 0 (n)

def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] >= x:
            #lower bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)   
# op  lower bound is the index: 3


# optimal  binary seach  TC  O(logN) : SC 1

def lowerBound(arr, n ,x ) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)
# op  lower bound is the index: 3

# cp  

# build in liberary/module => bisect | same tc sc as binary search  
# tc log n : sc 1 

print()





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
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
# .........................................

# brute    linear search tc = 0 (n)

def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] > x:
            #lower bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)   
# op  lower bound is the index: 3


# optimal  binary seach  TC  O(logN) : SC 1

def lowerBound(arr, n ,x ) -> int:
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
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)

if __name__ == "__main__":
    arr = [3, 5, 8,9, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)
# op  lower bound is the index: 3

# cp  

# build in liberary/module => bisect | same tc sc as binary search  
# tc log n : sc 1 

