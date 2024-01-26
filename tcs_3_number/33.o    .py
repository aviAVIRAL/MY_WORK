

# appne aap invente problem hai 
# Examples:

# Example 1:
# Input : N = 74
# Output : True . 
# Explanation: 74 can be expressed as 71 + 3 and both are prime numbers. 

#  ...........
# appne aap 


def f1 (n):
    
    if n == 1:   # or if n < 2 :
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def funct2(z):
    arr = []     # z = individual hai to problem nhi ayi arr mein dalne mein   
    for i in range(2 , z ):
        if f1 (i) :       # or   if f1 (i) == True :
            arr.append(i)   
   
    for x in arr : 
        for y in arr: 
            if x + y == z :
                return True
 
    return False 
        

if __name__ == "__main__":
    
    z = 74
    print(funct2(z))









