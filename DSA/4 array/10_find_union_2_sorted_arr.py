
# Example 1:
# Input:
# n = 5,m = 5.
# arr1[] = {1,2,3,4,5}  
# arr2[] = {2,3,4,4,5}
# Output:
#  {1,2,3,4,5}

# Explanation: 
# Common Elements in arr1 and arr2  are:  2,3,4,5
# Distnict Elements in arr1 are : 1
# Distnict Elemennts in arr2 are : No distinct elements.
# Union of arr1 and arr2 is {1,2,3,4,5} 

# Example 2:
# Input:
# n = 10,m = 7.
# arr1[] = {1,2,3,4,5,6,7,8,9,10}
# arr2[] = {2,3,4,4,5,11,12}
# Output: {1,2,3,4,5,6,7,8,9,10,11,12}
# Explanation: 
# Common Elements in arr1 and arr2  are:  2,3,4,5
# Distnict Elements in arr1 are : 1,6,7,8,9,10
# Distnict Elemennts in arr2 are : 11,12
# Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12} 


# 1.  brute  tc = sc = o(n) + o(m) + o(m+n)

def f(arr1 , arr2):
    s = set()
    temp = [ ]

    for X in arr1:
        s.add(X)
        

    for X in arr2:
        s.add(X)

    for X in s:
        temp.append(X)

    return temp 

arr1 = [1,1,2,3,3,4,5]
arr2 = [1,2,3,4,5,6,7]

ans = f(arr1,arr2)
print(ans)

# also represent it like :- 

    # n =  len(arr1)
    # m =  len(arr2)
    
    # for i in range(n):
    #     s.add(arr1[i])
        

    # for i in range(m):
    #     s.add(arr2[i])

# carefull : set() indexing issue 

print()

# 1.brute force  tc =o(n) + o(m) +o(n+m) = o(2n+2m) ~> o(n+m)
                # sc = ~> o(n+m)


def f(arr1, arr2):
    temp = []
    s = set()
    s.update(arr1)
    s.update(arr2)

    for x in s:
        temp.append(x)

    return temp

arr1 = [1, 1, 2, 3, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7]

ans = f(arr1, arr2)
print(ans)

print()

# 2.optimal sol : tc = o(n) + o(m)  ~>  o(m+n)
                # sc = o(m+n)
                # but sc = o(1) if union[ ] ka space not cnsider

# r1



def union_of_2_sorted_arr_is(arr1 , arr2):
    n = len(arr1)              
    m = len(arr2)
    
    i = 0
    j = 0

    union = []
    
                  # len(union) == 0  also represent as 
                  # len(union) == 0  also represent as 
                  # union == [ ]     to check list is empty or not 
                  # not union
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:     
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j +=1

    while i < n:
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < m:
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union 

arr1 = [1,1,2,3,3,4,5]
arr2 = [1,2,3,4,5,6,7]

ans = union_of_2_sorted_arr_is(arr1,arr2)
print(ans)

 

# r2 
def union_of_2_sorted_arr_is(arr1 , arr2):
    i = 0
    j= 0
    union = []
                  # len(union) == 0  also represent as 
                  # union == [ ]     to check list is empty or not 
                  # not union
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:     
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j +=1

    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union 

arr1 = [1,1,2,3,3,4,5]
arr2 = [1,2,3,4,5,6,7]

ans = union_of_2_sorted_arr_is(arr1,arr2)
print(ans)




