# Kadane’s Algorithm : Maximum Subarray Sum in an Array
# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# Examples
# Example 1:

# Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

# Output: 6 

# Explanation: [4,-1,2,1] has the largest sum = 6. 

# Examples 2: 

# Input: arr = [1] 

# Output: 1 

# Explanation: Array has only one element and which is giving positive sum of 1. 


# brute 
def maxSubarraySum(arr):
    maxi = float('-inf')  # maximum sum

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for k in range(i, j + 1):
                sum += arr[k]
                maxi = max(maxi, sum)

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = maxSubarraySum(arr)
print("The maximum subarray sum is:", maxSum)


# better
def maxSubarraySum(arr):
    maxi = float('-inf')  # maximum sum

    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            # current subarray = arr[i.....j]

            # add the current element arr[j]
            # to the sum i.e. sum of arr[i...j-1]
            sum += arr[j]

            maxi = max(maxi, sum)  # getting the maximum

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = maxSubarraySum(arr)
print("The maximum subarray sum is:", maxSum)
# ..............................................

#      concept 

# error in code 
arr = [ 1, 9, 10, -30, 5, 1 , -100]
maxi = -1
temp =  [] 
n = len(arr)
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += arr[j]
        if sum > maxi :
            maxi = max(maxi, sum )
            temp.append(arr[i:j+1]) #  see here 
print( maxi) # every time we append so many subarr come 
print(temp)
print()
# print()
# 20  maximum summation aaraha hai
# [[1], [1, 9], [1, 9, 10]] many subarry 

# correct code 
arr = [1, 9, 10, -30, 5, 1 , - 100]

maxi = -1
subarr = []
n = len(arr)
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        if sum > maxi:
            maxi = sum
            subarr = arr[i:j+1] # see here  
print( maxi) # variable mein store and update 
print(subarr)

# op 
# 20  maxi summation
# [1, 9, 10]  maxi summation that subarry 
    

# ...................................
# optimal  kadan algo    tc = 0(n)  sc = 0(1)

def maxSubarraySum(arr):
    maxi = float('-inf')  # maximum sum
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = maxSubarraySum(arr)
print("The maximum subarray sum is:", maxSum)


# .................................................
# followed up quetion ki  vo subarr bee return kr

def maxSubarraySum(arr):
    maxi = float('-inf')  # maximum sum
    sum = 0

    start = 0
    ansStart = -1
    ansEnd = -1

    for i in range(len(arr)):
        if sum == 0:
            start = i  # starting index

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        if sum < 0:
            sum = 0

    # Printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = maxSubarraySum(arr)
print("The maximum subarray sum is:", maxSum)


