print()
print( )
# print( ).................................


def intersection_of_two_sorted_arr(a,b):
    temp = []
    i = 0 
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1 
        elif b[j] < a[i]:
            j += 1
        else:
            a[i] == b[j]
            temp.append(a[i])
            i += 1
            j += 1
    return temp

a = [1,2,2,3,3,4,6,7]
b = [2,3,3,5,6,7,8]
ans = intersection_of_two_sorted_arr(a,b)
print(ans)



N = 3
summation = (N * (N + 1)) // 2
print(summation)