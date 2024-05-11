# Find all Palindrome Numbers in a given range
# Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

# Note: A palindromic number is a number that remains the same when its digits are reversed.OR  a palindrome is a number that reads the same forward and backward Eg: 121,1221, 2552

# Examples:

# Example 1:
# Input: min = 10 , max = 50
# Output: 11 22 33 44 
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.


def f(n):
    y = 0
    x = n
    while x > 0:
        y = y * 10 + x % 10
        x = x // 10
    return n == y

if __name__ == "__main__":
    min_val = 100
    max_val = 150
    
    for i in range(min_val, max_val + 1):
        if f(i):
            print(i, end=" ")

# /.....
    # r 2

def f(n):
    y = 0
    x = n
    while x > 0:
        y = y * 10 + x % 10
        x = x // 10

    return n == y

def count_pal(min_val, max_val):
    for i in range(min_val, max_val + 1):
        if f(i):
            print(i, end=" ")

if __name__ == "__main__":
    count_pal(100, 2000)


# trick 

def f(n):
    st = str(n)
    brr = st[::-1]
    if st == brr:
        return True 
    else:
        return False
    # y = 0
    # x = n
    # while x > 0:
    #     y = y * 10 + x % 10
    #     x = x // 10
    # return n == y

if __name__ == "__main__":
    min_val = 100
    max_val = 150
    
    for i in range(min_val, max_val + 1):
        if f(i) == True:
            print(i, end=" ")

