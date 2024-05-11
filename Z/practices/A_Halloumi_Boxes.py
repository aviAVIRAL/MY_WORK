
# reverse 
def f(n,k,arr):
    x = arr
    ans = sorted(arr)    
    if x == ans :
        return "YES"
    
    if k >= 2 :
        return "YES"
    else :
        return "NO"


# def f(n,k,arr):
#     if k >= 2:
#         for i in range(1,n):
#             if arr[i+1] < arr[i]:
#                 arr[i+1],arr[i] = arr[i], arr[i+1]
# def ff(arr):
#     for i in range(1,len(arr)):
#         if arr[i+1] < arr[i]:
#             arr[i+1],arr[i] = arr[i], arr[i+1]


if __name__=="__main__":
    # t = int(input())
    for _ in range(int(input())):
        n, k = map(int,input().split())
        arr = list(map(int,input().split()))
        print(f(n,k,arr))
















