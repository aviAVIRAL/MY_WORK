# Nth Root of a Number using Binary Search
# Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the ‘nth root is not an integer, return -1.

# Examples
# Example 1:
# Input Format: N = 3, M = 27
# Result: 3
# Explanation: The cube root of 27 is equal to 3.

# Example 2:
# Input Format: N = 4, M = 69
# Result: -1
# Explanation: The 4th root of 69 does not exist. So, the answer is -1.



# brute linear search

# brute 
def f(n):
    ans = 0
    # Linear search on the answer space:
    for i in range(1, n+1):
       
        if i*i*i == n:   #
            ans = i  
            return ans
    return -1
if __name__=="__main__":
    n = 27 
    print(f(n))

# optimal
def fun(n): 
    l, h = 1 , n-1 
    ans = 0 
    while (l <= h):
        m = ( l + h )//2

        if m*m*m == n :
            ans = m 
            return ans 
        
        if m*m*m > n  :
            h = m - 1
        else :
            l = m + 1
    
    return -1  

n = 27 
print(fun(n))

# .............REP ................


def f(n, x):
    l, h = 1, n
    ans = 0
    while (l <= h):
        m = (l + h) // 2
        if m**x > n:
            h = m - 1
        else:
            ans = m
            l = m + 1
# I M P    concept    to     write 
    if ans**x == n: return ans 
    else : return -1              
    
print(f(27, 3))   # OP 3
print(f(89, 3))   # OP -1 
 


 
