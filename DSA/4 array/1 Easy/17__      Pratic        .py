
# def f(arr):
#     n = len(arr)
    
#     j = 0
#     for i in range(n):
#         if arr[i] != 0 :
#             arr[j] = arr[i]
#             j+=1 
      
#     for i in range(j, n):
#         arr[i] = 0 

#     return arr 

# # if __name__=="__main__":

# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(f(arr))

# ..................................................
        
#  cp

# for _ in range(int(input())):
#     n = map(int, input().split())
#     arr = list(map(int, input().split()))
 

#     n = len(arr) # imp to define len gth 
#     j = -1
#     i = 0

#     while i < n:
#         if arr[i] == 0:
#             j = i
#             break
#         i += 1

#     i = j + 1
#     while i < n:
#         if arr[i] != 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             i += 1
#             j += 1
#         else:             #  imp* : else 
#             i += 1

#     # print(*arr)  
#     k = arr
#     for x in k: 
#         print(x, end = " ")


def f(arr):
    # arr= [1,2,3] 
    return arr
if __name__=="__main__":
    for _ in range(int(input())):
        n = map(int, input().split())
        arr = list(map(int, input().split()))
        k = f(arr)
        for x in k : 
            print(x, end = " ")    

# arr = [ 1,2,3]
# k = 3 
# print(f(arr, k ))
# 2
# 5
# 5 0 3 2 0
# 4
# 0 0 2 1


















