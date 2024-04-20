
#  Leaders in an Array

# A Leader is an element that is greater than all of the elements on its right side in the array.

# Problem Statement: Given an array, print all the elements which are leaders. 

# Examples
# Example 1:
# Input:
#  arr = [4, 7, 1, 0]
# Output:
#  7 1 0
# Explanation:
#  Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

# Example 2:
# Input:
#  arr = [10, 22, 12, 3, 0, 6]
# Output:
#  22 12 6
# Explanation:
#  6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6



# brute  tc ~ n^2   sc = n 
# r1 

def f (a):
    n = len(a)
    temp = []

    for i in range(n) : 
        leader = True 
        for j in range(i+1, n):
            if a[j] > a[i] : 
                leader = False
                break 
        if leader:   # if leader  ==  True  :
            temp.append(a[i])

    return temp

if __name__=="__main__":
    arr = [10, 22, 12, 3, 0, 6]
    k = f(arr)
    for x in k: 
        print(x, end = " ")
    print()

# r2 

def f (a):
    n = len(a)
    temp = []

    for i in range(n) : 
        leader = True 
        for j in range(i+1, n):
            if a[j] > a[i] : 
                leader = False
                break 
            
        if leader == True :  # see  
            temp.append(a[i])

    return temp

if __name__=="__main__":
    arr = [10, 22, 12, 3, 0, 6]
    k = f(arr)
    for x in k: 
        print(x, end = " ")
    print()


# optimal tc n  sc n 
    

# r1 if output is coming like  6 12 22

def f (a):
    n = len(a)
    temp = []
    
    maxi =  0

    for i in range(n-1, -1 , -1):   
        if a[i] > maxi :
            temp.append(a[i]) 
            maxi = a[i]

    return temp

if __name__=="__main__":
    arr = [10, 22, 12, 3, 0, 6]
    k = f(arr)
    for x in k: 
        print(x, end = " ")
    print()

# r2  op  22 12 6
    
def f (a):
    n = len(a)
    temp = []
    
    maxi =  0

    for i in range(n-1, -1 , -1):   
        if a[i] > maxi :
            temp.append(a[i]) 
            maxi = a[i]

    return temp

if __name__=="__main__":
    arr = [10, 22, 12, 3, 0, 6]
    k = f(arr)
    for i in range ( len(k) -1 , -1 , -1):
        print(k[i], end = " ")  # reverse kr diya 
    print()


# also represnet as 

def f (a):
    n = len(a)
    temp = []
    
    maxi =  0

    for i in range(n-1, -1 , -1):   
        if a[i] > maxi :
            temp.append(a[i]) 
            maxi =max(maxi, a[i])

    return temp

if __name__=="__main__":
    arr = [10, 22, 12, 3, 0, 6]
    k = f(arr)
    for x in k: 
        print(x, end = " ")
    print()







