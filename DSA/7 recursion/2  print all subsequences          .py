

# ........also repre 

def f(arr, brr =[], i =0):
    if i  == len(arr):
        print(brr )
        return

    brr.append(arr[i])
    f(arr, brr , i  + 1)
    
    brr.pop()
    f(arr, brr , i  + 1)

# Example usage
arr = [1, 2, 3]
f(arr)
# .................................

# also rep  best practices 

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

# ...................see all posiible representation  ....... 
print()

# r1 best practices  .....................
result = []

def f(arr, brr , i):
    if i  == len(arr):
        result.append(brr[:])
        return
    brr.append(arr[i])
    f(arr, brr , i  + 1)
    brr.pop()  
    f(arr, brr , i  + 1)
# Example usage
arr = [1, 2, 3]
f(arr, [], 0)
print(result)
# .........................................

# r2
result = []
brr = []  # teek hai but i dont like this practices 
def f(arr , i):
    if i  == len(arr):
        result.append(brr[:])
        return
    brr.append(arr[i])
    f(arr , i  + 1)
    brr.pop()  
    f(arr , i  + 1)
# Example usage
arr = [1, 2, 3]
f(arr , 0)
print(result)



# r3  ye wala not correct error de ga result ko always outside th efunction  


# def f(arr, brr , i, result): # wrong op wrong code 
#     if i  == len(arr):
#         result.append(brr[:])
#         return
#     brr.append(arr[i])
#     f(arr, brr , i  + 1, result)
#     brr.pop()  
#     f(arr, brr , i  + 1, result)
# # Example usage
# arr = [1, 2, 3]
# f(arr, [], 0, [])

# print(result)  wrong op 

# # print(result)


# ......... leetcode . .....................
from typing import List

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        result = []
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
        
        
        f(arr, [], 0)
        return result

# Example usage
sol = Solution()
print(sol.subsets([1, 2, 3]))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

# ..............................

