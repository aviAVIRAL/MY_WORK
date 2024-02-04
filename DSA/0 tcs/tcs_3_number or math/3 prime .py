# Check if a number is prime or not
# Problem Statement: Given a number, check whether it is prime or not. A prime number is a natural number that is only divisible by 1 and by itself.

# Examples 1 2 3 5 7 11 13 17 19 …

# Examples
# Example 1:
# Input: N = 3
# Output: Prime
# Explanation: 3 is a prime number

# Example 2:
# Input: N = 26
# Output: Non-Prime
# Explanation: 26 is not prime


# r2


def f(n):

    if n < 2 : 
        return False

    for i in range(2, n): #imp n+1 do use it 
        if n % i == 0 :
            return False
    return True

if __name__=="__main__":
    n = 11  # n = int ( input ( "enter number") ) 
    sol = f(n)

    if sol == True :
        print("prim hai")
    else:
        print("prim Nahi hai")


print()
print()

# r1 

def f(n):
    for i in range(2, n): #imp n+1 do use it 
        if n % i == 0 :
            return False
    return True

if __name__=="__main__":
    n = 11
    sol = f(n)

    if n != 1 and sol == True :
        print("prim hai")
    else:
        print("prim Nahi hai")


print()




