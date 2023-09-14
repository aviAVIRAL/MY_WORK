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







