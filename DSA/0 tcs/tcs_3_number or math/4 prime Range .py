# Range :  Prime Numbers in a given range
# Problem Statement: Given a and b, find prime numbers in a given range [a,b], (a and b are included here).

# Examples:

# Examples:
# Input: 2 10
# Output: 2 3 5 7 
# Explanation: Prime Numbers b/w 2 and 10 are 2,3,5 and 7.

# Example 2:
# Input: 10 16
# Output: 11 13 
# Explanation: Prime Numbers b/w 10 and 16 are 11 and 13.



print()
print()

#  r1 

def f1 (n):
    
    if n == 1:   # or if n < 2 :
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def funct2 (min , max):
    for i in range(min , max + 1):
        if f1 (i) :       # or   if f1 (i) == True :
            print(i, end=" ")

if __name__ == "__main__":
    
    min , max = 11, 17
    funct2 (min , max)


# op = 11 13 17























