# Find out how many times the array has been rotated { unique elm }
# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated. 

# Pre-requisites: Find minimum in Rotated Sorted Array,  Search in Rotated Sorted Array II & Binary Search algorithm

# Examples
# Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3]
# Result: 4
# Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

# Example 2:
# Input Format: arr = [3,4,5,1,2]
# Result: 3
# Explanation: The original array should be [1,2,3,4,5]. So, we can notice that the array has been rotated 3 times.



# brute 
def findKRotation(arr):
    ans = float('inf')
    index = -1
    for i in range(len(arr)):
        num = arr[i]
        if num < ans:
            ans = num
            index = i
    return index

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findKRotation(arr)
    print("The array is rotated", ans, "times.")

# optimal  tc : O(logN)

def findMinIndex(arr):
    low = 0
    high = len(arr) - 1
    ans = float("inf")
    inx = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:  # if left part is sorted
            if arr[low] < ans:
                ans = arr[low]
                inx = low
            low = mid + 1  # eliminate left half
            
        else:  # if right part is sorted
            if arr[mid] < ans:
                ans = arr[mid]
                inx = mid
            high = mid - 1  # eliminate right half

    return inx 

if __name__ == "__main__":
    arr = [4,5,6,7,8,9,   1, 2, 3]
    inx = findMinIndex(arr)
    if inx == -1:
        print("No minimum element found.")
    else:
        print("The index of the minimum element is:", inx)









