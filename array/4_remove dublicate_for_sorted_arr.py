# 1. brute forces by using SET data structure 

# 2. better approach  tc = o(n)   sc = o(n) *due to extra arr

def remove_dublicates(arr):
    i = 0
    new_arr = [arr[0] ]
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1 
            arr[i] = arr[j]
            # new_arr = arr[i] it will return only 3 .'. use append
            new_arr.append(arr[i])
    return new_arr

arr = [1,1,2,2,3,3]
ans = remove_dublicates(arr)
print(ans)


# 3. optimal approach  tc = 0(n)   sc = 0(1)  { use slicing 

def remove_duplicates(arr):
    i = 0
    n = len(arr)
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]  

    return arr[:i + 1]


arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
modified_arr = remove_duplicates(arr)

print( modified_arr )


# 3. optimal approach  tc = 0(n)   sc = 0(1)  { without slicing 

def removeDuplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1


arr = [1, 1, 2, 2, 2, 3, 3]
k = removeDuplicates(arr)

print("The array after removing duplicate elements is ")
for i in range(k):
    print(arr[i], end=" ")