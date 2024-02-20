
#  right rotation place not left caerfuly

def rotate_by_k_place(arr, n, k):
    k = k % n   
    temp = []

    for i in range(0, n-k):
        temp.append(arr[i])


    j = 0
    for i in range(n-k, n):
         arr[j] = arr[i]
         j += 1    
    

    j = 0
    for i in range(k, n):
        arr[i] = temp[j]
        j += 1    
       

    return arr

arr = [1, 2, 3, 4, 5,   6, 7  ]
n = 7
k = 2  # output [6, 7,    1, 2, 3, 4, 5]
ans = rotate_by_k_place(arr, n, k)
print(ans)



# Time Complexity: O(n)
# Space Complexity: O(n) *

def right_rotate_by_k_places(arr, n, k):
    k = k % n

    arr[::] = arr[-k:] + arr[:-k]
    
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
ans = right_rotate_by_k_places(arr, n, k)
print(ans)


