# 1. brute forces Approch 

def Move_all_Zero_at_last(arr,n):
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(n):
        if arr[i] == 0:
            temp.append(arr[i])

    j =0 
    for i in range(0,n):
        arr[i] = temp[j]
        j+=1

    return arr

arr = [1,2,0,4,0,5,0]
ans = Move_all_Zero_at_last(arr,7) # output [1, 2, 4, 5, 0, 0, 0]
print(ans)










