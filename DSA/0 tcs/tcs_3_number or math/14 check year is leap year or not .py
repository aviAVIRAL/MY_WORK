
# Check if given year is a leap year or not
# In this post we will solve the problem “Check if given year is a leap year or not”.

# Problem Statement: Check if the given year is a leap year or not.

# Examples:

# Example 1:
# Input: 1996
# Output: Yes
# Explanation: Since 1996 is a leap year answer is “Yes”.


# : A year is a leap year only if it satisfies the following condition.

# The year is divisible by 400
# The year is divisible by 4 but not by 100


# r 1 


def f(year):
    
    if year % 4 == 0 and year % 100 != 0 :
        return True
    
    elif  year % 400 == 0 : 
        return True
    
    else: 
        return False

if __name__=="__main__":
        
    year = 1996

    if f(year):
        print("Yes")
    else:
        print("No")


# r 2

def f(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__=="__main__":
        
    year = 1996

    if f(year):
        print("Yes")
    else:
        print("No")












