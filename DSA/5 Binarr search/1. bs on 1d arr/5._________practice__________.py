def floor(arr, x):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] <= x:  # imp
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return high #upper value ye index return 


arr = [3, 4, 4, 4 ,  7, 8, 10]
x = 5
ans = floor(arr, x)
print(ans)
print()
def floor(arr, x):
    n = len(arr)
    f = -1 
    la = -1
    for i in range(n):
        if arr[i] == x:
            if f == -1:  f = i 
            la = i 
    return f"{f} {la}" 
arr = [3, 5,5,5 ,5,5,5, 5 , 7, 8, 10]
x = 5
ans = floor(arr, x)
print(ans)




