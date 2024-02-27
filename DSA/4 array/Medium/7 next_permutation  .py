# next_permutation : find next lexicographically greater permutation
# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

# Examples
# Example 1 :

# Input format: Arr[] = {1,3,2}
# Output: Arr[] = {2,1,3}
# Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.


# brute : 

# better  using liberarys in python :

# concept 

from itertools import permutations
arr = [1,3,2 ]
k = permutations(arr)
for x in k:
    print(x, end = "")
# op (1, 2, 3)(1, 3, 2)(2, 1, 3)(2, 3, 1)(3, 1, 2)(3, 2, 1)
    
print()
print()

from itertools import permutations

arr = [1, 3, 2]

# Get all permutations of the array as a list
perms = list(permutations(arr))

# Check if there is a next permutation
if len(perms) > 1:
    # Get the next permutation
    next_perm = perms[1]

    # Print the next permutation
    print(*next_perm)
else:
    print("There is no next permutation.")

