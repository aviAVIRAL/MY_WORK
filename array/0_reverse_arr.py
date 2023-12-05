# reverse arr  without recursion 
# i/p = arr = [ 1, 2, 3, 4 ]
# 0/p = arr =  [4, 3, 2, 1]

# m- 1
# simple methoud with logic 

def reverse_func(arr):
    n = len( arr)
    i = 0
    r = n - 1 
    while i <= r:
        arr[i], arr[r] = arr[r], arr[i]
        i += 1
        r -= 1    
    return arr  

if __name__=="__main__":

    arr = [ 1, 2, 3, 4 ]
    reverse_func(arr)
    print( arr )

# or

# if __name__=="__main__":
 
#     arr = [ 1, 2, 3, 4, 5 ]
#     Result = reverse_func(arr)
#     print( Result )


# or 

# if __name__=="__main__":

#     arr = [ 1, 2, 3, 4 ]
#     print(reverse_func(arr))

# .....................................

# m-2 
# python build in function

    arr = [1, 2, 3, 4, 5, 6, 7]

    arr.reverse()

    print(arr)

# m-3
# python build in function

    arr = [1, 2, 3, 4, 5, 6, 7]

    reversed_arr = arr[::-1]

    print(reversed_arr)
  

