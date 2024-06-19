# Finding Sqrt of a number using Binary Search
# Problem Statement: You are given a positive integer n. Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of ‘sqrt(n)’.

# Note: The question explicitly states that if the given number, n, is not a perfect square, our objective is to find the maximum number, x, such that x squared is less than or equal to n (x*x <= n). In other words, we need to determine the floor value of the square root of n.

# Examples
# Example 1:
# Input Format: n = 36
# Result: 6
# Explanation: 6 is the square root of 36.

# Example 2:
# Input Format: n = 28
# Result: 5
# Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5.


# brute linear search  

def f(n):
    for i in range(1, n):
        if i*i == n :
            break
    return i  

def floorSqrt(n):
    ans = 0
    # Linear search on the answer space:
    for i in range(1, n+1):
       
        if i*i <= n:   # ip    n = 26     op ~ 5
            ans = i  
        else:
            break      # i * i > 26 to break 
    return ans
if __name__=="__main__":
    n = 25 
    print(floorSqrt(n))

# optimal   using build in function 
# m1 tc O(1)  sc O(1)
import math
n = 26
ans = math.sqrt(n)   # Using sqrt() function

print(ans)       # op  5.0990195135   float value   
print(int(ans))  # op  5              int value     
# r2

from math import sqrt as r
n = 25 
ans = r(n)
print(ans)

# m2   tc O(1)  sc O(1)
n = 25
ans = n ** 0.5
print( ans)

# optimal binary search  tc log n    sc 1 

# binary search by avi 

def f(n): 
    l, h = 1 , n-1 
    ans = 0 
    while (l <= h):
        m = ( l + h )//2
        if m*m <= n :
            ans = m  
        
        if m*m > n  :
            h = m - 1
        else :
            l = m + 1
    
    return ans  

n = 26 
print(f(n))

