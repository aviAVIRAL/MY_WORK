# Find GCD of two numbers
# Problem Statement: Find the gcd of two numbers.

# Examples
# Example 1:
# Input: num1 = 4, num2 = 8
# Output: 4
# Explanation: Since 4 is the greatest number which divides both num1 and num2.

# Example 2:
# Input: num1 = 3, num2 = 6
# Output: 3
# Explanation: Since 3 is the greatest number which divides both num1 and num2.



# # m 1 brute 

if __name__ == '__main__':
    
    a = 4
    b = 8
    
    gcd = 1
    
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    print(gcd)

# m 2 optimal ecliden algo  
    
def GCD(a , b):
    
    gcd = 1

    while( a > 0 and b > 0 ):
        if a > b :
            a = a % b
        else :
            b = b % a 
        
    if a == 0 :
        gcd = b 
    else:
        gcd = a 

    return gcd 
    
if __name__=="__main__":
    print(GCD(52 , 10))


