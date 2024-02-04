# Find LCM of two numbers
# Problem Statement: Find lcm of two numbers.

# Examples:

# Example 1:
# Input: num1 = 4,num2 = 8
# Output: 8


# Example 2:
# Input: num1 = 3,num2 = 6
# Output: 6



# # m 1 brute 

if __name__ == '__main__':
    
    a = 4
    b = 8
    
    gcd = 1
    
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    lcm = (a * b) / gcd


    print(lcm)

# m 2 optimal ecliden algo  
   
 
def f(a , b):
    
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
    
    a = 8 
    b = 4
    gcd = f(a , b)
    
    lcm = (a*b) / gcd
    print(lcm)