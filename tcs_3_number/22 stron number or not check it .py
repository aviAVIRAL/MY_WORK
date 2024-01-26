
# Check if a number is a Strong Number or not
# Problem Statement: Given an integer Print “YES” if it is a strong number else print “NO”.

# Note : 

# When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 
# Strong number is also known as Krishnamurthi number/Peterson Number.
# Examples:

# Examples 1:
# Input: N = 145
# Output: Yes
# Explanation: 1! + 4! + 5! = 145. Hence 145 is a strong number. 

# Example 2:
# Input:  26
# Output: No
# Explanation: 2! + 6! = 722. Hence 26 is not a strong number.

def Factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res  

def f(x):
    original_x =  x
    sum = 0 
    while x > 0 :  
        d = x % 10     
        sum += Factorial(d)
        x = x//10
        
    return sum == original_x   # imp 

if __name__=="__main__":
    k  = 145
    if f(k):
        print(True) 
    else :
        print(False) 
    













