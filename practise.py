

# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *
# *             *
# * *         * *
# * * *     * * *
# * * * * * * * *

# m-1

def pattern_18_(n):
    for i in range(1,  2*n   +1):
        if i <= n :
            # star 
            for j in range ( 1,  n-i+1  +1):
                print("*", end=" ")
             # space
            for j in range( 1 , i*2-2  +1):
                print(" ", end =" ")

             # star 
            for j in range ( 1,  n-i+1  +1):
                print("*", end=" ")
        if i > n :
            # star 
            for j in range ( 1, i -n  +1):
                print("*", end=" ")
            # space - 1
            for j in range( 1 , 2*n - i  +1):
                print(" ", end =" ")
            # space - 2
            for j in range( 1 , 2*n - i  +1):
                print(" ", end =" ")
            # star 
            for j in range ( 1,  i- n  +1):
                print("*", end=" ")

        print()

# m - 2

def pattern_18_(n):
    for i in range(1,  2*n   +1):
        if i <= n :
            # star 
            for j in range ( 1,  n-i+1  +1):
                print("*", end=" ")
             # space
            for j in range( 1 , i*2-2  +1):
                print(" ", end =" ")
             # star 
            for j in range ( 1,  n-i+1  +1):
                print("*", end=" ")
        if i > n :
            # star 
            for j in range ( 1, i -n  +1):
                print("*", end=" ")
            # space  
            for j in range( 1 , 2*( 2*n - i ) +1):
                print(" ", end =" ")
            # star 
            for j in range ( 1,  i- n  +1):
                print("*", end=" ")

        print()

pattern_18_(4)


