# * * * *
# * * * *
# * * * *
# * * * *


def pattern_1_(n):
    for i in range(1, n+1):
        for j in range(1,n+1):
            print("*", end = " ")
        print()
def pattern_1_(n):
    i = 1
    while i < n + 1:
        j = 1
        while j < n + 1:
            print("*", end=" ")
            j += 1
        
        print()
        i += 1  


# *
# * *
# * * *
# * * * *

def pattern_2_(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print("*", end = " ")
        print()
def pattern_2_Another_Approach_(n):
    for i in range(1, n + 1):
        print("* " * i)
def pattern_2_(n):
    i = 1
    while i < n + 1:
        j = 1
        while j < i + 1:
            print("*", end=" ")
            j += 1
        
        print()
        i += 1

# 1
# 2 2
# 3 3 3
# 4 4 4 4

def pattern_3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()
def pattern_3(n):
    i = 1
    while i < n + 1:
        j = 1
        while j < i + 1:
            print(i, end=" ")
            j += 1
        
        print()
        i += 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
def pattern_4_(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
def pattern_4_(n):
    i = 1
    while i < n + 1:
        j = 1
        while j < i + 1:
            print(j, end=" ")
            j += 1
        
        print()
        i += 1

# * * * *
# * * *
# * *
# *

# for loop :
def pattern_5_(n):
    for i in range(1, n+1 ):
        for j in range(1, n -i +1 +1):
            print("*", end=" ")
        print()

# reverse chalo loop to :
def pattern_5_(n):
    for i in range(n  , 0 , -1  ):
        for j in range(1 , i  ):
            print("*", end=" ")
        print()

# while loop :
def pattern_5_(n):
    i = 1
    while i < n + 1:
        j = 1
        while j < n - i + 1 +1:
            print("*", end=" ")
            j += 1
        
        print()
        i += 1

# M-2
def pattern_5_another_Approach_(n):
    for i in range( 1, n    +1):
        print((n-i+1)* "*")




# 1 2 3 4
# 1 2 3
# 1 2
# 1
def pattern_6_(n):
    for i in range(1, n+1 ):
        for j in range(1, n -i +1 +1):
            print(j, end=" ")
        print()
def pattern_6_(n):
    i = 1
    while i < n + 1:
        j = 1
        while j < n - i + 1 +1:
            print(j, end=" ")
            j += 1
        
        print()
        i += 1



#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
def pattern_7_(n):
    for i in range(1, n  +1):
        # space
        for j in range(1, n - i  +1):
            print(" ", end=" ")
        # Star
        for j in range(1, 2*i - 1  +1):
            print("*", end=" ")
        # space
        for j in range(1, n - i  +1):
            print(" ", end=" ")
 
        print()

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
def pattern_8_(n):
    for i in range(1, n   +1):
        # space
        for j in range(1, i -1    +1):
            print(" ", end=" ")
        # Star
        for j in range(1,  2*n - 2*i +1   +1):
            print("*", end=" ")
        # space
        for j in range(1, i -1  +1):
            print(" ", end=" ")
 
        print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

def pattern_9_(n):  
    pattern_7_(5)  # fun patter_7 ko call kiya  n = 5 dal diya 
    pattern_8_(5)  # fun patter_8 ko call kiya  n = 5 dal diya 
                
# pattern_9_(5)


#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# m-2  
def pattern(n):
    for i in range(1, n   +1 ):
        print( (" "*(n-i)) + "*"*i )

# m-1
def pattern(n):
    for i in range(1, n   +1 ):
        # space
        for j in range(1,  n - i   +1):
            print(" " , end = " ")
        # star
        for j in range(1,  i   +1):
            print("*" , end = " ")
        
        print() 



# i

# 1  *            n = 5   { 5 * 2 - 1 = 9 total row  } 
# 2  * *              .'. i = 9
# 3  * * *
# 4  * * * *         
# 5  * * * * *     n = 5 tak symmetry only 
# 6  * * * *        
# 7  * * *
# 8  * *
# 9  *

def pattern_11_(n):
    for i in range(1, 2*n -1   +1):
        if i <= n :
            for j in range( 1 , i   +1) :
                print("*", end =" ")
        else :
            for j in range( 1, 2*n - i   +1):
                print("*", end  = " ")

     
        print ()

 


# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *
# *             *
# * *         * *
# * * *     * * *
# * * * * * * * *

# m-1

def pattern_18_same_concept_to_11(n):
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

def pattern_18_same_concept_to_11(n):
    for i in range(1,  2*n   +1):
        if i <= n :
            # star 
            for j in range ( 1,  n-i+1  +1):
                print("*", end=" ")
             # space
            for j in range( 1 , 2*(i-1)  +1):
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


# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0
# 1 0 1 0 1 0

# m - 1
def pattern_12_(n):
    for i in range(1, n + 1):
        for j in range(i):
            if (i + j) % 2 == 0:  
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

# m - 2
def pattern_12_(n):
    for i in range(1, n  +1):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(1,  i   +1):
            print(start, end=" ")
            start = 1 - start     # alternate concept 
        
        print()


#   1                 1   
#   1 2             2 1
#   1 2 3         3 2 1
#   1 2 3 4     4 3 2 1
#   1 2 3 4 5 5 4 3 2 1


def pattern_13_(n):
    for i in range(1, n  +1):
        
        count = 1
        for j in range(1,  i   +1):
            print(count, end=" ")
            count += 1
#              or 
#       for j in range(1,  i   +1):
#           print(j, end=" ")

        for j in range(1, 2*n -2*i   +1):
            print(" ", end=" ")
        
        
        for j in range(1,  i   +1):                             
            print(i, end=" ")
            i -=1          #  important  part 
      #       or 
      # for j in range( i , 0 , -1 ):    0 is not included//let i=3 than 3,2,1 
      #     print(j, end =" ") 
        #      or 
        # count = i
        # for j in range( 1, i +1):
        #     print(count, end= " ")
        #     count -=1
        
        print()



# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


def pattern_13_1_(n):
    count =1 
    for i in range(1, n  +1):
        for j in range(1, i +1):
            print(count , end = " ")
            count +=1 
        print()


# A
# A B
# A B C
# A B C D
# A B C D E

def pattern_14_(n):
    for i in range(1, n   +1):
        num = 'A'
        for j in range(1 , i  +1):
            print(num , end =" ")
            num = chr( ord(num) + 1 )
        print()


# A
# B C
# D E F
# G H I J
# K L M N O

def pattern_14_1_(n):
    num = 'A'
    for i in range(1, n   +1):
        for j in range(1 , i  +1):
            print(num , end =" ")
            num = chr( ord(num) + 1 )
        print()

# A B C D E
# A B C D
# A B C
# A B
# A

def pattern_15_(n):
    for i in range(1,  n   +1):
        num = "A" 
        for j in range(1, n - i + 1   +1):
            print(num , end=" ")
            num = chr(  ord(num) + 1  )
        print()


# A             * I M P O R T A N T
# B B
# C C C
# D D D D
# E E E E E       

# M-1
def pattern_16_(n):
    for i in range(1, n   +1):
        num = chr(ord("A") + i - 1 ) # also num = chr(65 + i - 1 )
        for j in range(1 , i   +1):
            print(num, end= " ")
         # No need for updation    
        print()

# M-2
def pattern_16_(n):
    num = "A"
    for i in range(1,  n   +1):
        # num = "A" 
        for j in range(1, i  +1):
            print(num , end=" ")
            # num = chr(  ord(num) + 1  )
        print()
        num = chr(  ord(num) + 1  )
        

#           A
#         A B A
#       A B C B A
#     A B C D C B A
#   A B C D E D C B A


def pattern_17_(n):
    for i in range(1,  n   +1):
       
        # space
        for j in range(1, n - i + 1   +1):
            print( " " , end=" ")
        
        # chr    I M P O R T A N T
        num = "A"                  
        breakpoint = (2*i - 1)//2   
      
        for j in range(1 ,2*i - 1   +1):
            print( num  , end=" ")
            if j <= breakpoint :
                num = chr(ord(num) + 1 )
           
            else :
                num = chr(ord(num) - 1 )   
       
        # space  


        for j in range(1, n - i + 1   +1):
            print( " " , end=" ")


        print()


# E           I M P O R T A N T 
# D E
# C D E
# B C D E
# A B C D E


def pattern_18_(n):

    for i in range(1,  n   +1):
       
        num = chr(ord("E") - i + 1 )

        for j in range(1,  i   +1):
        
            print(num , end =" " )
        
            num = chr(ord(num) + 1) 

        print()


# pattern 18 done upper 



