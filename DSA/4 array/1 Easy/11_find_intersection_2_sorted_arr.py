# 1.  brute forces   tc = o(n*m)    sc = o(m)

#    a , b , c   => arr hai 


def intersection_withoutdublicate(a, b):
    temp = []
    vist =[0]*len(b)

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and vist[j] == 0 :
                temp.append(b[j])
                vist[j] = 1 
                break
            if a[i] < b[j] :
                break
    return temp

a = [1,2,2,3,3,4,6,7]
b = [2,3,3,5,6,7,8]
ans = intersection_withoutdublicate(a,b)
print(ans)



# LeedCode: -
# # # intersection using set data struture 

# # set :- correct indexing ordering ki no gurantee

# # therfor not good practices 

# def intersection_2_sorted_arr(a, b):

  
#     x=set(a) 
#     y=set(b)
#     ans = x.intersection(y)
#     return ans
 
# a = [1,2,2,3,3,4,5,6,7]
# b = [2,3,3,5,6,6,7]
# ans = intersection_2_sorted_arr(a, b)
# print(ans)

# # union using set data struture 

# # set :- correct indexing ordering ki no gurantee

# def union_of_2_sorted_arr(a, b):

#     x=set(a) 
#     y=set(b)
#     ans = x.union(y)
#     return ans
 
# a = [1,2,2,3,3,4,5,6,7]
# b = [2,3,3,5,6,6,7,8,9,99]
# ans = union_of_2_sorted_arr(a, b)
# print(ans)


# print("next")

# def ins(arr1,arr2):

#     c=[]
#     for i in range (len(arr1)):
#         for j in range (len(arr2)):
#             if arr1[i] == arr2[j]:
#                 c.append(arr2[j])
#     ans = set(c)
#     return ans 
# arr1 = [1,2,2,3,3,4,5,6,7]
# arr2 = [2,3,3,5,6,6,7,8,9,99]
# ans = ins(arr1, arr2)
# print(ans) 
# ...................................
# concept : -
#     only for  set data structure :~
#     set1 && set2 } && represent intersecion
# ...................................



# optimal solution : tc = o(n + m)  # sc = o(1) 
                                    # sc = o(n + m) to stored and return

def intersection_of_two_sorted_arr(a,b):
    c = []
    i = 0 
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1 
        elif b[j] < a[i]:
            j += 1
        else:
            a[i] == b[j]
            c.append(a[i])
            i += 1
            j += 1
    return c

a = [1,2,2,3,3,4,6,7]
b = [2,3,3,5,6,7,8]
ans = intersection_of_two_sorted_arr(a,b)
print(ans)



