
# Count digits in a number
# Problem Statement: Given an integer N, write a program to count the number of digits in N.

# Examples
# Example 1:
# Input: N = 12345
# Output: 5
# Explanation: N has 5 digits


# m1 

def f(n):

    count = 0
    x = n
    while( x != 0 ):   # or  while( x >  0 ):
            x//=10
            count+=1
    return count

if __name__=="__main__":
        
    n = 876
    print(f(n)) 


# m 2 trick 

def f(n):

    x = str(n)
    ans = len(x)
    
    return ans

if __name__=="__main__":
        
    n = 876
    print(f(n)) 



