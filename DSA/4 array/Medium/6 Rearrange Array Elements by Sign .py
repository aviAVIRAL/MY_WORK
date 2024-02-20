# Rearrange Array Elements by Sign
# Variety-1

# Problem Statement:

# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Note: Start the array with positive elements.

# Examples: 

# Example 1:

# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5

# Explanation: 

# Positive elements = 1,2
# Negative elements = -4,-5
# To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

# Example 2:
# Input:
# arr[] = {1,2,-3,-1,-2,-3}, N = 6
# Output:
# 1 -3 2 -1 3 -2
# Explanation: 

# Positive elements = 1,2,3
# Negative elements = -3,-1,-2
# To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
# Also, -3 should come before -1, and -1 should come before -2.


# ........................
# variety 1 : same pos n neg el

# brute  by Avi  tc = 0(2n)   sc =  0(n)

def f(arr, n):
    pos = []
    neg = []

    for x in arr: 
        if x > 0: 
            pos.append(x)
        else: 
            neg.append(x)
    
    j = 0 
    for i in range(0, n, 2):
        arr[i] = pos[j]
        j += 1

    k = 0 
    for i in range(1, n, 2):
        arr[i] = neg[k]
        k += 1
    
    return arr 

if __name__=="__main__":
    arr = [1,2,-4,-5]
    k = f(arr,len(arr))

    for x in k:
        print(x, end = " ")
    print()

# brut by Striver 
    
# Time Complexity: O(N+N/2) { O(N) for traversing the array once for segregating positives and negatives and another O(N/2) for adding those elements alternatively to the array, where N = size of the array A}.

# Space Complexity:  O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.

def f(arr):
    pos = []
    neg = []
  
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
  
    for i in range(len(pos)):
        arr[2 * i] = pos[i]
    for i in range(len(neg)):
        arr[2 * i + 1] = neg[i]
  
    return arr

if __name__=="__main__":
    arr = [1,2,-4,-5]
    k = f(arr,len(arr))

    for x in k:
        print(x, end = " ")
    print()

# optimal   tc = 0(n) sc = 0(1)
    
def RearrangebySign(arr): 
    n = len(arr)
    
    temp = [0] * n
    
    posIndex, negIndex = 0, 1
    
    for i in range(n):
        
        if arr[i] < 0:
            temp[negIndex] = arr[i]
            negIndex += 2
        
        else:
            temp[posIndex] = arr[i]
            posIndex += 2
    
    return temp
    
# Test the function
A = [1,2,-4,-5]
ans = RearrangebySign(A)
print(ans)

# ........................
# variety 2 : not same pos n neg el
 
