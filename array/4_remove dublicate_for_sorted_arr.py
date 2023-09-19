# 1.  brute forces  by using SET data structure 
#     :- by use of set data structure  tc =o(n) sc =o(n)

def duplicate_remove(arr, n):
    new_arr = set(arr)
    return new_arr

arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
ans = duplicate_remove(arr, 10)

print(ans)

print() 

# 1. brute forces

def dublicate_hata_bhai(arr):
    s =set()
    s.update(arr)
    arr[:] =list(s)
    return arr

arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
ans = dublicate_hata_bhai(arr)
print(ans)


# 1. brute forces :-  tc =o(n) sc =o(n)

def find_union(arr):
    s = set()
    temp = []
    
    for each_element in arr:
        s.add(each_element)
    temp.append(s)

    return temp

arr = [1,1,2,2,3,3]
ans = find_union(arr)
print(ans)

# 1. brute forces 
def removeDuplicates(arr): 
    s = set()
    for each_element in arr:
        s.add(each_element)
    arr[:] = s
    return arr  

arr = [1, 1, 2, 2, 3, 3]
ans = removeDuplicates(arr)
print(ans)

# set() never return the sme odering indexing 
# code is correct  but leedcode hidden test case will not pass
# therfore set() data structure is not a good practices

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

# 1.brute approach : 
# 
# set mein odering correct kr ne ki trick but time complexity bahut 
# hee bekar aye ge bhai due to sorted()
def remove_dublicatesbhai(arr):
        s = set()
        s.update(arr)
        ans = list(s) 
        arr[:] = sorted(ans) 
#  ans act as variable that hold list  
        return arr
arr = [1,1,2,2,3,3]
ans = remove_dublicatesbhai(arr)
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

print()
