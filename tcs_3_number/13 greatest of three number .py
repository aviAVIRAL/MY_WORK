
# Greatest of three numbers
# Problem Statement: Given three numbers. Find the greatest of three numbers.

# Examples:

# Example 1:
# Input: 1 3 5
# Output: 5
# Explanation: Answer is 5.Since 5 is greater than 1 and 3.



# m1

# max ( a , b , c)

# m2 

num1 = 1
num2 = 3
num3 = 5

if num1 > num2 and num1 > num3:
    print("The greatest of the three numbers is", num1)
elif num2 > num1 and num2 > num3:
    print("The greatest of the three numbers is", num2)
else:
    print("The greatest of the three numbers is", num3)



