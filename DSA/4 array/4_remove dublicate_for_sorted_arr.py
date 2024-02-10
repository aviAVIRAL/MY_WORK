# 1. brute forces  by using SET data structure 
#    by use of set data structure  tc = o(nlogn) sc = o(n)
#    using set data structure : not good for leedcode 

# Q 1 return "Count" / total number of, unique element 
def f(arr) : 
    s = set()
    n = len(arr)

    for i in range(n):
        s.add(arr[i])
    
    k = len(s)
    j = 0
    for x in s:
        arr[j] = x
        j += 1

    return k  # or return j 

# output will : 3  only 
if __name__ == "__main__":
    arr = [1, 1, 2,  2, 2, 3, 3]
    print(f(arr))

# Q 2 return arr of unique elements only 
def f(arr) : 
    s = set()
    n = len(arr)

    s.update(arr)
    
    k = len(s)
    j = 0
    for x in s:
        arr[j] = x
        j += 1

    return arr[:k]   # or return [:j]

# output will : [1,2,3]  
if __name__ == "__main__":
    arr = [1, 1, 2,  2, 2, 3, 3 ]
    print(f(arr))

# ...............................
    # concept 
#  T.C = O(n) is generally better than O(n log n)
    
#  .............................. 
      
# 2  better tc = o(n)  , sc = o(n)  due to temp [ full logic]
# r 1
print()
def f(arr):
    
    temp = []
    i = 0
    j = 1
    
    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            temp.append(arr[i])  # 
        else:
            j += 1

    return temp    # output = [ 1, 2, 3, 4] 

if __name__ == "__main__":
    arr = [1,1,   2,2,  3,3,  4,4]
    print(f(arr))


# better tc=o(n) :sc=o(n) due to  sllicing ,use build in function  
# r 2 
def fun(arr):
    
    # temp = [ ]  no need 
    i = 0
    j = 1
    
    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            # temp.append(arr[i])  no need
        j += 1

    return arr[:i+1]       # or  return i+1  than output : 4 
   
if __name__ == "__main__":
    arr = [1,1,   2,2,  3,3,  4,4]
    print(fun(arr))
    # output = [ 1, 2, 3, 4] 

# ..................................

# 3. optimal approach  tc = 0(n) , sc = 0(1) bolo ki mere logic mein no extra space but quetion demand the extra space therfore sc = o(n) 

# rep 1 :  while loop 
def f(arr):
    i = 0
    j = 1
    
    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        j += 1
    
    return i + 1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = f(arr)      # k = 3 ayega 
    for i in range(k):
        print(arr[i], end=" ")

# rep 2 ;  while loop ,if elif 
def f(arr):
    i = 0
    j = 1
    
    while j < len(arr):

        if arr[i] == arr[j]:
            j+=1
        elif arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
                                               
        j += 1      # also use else: here
           
    
    return i + 1
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = f(arr)

    print("Now duplicates removed:")
    for i in range(k):
        print(arr[i], end=" ")

# rep 3 , for loop 
def removeDuplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

if __name__=="__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)

    print(" array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")

# output  [1 2 3]

# ..................................
# ..................................
        
#    i did it by using map | dictionary | { }  concept 

# unsorted arr = [ 2,4,6,5,4,2,2,4,10,10]
# output = []

# r1 map
def get_median(arr):
    n = len(arr)
    mp = { }
    for i in range(n):
        if arr[i] in mp:  # in operator
            mp[arr[i]] +=1 
        else:
            mp[arr[i]] = 1

    temp = [ ]    
    for x in mp:
            temp.append(x)

    return temp 

if __name__ == "__main__":
    arr = [10, 2, 2, 10, 5, 6 ,3]
    print (arr)
    print("remove dulicates", get_median(arr))

# r2 map 


def f(arr):
    mp = { }
    n = len(arr)
    for i in range(n): 
        if arr[i] not in mp:  # not in operator
            mp[arr[i]] = 1
        else:
            mp[arr[i]] += 1
    
    temp = []
    for x in mp: 
        temp.append(x)
    return temp
if __name__=="__main__":
    arr = [1,1,1,2,2,3,3,4,5,5]
    print(f(arr))

# best representation 
# tc = o(n) + o(n) | sc = o(n)    worst mein all unique elemnet ho to mp mein nth space complexity and temp mein jayega therfor space compacity will be o(n)
print()

def f(arr):
   
    mp = { }     # n = len(arr)   arr[i] => no need to write  
    for y in arr: 
        if y not in mp:
            mp[y] = 1
        else:
            mp[y] += 1
    
    temp = []
    for x in mp: 
        temp.append(x)
    return temp
if __name__=="__main__":
    arr = [1,1,1,2,2,3,3,4,5,5]
    print(f(arr))

# representation 
def removeDuplicates( arr): 
    mp={}
    for x in arr: 
        if x not in mp :
            mp[x] = 1
        else :
            mp[x]+=1 
    j = 0
    for y in mp :
        arr[j] = y
        j+= 1

    return j
if __name__=="__main__":
    arr = [9,1,8,2,2,3,3,4,5,5]
    print(removeDuplicates(arr))

# ..................................

#  u can ignore it :  Brute forces by own 

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
# .............................................
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

