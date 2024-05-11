
# for _ in range(int(input())):
#     k = int(input())
#     arr = list(map(int, input().split()))

#     maxi = -1
#     n = len(arr)
#     for i in range(n):
#         s = 0
#         for j in range(i, n):
#             s += arr[j]
#             if s == k and (j - i + 1) > maxi : 
#                 # maxi = max(maxi, j - i + 1 )
#                 maxi = j - i + 1
#                 subarr = arr[i: j + 1]
#     print(maxi, subarr)

# # # ip 
# # 2 test cases 
# # 10 k 
# # 2 3 5 1 9  arr 
# # 3 [2, 3, 5] op

# # 15 k 
# # 5 5 5 20 arr 
# # 3 [5, 5, 5] op




