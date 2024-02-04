# alculate the Power of a Number : Binary Exponentiation
# Problem Statement: Find the Power of a number.

# Examples:

# Example 1:
# Input: N = 5, k=3
# Output: 125
# Explanation: Since 5*5*5 is 125.


# m1

n = 5
x = 3
print( pow(n , x)  )


# m2

n = 5
x = 3
ans = 1

for i in range(1 , x+1):
    ans = ans * n

print(f"{n} raised to the power {x} is {ans}")


