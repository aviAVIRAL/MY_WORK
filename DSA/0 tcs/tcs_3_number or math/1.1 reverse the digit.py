# Reverse digits of a number
# Problem Statement: Given an integer. Write a program to reverse digits of a number.

# Examples:

# Example 1:
# Input: N = 472
# Output: 274
# Explanation: Reading the number from back to front, we see that the output should be 274

# m1 
def f(X):
    Y = 0
    while X != 0:  # while X :
        digit = X % 10
        Y = Y * 10 + digit
        X = X // 10
    return Y


if __name__ == "__main__":
   x = 123 
   print( f"{x} reverse is -> ", f(x))


# ..................
   
# m2 trick int -> string 
   
n = 123 

st = str(n)

y = st[::-1]

i = int(y)

print(i)

# ...................
# # rule 
# 7 % 10 is 7   : 10 se niche ka number hai 
# 7 // 10 is 0   : 10 se niche ka number hai 






