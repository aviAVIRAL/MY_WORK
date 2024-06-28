# next_permutation : find next lexicographically greater permutation
# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

# Examples
# Example 1 :

# Input format: Arr[] = {1,3,2}
# Output: Arr[] = {2,1,3}
# Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.


# brute :  bus oraly bol na hai only 

# better  using liberarys in python 

from itertools import permutations

arr = [1,3, 2]

arr.sort()

sol = [x for x in permutations(arr)]

target = (1,3,2)
for i in range(len(sol)):
    if sol[i] == target:
        print(sol[i+1])


# op ( 2, 1, 3)

# ........jab last elm hai target to return first elm

from itertools import permutations
arr = [1,3, 2]
arr.sort()
sol = [x for x in permutations(arr)]
target = (3,2,1)
# edge case 
if target == sol[len(sol)-1]:
    print(sol[0])

for i in range(len(sol)-1): # see here 
    if sol[i] == target:
        print(sol[i+1])

# op ( 2, 1, 3)

# represenatation 2
import itertools

arr = [1, 3, 2]
arr.sort()
sol = [x for x in itertools.permutations(arr)]
target = (3, 2, 1)  # ye to tuple hai 

if target == sol[-1]:  # Check if the target is the last permutation
    print(sol[0])  # If so, print the first permutation

for i in range(len(sol) - 1):
    if sol[i] == target:
        print(sol[i + 1])  # Print the next permutation after the target

# correct represntations is 

print( )

def f(nums):
    x = tuple(nums) # concept 
    nums.sort()
    sol = [x for x in permutations(nums)]
    n = len(sol)
    if x == sol[n-1]:
        return sol[0]
    for i in range(n - 1):
        if sol[i] == x :
            return sol[ i +1 ]
            
nums =[1,2,3]
print(f(nums))

# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# optimal 



from typing import List

def nextGreaterPermutation(A: List[int]) -> List[int]:
    n = len(A) # size of the array.

    # Step 1: Find the break point:
    ind = -1 # break point
    for i in range(n-2, -1, -1):
        if A[i] < A[i + 1]:
            # index i is the break point
            ind = i
            break

    # If break point does not exist:
    if ind == -1:
        # reverse the whole array:
        A.reverse()
        return A

    # Step 2: Find the next greater element
    #         and swap it with arr[ind]:
    for i in range(n - 1, ind, -1):
        if A[i] > A[ind]:
            A[i], A[ind] = A[ind], A[i]
            break

    # Step 3: reverse the right half:
    A[ind+1:] = reversed(A[ind+1:])

# or also use  
# A[:] = A[:ind+1] + A[ind+1:][::-1]

    return A

if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextGreaterPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")

print()



















