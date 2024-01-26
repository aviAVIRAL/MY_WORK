# Permutations in which N people can occupy R seats
# Problem Statement: Find permutations in which n people can occupy r seats in a classroom.

# Examples:

# Example 1:
# Input: N = 5, r = 3
# Output: 60
# Explanation: To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60


def fac(n):
    r = 1 
    for i in range(1, n+1):
        r *= i
    return r    
 

def f(a , b):
    sol = fac(a) / fac(a-b)

    return sol 

if __name__=="__main__":
    print(f(5 , 3))





