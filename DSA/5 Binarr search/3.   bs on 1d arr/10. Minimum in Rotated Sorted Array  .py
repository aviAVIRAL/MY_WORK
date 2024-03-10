# Minimum in Rotated Sorted Array
# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 

# Pre-requisites: Search in Rotated Sorted Array I,  Search in Rotated Sorted Array II & Binary Search algorithm

# Examples
# Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3]
# Result: 0
# Explanation: Here, the element 0 is the minimum element in the array.

# Example 2:
# Input Format: arr = [3,4,5,1,2]
# Result: 1
# Explanation: Here, the element 1 is the minimum element in the array.


# brute using  min()   TC n  SC 1

# optimal using binary search   tc logN   sc 1 

import sys
def findMin(arr: [int]):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:  # if left part is sorted
            ans = min(ans, arr[low])  # keep the minimum
            low = mid + 1  # eliminate left half
            
        else:  # if right part is sorted
            ans = min(ans, arr[mid])  # keep the minimum
            high = mid - 1  # eliminate right half

    return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findMin(arr)
    print("The minimum element is:", ans)

# for dub
















