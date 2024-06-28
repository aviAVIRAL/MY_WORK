
# brute 

res = set()
def f(arr, brr , i ):
    if i  == len(arr):
        res.add(tuple(brr))
        return
    
    brr.append(arr[i])
    f(arr, brr ,i+1 )
    brr.pop()
    f(arr, brr , i+1)

arr = [1,1,2]
f(arr, [], 0 )
print(res)

# .................. repre in arr form trick 

ans = []
for x in res : 
    ans.append(list(x))
print(ans)

# ...........................
print()
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = set()


        def fun(index: int, ds: List[int]):
            if index == len(nums):
                ds.sort()
                res.add(tuple(ds))
                return
            ds.append(nums[index])
            fun(index + 1, ds)
            ds.pop()
            fun(index + 1, ds)
        fun(0, [])
        for it in res:
            ans.append(list(it))
        return ans




if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print("[ ", end="")
    for i in range(len(ans)):
        print("[ ", end="")
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print("]", end="")


 # optima l  

res = []
def f(arr, i, ds):
    res.append(ds[:])
    for j in range(i, len(arr)):
        if j != i and arr[j] == arr[j - 1]:
            continue
        ds.append(arr[j])
        f(arr, j + 1, ds)
        ds.pop()


arr = [1, 2, 2]
f(arr, 0, [])
print(*res)

# leetcode  rep 

print()
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def findSubsets(ind, ds):
            ans.append(ds[:])
            for i in range(ind, len(nums)):
                if i != ind and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])
                findSubsets(i + 1, ds)
                ds.pop()
        nums.sort()
        findSubsets(0, [])
        return ans

if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print(*ans)