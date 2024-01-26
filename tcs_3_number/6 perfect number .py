# Check whether a number is Perfect Number or not
# Problem Statement: Perfect Number. Write a program to find whether a number is a perfect number or not.

# A perfect number is defined as a number that is the sum of its proper divisors ( all its positive divisors excluding itself). 

# Examples:

# Example 1:
# Input: n=6
# Output: 6 is a perfect number

# Example 2:
# Input: n=15
# Output: 15 is not a perfect number

# Example 3:
# Input: n=28
# Output: 28 is a perfect number
# Reason:
# For 6 and 28 , the sum of their proper divisors (1


def f(n):
    orig = n
    s = 0
    
    for i in range(1, n):
        if n%i == 0:
            s += i
    return orig == s
    
    # if orig == s :
    #     return True
    # else:
    #     False

if __name__=="__main__":
    n = 28 
    if f(n):
        print("yes")
    else:    
        print("no")


