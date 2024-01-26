

# Replace all the 0’s with 1 in a given integer
# Problem Statement: You are given an integer. Your task is to replace all the zeros in the integer with ones.

# Examples:

# Example 1:
# Input: N = 102003
# Output: 112113
# Explanation: The 2nd,4th and 5th position from left contain 0.The resultant integer has replaced the 0’s in those  positions with 1.



def f(n):
    y = 0
    while n > 0:
        d = n % 10
        if d == 0 :
            d = 1 
        y = y * 10 + d
        n = n // 10
    return y


if __name__ == "__main__":

    print( f(307) )
#     o/p = 713   # problem reverse aa raha hai 
 
    # ..........................
   
#  trick 
    
def f(n):
    y = 0
    while n > 0:
        d = n % 10
        if d == 0 :
            d = 1 
        y = y * 10 + d
        n = n // 10
    
    ans = str(y)
    return ans[::-1]   # impo 


if __name__ == "__main__":

    print( f(307) )
    # o/p =  317

