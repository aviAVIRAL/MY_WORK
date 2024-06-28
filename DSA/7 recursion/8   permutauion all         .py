
# brute sc high  due to map tech 
res = []
def f( arr, freq, ds):
    if len(ds) == len(arr):
        res.append(ds[:]) # res.append(ds.copy())
        return
    for i in range(0, len(arr)):
        if freq[i] == 0:       
        # if not freq[i]:
            ds.append(arr[i])
            freq[i] = 1
            f(arr, freq, ds)
            freq[i] = 0
            ds.pop()

arr = [1, 2, 3]
res = []
freq = [0] * len(arr)
f(arr, freq, [])
print(res)


# The syntax if not freq[i]: is a shorthand way of checking if the value at index i in the freq list is False or 0. In Python, any value that evaluates to False in a boolean context will cause the if not condition to be true.
#  if freq[i] == 0:       
#         # if not freq[i]:

print()
# optimal using swaping technique  sc optimize 
res=[]
def f( arr, i):
    if i == len(arr):
        res.append(arr[:]) # 
        return
    for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            f(arr, i+1)
            arr[i], arr[j] = arr[j], arr[i]

arr = [1, 2, 3]
f(arr,0)
print(res)



# ........ total leetcode representation ..........
from typing import List

class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        res = []

        def f(arr, i):
            if i == len(arr):
                res.append(arr[:])  # Make a copy of arr and append to res
                return
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]  # Swap
                f(arr, i + 1)
                arr[i], arr[j] = arr[j], arr[i]  # Swap back

        f(arr, 0)
        return res

# Example usage
if __name__ == "__main__":
    obj = Solution()
    v = [1, 2, 3]
    permutations = obj.permute(v)
    print("All Permutations are:")
    for perm in permutations:
        print(perm)















