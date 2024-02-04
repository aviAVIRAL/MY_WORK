# Example 1:
# Input: 18
# Output: Abundant Number
# Explanation: Divisors of 18 are 1,2,3,6,9. 1+2+3+6+9=21, Since 21 is greater than 18, 18 is an abundant number.

# Example 2:
# Input: 21
# Output: Not Abundant Number
# Explanation:Divisors of 21 are 1,3,7. 1+3+7=11, Since 11 is smaller than 21, 11 is not an abundant number.



def f(n):

    x = n
    sum = 0
    
    for i in range(1 , n):
        if n % i == 0 :
            sum += i 

    if sum > x :
        return True
    else: 
        return False
   
    
if __name__=="__main__":
    n = 18 
    print(f(n))


    
