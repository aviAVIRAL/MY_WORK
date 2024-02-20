
# Maximum Product Subarray in an Array
# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

# Examples
# Example 1:
# Input:
#  Nums = [1,2,3,4,5,0]
# Output:
#  120
# Explanation:
#  In the given array, we can see 1×2×3×4×5 gives maximum product value.


# Example 2:
# Input:
#  Nums = [1,2,-3,0,-4,-5]
# Output:
#  20
# Explanation:
#  In the given array, we can see (-4)×(-5) gives maximum product value



# brute   tc = o(n^3)

def f(arr):
    n = len(arr)

    maxi = - float( " inf ")

    for i in range(0, n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j + 1):
                prod = prod * arr[k]
                maxi = max ( prod, maxi )

    return maxi

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


# 3 optimal tc 0(n) sc 0(1)


def maxProductSubArray(arr):
    n = len(arr) 

    pre = 1
    suff = 1

    maxi = float('-inf')
    
    for i in range(n):
        
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1

        pre *= arr[i]    #    pre = pre * arr[i]
        suff *= arr[n - i - 1]
        maxi = max(maxi, max(pre, suff))

    return maxi

arr = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray is:", maxProductSubArray(arr))


    
    
