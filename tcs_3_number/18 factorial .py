

#  imp tcs nq t : factorial of a number without * operator 

# ip = 5
# op = 120


def Multi(a , b ):
    r = 0 
    for i in range(1 , b+1):
        r = r + a 
    return r 

def fact(n):
    sol = 1 
    for i in range( 1 , n+1 ):  #  for i in range( n, 0, -1 ): imp
        sol = Multi( sol , i)
    return sol 

if __name__=="__main__":
    k = 5 
    print( fact( k ))