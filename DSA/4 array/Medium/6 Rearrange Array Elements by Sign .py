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
print(" Varirty 1 : equal +vs -ve ")

# brute  by Avi  tc = 0(n + n)   sc =  0(n)

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
    n = len(arr)
    pos = []
    neg = []
  
    for i in range(n):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
  
    for i in range(n//2):  # imp  
        arr[2 * i] = pos[i]
        arr[2 * i + 1] = neg[i]
  
    return arr

if __name__=="__main__":
    arr = [1,2,-4,-5]
    k = f(arr)

    for x in k:
        print(x, end = " ")
    print()

# optimal   tc = 0(n) sc = 0(1)
    
def f(arr): 
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
if __name__=="__main__":
    arr = [1,2,-4,-5]
    k = f(arr)
    for x in k:
        print(x, end = " ")
    print()

# ........................
# variety 2 : not same pos n neg el

# Example 1:

# Input:
# arr[] = {1,2,-4,-5,3,4}, N = 6
# Output:
# 1 -4 2 -5 3 4

# Explanation: 

# Positive elements = 1,2
# Negative elements = -4,-5
# To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.
# Leftover positive elements are 3 and 4 which are then placed at the end of the array.

# Example 2:
# Input:
# arr[] = {1,2,-3,-1,-2,-3}, N = 6
# Output:
# 1 -3 2 -1 3 -2
# Explanation: 

# Positive elements = 1,2
# Negative elements = -3,-1,-2,-4
# To maintain relative ordering, 1 must occur before 2.
# Also, -3 should come before -1, and -1 should come before -2.
# After alternate ordering, -2 and -4 are left, which would be placed at the end of the ans array.
print(" Varirty 2 : unequal +vs -ve ")

print()
def RearrangebySign(arr, n):
    pos = []
    neg = []
    
    for i in range(n):
        if arr[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
    
    if len(pos) < len(neg):
        for i in range(len(pos)):
           arr[2*i] = pos[i]
           arr[2*i+1] = neg[i]

        k = len(pos)*2
        for i in range(len(pos), len(neg)):
            arr[k] = neg[i]
            k += 1
    

    else:
        for i in range(len(neg)):
           arr[2*i] = pos[i]
           arr[2*i+1] = neg[i]
        
        k = len(neg)*2
        for i in range(len(neg), len(pos)):
            arr[k] = pos[i]
            k += 1
    
    return arr

# Array initialization
n = 6
A = [1, 2, -4, -5, 3, 4]

ans = RearrangebySign(A, n)

for i in range(len(ans)):
    print(ans[i], end=" ")



