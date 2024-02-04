# Find Sum of AP Series
# Example 1:
# Input:
# n=4
# a=2
# d=2
# Output: 20
# Explanation: 2+4+6+8 = 20

# ..................

# m1  use  for loop 

def f(a, d, n):

    s = 0

    for i in range(1, n + 1):   # imp
        s += a
        a += d

    return s

if __name__ == "__main__":
    a = 1
    d = 2
    n = 5
    print("Sum of Given AP Series:", f(a, d, n))



# m2  direct formula 
    

def sum_of_ap(a, d, n):

    return (n / 2) * (2 * a + (n - 1) * d)

if __name__ == "__main__":
    a = 1.5
    d = 3
    n = 5
    print("Sum of Given AP Series:", sum_of_ap(a, d, n))














print()










