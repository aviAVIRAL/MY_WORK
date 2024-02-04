# input  = [    1, 2, 3, 4, 5    ]
# output = [10, 1, 2, 3, 4, 5    ]



# add element in first position 

def f ( arr ): 
    n = len (arr)
    arr.append( 0 )

    for i in range(n-1 , -1 , -1 ):
        arr[i+1] = arr[i]
    
    arr[0] = 10 

    return arr 

if __name__=="__main__":
    arr = [ 1,2,3,4,5]
    print(f(arr))


print( )
# print( ).................................

def f ( arr ): 
    n = len (arr)

    arr.append( 0 )

    for i in range ( n- 1 ,-1 , -1 ):
        arr[i+1] = arr[i]
    
    arr[0] = element  

    return arr 

if __name__=="__main__":
    arr = [ 1,2,3,4,5]

    element  = int(input( " enter the elm : "))

    print(f(arr))
    