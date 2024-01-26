# January 4, 2022 Data Structure / Maths
# Maximum and Minimum Digit in a Number
# Problem Statement: Given a number N, print the smallest and largest digits present in the number.

# Examples:

# Example 1:
# Input: N = 2746
# Output: Largest digit: 7
#         Smallest digit: 2
# Explanation: By simply going through the digits of 
# the number, we figure out the largest and smallest 
# digit in the number.


print()

# r1
def min_max(n):
    mini = float('inf')
    maxi = float('-inf')
    
    while n != 0:
        d = n % 10
        mini = min(mini, d)
        maxi = max(maxi, d)
        n = n // 10
    
    print( mini , maxi)    # imp automatically standard space 

if __name__ == "__main__":
    number = 4726
    min_max(number)


print()
# r2 
def f(n):
    mini = float('inf')
    maxi = float('-inf')
    
    while n != 0:
        d = n % 10
        mini = min(mini, d)
        maxi = max(maxi, d)
        n = n // 10
    
    print(f"{mini} ,,//,, {maxi}")  # imp space decide by me 

if __name__ == "__main__":
    number = 4726
    f(number)












