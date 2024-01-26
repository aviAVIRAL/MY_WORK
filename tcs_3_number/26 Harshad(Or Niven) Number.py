
# Check if the given number is Harshad(Or Niven) Number
# Problem Statement: Check if the number is a Harshad(or Niven) number or not.

# Examples:

# Example 1:
# Input: 378
# Output: Yes it is a Harshad number.
# Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number 
    
def f(n):

    x = n    # imp or  original_n = n 
    sum = 0
    while (n> 0):
        d = n%10 
        sum += d
        n = n//10 

    if x % sum == 0 :   # imp  or  original_n % sum == 0 : 
        return True
    else: 
        return False
   
    
if __name__=="__main__":
    n = 378 
    print(f(n))


    
