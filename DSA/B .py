


import math

def  pos(arr,div,t):
    tot = 0 
    for i in range(len(arr)):
        tot += math.ceil(arr[i]/div)
    if tot <= t:
        return True 
    else : 
        return False 

def f(arr,t):
    for i in range(min(arr), max(arr)+1):
        if  ( pos(arr,i,t) == True ):
            return i 
    return -1 

if __name__=="__main__":
    arr = [1,2,5,9]
    t = 6 
    print(f(arr,t))

# by avi ..........
    
import math

def  pos(arr,div,t):
    tot = 0 
    for i in range(len(arr)):
        tot += math.ceil(arr[i]/div)
    if tot <= t:
        return True 
    else : 
        return False 

def f(arr,t):
    l = min(arr)
    h = max(arr)
    while l<=h:
        m = (l+h)//2

        if  (   pos(arr,m,t)  ):
            h = m - 1
        else:
            l = m + 1
        
        return m 
    return -1 

if __name__=="__main__":
    arr = [1,2,5,9]
    t = 6 
    print(f(arr,t))
