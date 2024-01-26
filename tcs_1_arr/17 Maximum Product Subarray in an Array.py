# Input:
#  Nums = [1,2,-3,0,-4,-5]
# Output:
#  20

# brute   tc = o(n^3)

def f(arr):
    n = len(arr)

    maximum = - float( " inf ")

    for i in range(0, n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j + 1):
                prod = prod * arr[k]
            maximum = max ( prod, maximum )

    return maximum

if __name__ == "__main__":
    arr = [2, 3, 0, 4 ]
    print(f(arr))

# output  6 


# better   tc = o(n^2)
    

def f(arr):
    n = len(arr)

    maximum = - float( " inf ")

    for i in range( 0, n ):
        prod = 1
        for j in range( i, n ):
            prod = prod * arr[ j ]
            maximum = max ( prod, maximum )

    return maximum

if __name__ == "__main__":
    arr = [2, 3, 0, 4 ]
    print(f(arr))


# optimal struver video :- 
    
    
