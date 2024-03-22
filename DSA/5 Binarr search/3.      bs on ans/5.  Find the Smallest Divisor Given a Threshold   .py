# Find the Smallest Divisor Given a Threshold
# Problem Statement: You are given an array of integers ‘arr’ and an integer i.e. a threshold value ‘limit’. Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division’s result is less than or equal to the given threshold value.

# Examples
# Example 1:
# Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
# Result: 3
# Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
# The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

# Example 2:
# Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
# Result: 2
# Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.



# Point to remember:


# While dividing the array elements with a chosen number, we will always take the ceiling value. And then we will consider their summation. For example, 3 / 2 = 2.



# brute   by avi 

import math

def  pos(arr,div,t):    
    tot = 0 
    for i in range(len(arr)):
        tot += math.ceil(arr[i]/div)
    if tot <= t:
        return True 
    else : 
        return False 

def f(arr,t):
    for i in range(min(arr), max(arr)+1):
        if  ( pos(arr,i,t) == True ):  # if (  pos(arr,m,t) ):
            return i 
    return -1 

if __name__=="__main__":
    arr = [1,2,5,9]
    t = 6 
    print(f(arr,t))

# optimal   by avi 
    
import math

def  pos(arr,div,t):
    tot = 0 
    for i in range(len(arr)):
        tot += math.ceil(arr[i]/div)
    if tot <= t:
        return True 
    else : 
        return False 

def f(arr,t):

    if len(arr) > t:
        return -1
    
    l = min(arr)
    h = max(arr)
    while l<=h:
        m = (l+h)//2

        if  ( pos(arr,   m   ,t) == True ): 
            h = m - 1
        else:
            l = m + 1
        
    return l 
    

if __name__=="__main__":
    arr = [1,2,5,9]
    t = 6 
    print(f(arr,t))

# # ......................................................
# import math

# def smallestDivisor(arr, limit):
#     n = len(arr)  # size of array
#     maxi = max(arr)
#     # Find the smallest divisor
#     for d in range(1, maxi+1):
#         # Find the summation result
#         sum = 0
#         for i in range(n):
#             sum += math.ceil(arr[i] / d)
#         if sum <= limit:
#             return d
#     return -1

# arr = [1, 2, 3, 4, 5]
# limit = 8
# ans = smallestDivisor(arr, limit)
# print("The minimum divisor is:", ans)

# optimal


import math

def sumByD(arr, div):
    n = len(arr)  # size of array
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisor(arr, limit):
    n = len(arr)
    
    if n > limit:
        return -1
    
    low = 1
    high = max(arr)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)








