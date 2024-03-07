# First and Last Occurrences in Array
# Problem Statement: Given a sorted array arr of n integers and a target value k. Write a program to find the indices of the first and the last occurrences of the target value. If the target is not found then return -1 as indices.

# Note: Consider 0-based indexing

# Pre-requisites: Lower Bound,  Upper Bound, & Binary Search

# Examples
# Example 1:
# Input Format: n = 8, arr[] = {2, 4, 6, 8, 8, 8, 11, 13}, k = 8
# Result: 3 5
# Explanation: The first occurrence of 8 is at index 3 and the last occurrence is at index 5.

# Example 2:
# Input Format: n = 8, arr[] = {2, 4, 6, 8, 8, 8, 11, 13}, k = 10
# Result: -1 -1
# Explanation: The target value is not present in the array. So, we have returned -1 as the indices of the first and the last occurrence.




# brute  by avi    tc 2n    sc 1
def f(a, t):    
    n = len(a)
    f = -1 
    la = -1

    for i in range(n):
        if a[i] == t:
            f = i
            la = i
            break 

    for j in range(n):
        if a[j] == t:
            la = j

    return f, la

if __name__=="__main__":
    arr = [2,4,6,8,8,8,11,13]
    t = 8 
    print(f(arr, t))
            
# brute by striver  tc  n    sc 1 

def firstAndLastPosition(arr,  k):
    
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == k:
            if first == -1:    # imp 
                first = i
            last = i   # last ko to update kr na hee kr na hai else mat likiyo 

    return first, last

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    k = 8
    ans = firstAndLastPosition(arr,  k)
    print("first & last positions r:", ans[0], ans[1])


# optimal     tc O(2*logN)  sc O(1)

# lower bound and ( upper bound - 1 ) se  :

def upperBound(arr, n, x):
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

def lowerBound(arr, n, x):
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

def firstAndLastPosition(arr, n, k):
    lb = lowerBound(arr, n, k)
    if lb == n or arr[lb] != k : # imp 
        return (-1, -1)
    ub = upperBound(arr, n, k)
    return (lb, ub - 1)  # imp ( upperbound - 1 )

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 8
    ans = firstAndLastPosition(arr, n, k)
    print("The first and last positions are:", ans[0], ans[1])

# .......... using bisect 
import bisect

def f(arr, x):
    lb = bisect.bisect_left(arr, x )
    ub = bisect.bisect_right(arr, x ) - 1  # imp

    # edge cases 
    if lb == len(arr)  or arr[lb] != x :  # acc to que 
        lb = -1
    if ub == len(arr) - 1 or arr[lb] != x : 
        ub = -1    

    return lb, ub 

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 8
    ans = f(arr,k)
    print("The first and last positions are:", ans[0], ans[1])


# full binary search from scrach tc same as optimal 

def firstOccurrence(arr, n, k):
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            first = mid
            # look for smaller index on the left
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return first


def lastOccurrence(arr, n, k):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            last = mid
            # look for larger index on the right
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return last


def firstAndLastPosition(arr, n, k):
    first = firstOccurrence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(arr, n, k)
    return (first, last)

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 8
    ans = firstAndLastPosition(arr, n, k)
    print("The first and last positions are:", ans[0], ans[1])



print()