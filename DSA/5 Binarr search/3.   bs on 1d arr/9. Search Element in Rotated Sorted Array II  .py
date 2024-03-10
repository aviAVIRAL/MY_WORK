# Search Element in Rotated Sorted Array II
# Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False. 

# Pre-requisite: Search Element in Rotated Sorted Array I & Binary Search algorithm

# Examples
# Example 1:
# Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
# Result: True
# Explanation: The element 3 is present in the array. So, the answer is True.

# Example 2:
# Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
# Result: False
# Explanation: The element 10 is not present in the array. So, the answer is False.

# brute 
# simple linear search 

# Optimal (Using Binary Search): tc : O(logN)  

from typing import *
def searchInARotatedSortedArrayII(arr : List[int], k : int) -> bool:
    n = len(arr)  # size of the array
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # if mid points to the target
        if arr[mid] == k:
            return True

        # Edge case  :    [ 3,1,4,5,3,3,3,3,3] target = 3
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1

    return False

if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    k = 3
    ans = searchInARotatedSortedArrayII(arr, k)
    if not ans:
        print("Target is not present.")
    else:
        print("Target is present in the array.")




