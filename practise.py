

from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s = 0
            for K in range(i, j+1):
                s += a[K]

            if s == k:
                length = max(length, j - i + 1)
    return length

if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")



from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0  # Initialize a variable to count the subarrays with sum k
        for i in range(n):
            s = 0  # Initialize the running sum
            for j in range(i, n):
                s += nums[j]  # Update the running sum
                if s == k:
                    count += 1  # Increment count when the sum equals k
        return count

if __name__ == "__main__":
	a = [1,2,3,1,1,1,1,4,2,3]
	k = 3

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")
     






#   it will count total  sub arry  which are equal t k 
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    count += 1
        
        return count








