

 

def f(arr, brr , i):
    if i  == len(arr):
        print(brr )
        return

    brr.append(arr[i])
    f(arr, brr , i  + 1)
    
    brr.pop()  # also     brr.remove(arr[i])
    f(arr, brr , i  + 1)

# Example usage
arr = [1, 2, 3]
f(arr, [], 0)


# ......... leetcode . .....................
from typing import List

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        def f(arr, brr, index):
            # If we have considered all elements
            if index == len(arr):
                result.append(brr[:]) # I M P O  Append a copy of the current subset
                return
            
            # Include the current element
            brr.append(arr[index])
            f(arr, brr, index + 1)
            
            # Exclude the current element
            brr.pop()
            f(arr, brr, index + 1)
        
        result = []
        f(arr, [], 0)
        return result

# Example usage
sol = Solution()
print(sol.subsets([1, 2, 3]))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


