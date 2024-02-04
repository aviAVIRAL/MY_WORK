

# important unnique quetion : 


# Print all Prime Factors of the given number

# Problem Statement: Given a number n. Print all Prime Factors of the given number n.

# Examples:

# Example 1:
# Input: N = 12
# Output: 2,2,3
# Explanation: These are the prime factors of 12.

# Example 2:
# Input: N = 36
# Output: 2,2,3,3
# Explanation: These are the prime factors of 36.



# imp concept  r1 

def f( n):
    
    i = 2
    while n > 1 :

        if n % i == 0:
            
            while n % i == 0:
                print(i, end=" ")
                n = n // i

        i += 1

if __name__ == "__main__":
    n = 60
    f(n)


print()
# r2 
def f(n):
    for i in range(2, n + 1):
        if n % i == 0:
            while n % i == 0:
                print(i, end=" ")
                n = n // i

if __name__ == "__main__":
    n = 60
    f(n)


print()


