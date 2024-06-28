

# my rep /

def f(arr, brr , i , k):
    if i  == len(arr):
        if k == 0:      
            print(brr)
        return
    
    if arr[i] <= k :
        brr.append(arr[i])
        f(arr, brr ,i, k - arr[i])
        brr.pop()
    f(arr, brr , i+1, k)

# Example usage
arr = [2 , 3, 6, 7 ]
f(arr, [], 0, 7 )
print()


# ... .. .... . .  ... .. ... .. ... .. ... . ...
# leet code reprer

# class Solution:
#     def combinationSum(self, arr: List[int], k: int) -> List[List[int]]:
#         ans = []
#         ds = [] # see impo repr also 

#         def f(i: int, k: int):
#             if i == len(arr):
#                 if k == 0:
#                     ans.append(ds[:])
#                 return
#             if arr[i] <= k:
#                 ds.append(arr[i])
#                 f(i, k - arr[i])
#                 ds.pop()
#             f(i + 1, k)
#         f(0, k)  # see impo repr 
#         return ans

# if __name__ == "__main__":
#     obj = Solution()
#     arr = [2, 3, 6, 7]
#     k = 7
#     ans = obj.combinationSum(arr, k)
#     print("Combinations are: ")
#     for i in range(len(ans)):
#         for j in range(len(ans[i])):
#             print(ans[i][j], end=" ")
#         print()








