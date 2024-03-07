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



