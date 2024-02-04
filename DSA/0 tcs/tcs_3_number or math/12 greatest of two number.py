
# Greatest of two numbers
# Problem Statement: Given two numbers. Find the greatest of two numbers.

# Examples:

# Example 1:
# Input: 1 3
# Output: 3
# Explanation: Answer is 3,since 3 is greater than 1.

# Input: 1.123  1.124
# Output: 1.124
# Explanation: Answer is 1.124,since 1.124 is greater than 1.123.



# m1

num1 = 1
num2 = 3
print("The greatest of the two numbers is", max(num1, num2))


# m2

num1 = 1.123
num2 = 1.124

if num1 < num2:
    print("The greatest of the two numbers is", num2)
else:
    print("The greatest of the two numbers is", num1)





