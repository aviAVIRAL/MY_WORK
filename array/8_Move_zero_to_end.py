# 1. brute forces Approch   tc =  o(n) +o(n) = O(2n) ~> O(n)  & sc = o(n)

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

arr = [1,2,0,4,0,5,0,1]
ans = Move_all_Zero_at_last(arr,8) # output [1, 2, 4, 5, 0, 0, 0]
print(ans)


# 2. oprimal solution tc = o(x) + o(n -x) ~> o(n)    sc = o(1)

def Move_Zero_at_last(arr,n):

    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range( j+1 , n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    
    return arr


arr = [1,2,0,4,0,0,5,0]
ans = Move_Zero_at_last(arr,7) # output [1, 2, 4, 5, 0, 0, 0]
print(ans)











