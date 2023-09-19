# 1.  brute  tc = sc = o(n) + o(m) + o(m+n)

def union_of_2_sorted_arr(arr1 , arr2):
    s = set()
    union = [ ]

    for each_element in arr1:
        s.add(each_element)
        

    for each_element in arr2:
        s.add(each_element)

    for each_element in s:
        union.append(each_element)

    return union 

arr1 = [1,1,2,3,3,4,5]
arr2 = [1,2,3,4,5,6,7]

ans = union_of_2_sorted_arr(arr1,arr2)
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

def union_2_sorted_arr(arr1, arr2):
    s = set()
    s.update(arr1)
    s.update(arr2)

    union = list(s)

    return union

arr1 = [1, 1, 2, 3, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7]

ans = union_2_sorted_arr(arr1, arr2)
print(ans)

print()

# 2.optimal sol : tc = o(n) + o(m)  ~>  o(m+n)
                # sc = o(m+n)
                # but sc = o(1) if union[ ] ka space not cnsider

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




