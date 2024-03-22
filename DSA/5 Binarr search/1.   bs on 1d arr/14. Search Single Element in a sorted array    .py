# Search Single Element in a sorted array
# Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

# Pre-requisite: Binary Search Algorithm

# Examples
# Example 1:
# Input Format: arr[] = {1,1,2,2,3,3,4,5,5,6,6}
# Result: 4
# Explanation: Only the number 4 appears once in the array.

# Example 2:

# Input Format: arr[] = {1,1,3,5,5}
# Result: 3
# Explanation: Only the number 3 appears once in the array.


# ...........................  same quetion in arr u will find it
#  just return unique elm  
# ...........................

# my  bhai aapne app kiya hai  brute 
def f(arr,n):
    if arr[n-1] != arr[n-2]: # edge case
        return arr[n-1]
    for i in range(0, n-1, +2):
        if arr[i] != arr[i+ 1]:
            return arr[i]
arr = [ 1,1,2,2,3,3,4,4,5,5,6,6,11]      
print(f(arr, len(arr)))  
arr = [ 1,1,2,2,3,3,4,4,100,5,5,6,6]      
print(f(arr, len(arr)))  


# Optimal Approach(Using Binary Search):   tc  log n 



def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the single element:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # We are in the left:
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
        # We are in the right:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)

