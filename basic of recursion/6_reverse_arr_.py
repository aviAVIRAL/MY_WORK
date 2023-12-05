# reverse the arr 

# by using two pointer
# m-1
# representation - 1 

def f(arr, l, r):
    if l >= r:
        return arr     # leed code type rep  
    arr[l], arr[r] = arr[r], arr[l]
    f(arr, l + 1, r - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    
    f(arr, 0, n - 1)

    print(arr)

# m-1
# rep - 2   

def f(arr, l, r):
    if l >= r:
        print(arr)    # print statment
        return
    arr[l], arr[r] = arr[r], arr[l]

    f(arr, l+1, r-1)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    n= len(arr)
    f(arr, 0, n-1)

# m-2
# by using One pointer

def f(arr, i):
    if i >= n / 2:
        return arr
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    f(arr, i + 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    f(arr, 0)
    print(arr)


# m-3
# simple methoud { No use of recursion} 

def f(arr):
    n = len(arr)
    i = 0
    r = n - 1 
    while i <= r:
        arr[i], arr[r] = arr[r], arr[i]
        i += 1
        r -= 1    
    return arr   

if __name__=="__main__":

    arr = [ 1, 2, 3, 4 ]
    f(arr)
    print( arr )


# or 

# if __name__=="__main__":

#     arr = [ 1, 2, 3, 4 ]
#     print(f(arr))

# or

# if __name__=="__main__":

#   arr = [ 1, 2, 3, 4, 5 ]
#   Result = f(arr)
#   print( Result )

