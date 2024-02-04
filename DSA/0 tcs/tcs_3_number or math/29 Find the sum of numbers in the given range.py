
# Find the sum of numbers in the given range
# Problem Statement: Find the sum of numbers in the given range.

# Examples:

# Example 1:
# Input: l=2, r=7
# Output: 27
# Explanation: 2+3+4+5+6+7=27. Therefore 27 is the answer.

# Example 2:
# Input: l=5, r=9
# Output: 35
# Explanation: 5+6+7+8+


def f(n,m):
   
    sum = 0
    
    for i in range(n , m+1):
        sum += i 
    return sum 
   
if __name__=="__main__":
     
    print(f(2  , 7 ))


    
