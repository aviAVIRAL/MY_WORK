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
def pattern_2_(n):
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
                
pattern_9_(5)


 


