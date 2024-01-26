# Check if a number is Palindrome or Not
# Problem Statement:  Given a number check if it is a palindrome.

# An integer is considered a palindrome when it reads the same backward as forward.

# Examples:

# Example 1:
# Input: N = 123
# Output: Not Palindrome Number
# Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.


# r 1 
def f(X):
    Y = 0
    while X > 0:
        digit = X % 10
        Y = Y * 10 + digit
        X = X // 10
    return Y


if __name__ == "__main__":
    X = 121
    dummy = X
    Y = f(X)
    if dummy == Y:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")



# r 2

def f(X):

    Y = 0

    while X > 0:
        
        Y = Y * 10 + X % 10
        X = X // 10

    return Y


if __name__ == "__main__":
    X = 121
    dummy = X
    Y = f(X)
    if dummy == Y:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")












