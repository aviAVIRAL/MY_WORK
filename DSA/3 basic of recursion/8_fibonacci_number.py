# fibbonacci         : 0 0 1 1 2 5 8 13....
# range              : 0 1 2 3 4 5 6 7

# input : 6    
# output : 8 

# input : 5    
# output : 5 



# m-1 rep 1 with recursion 

def f(n):
    if n <= 1 :
        return n
    return f(n-1) + f(n-2)
if __name__=="__main__":
    print(f(4))

# m -1 rep 2 

def f(n):    
    if n == 0 :
        return 0    
    if n == 1 :
        return 1    
    return f(n-1) + f(n-2)
if __name__=="__main__":
    print(f(4))
    

# m-1 rep 3

def f(n):
    if n <= 1 :
        return n
    last = f(n-1) 
    Sec_Last = f(n-2)
    return last + Sec_Last

if __name__=="__main__":
    print(f(3))

# ....................................

# m-2  r-1 simple methoud { without reccrusrion }
# caerfull :-  range , return kya kr na hai 

def fibo(n):

    if n == 0 :
        return 0   
    
    elif n == 1 :
        return 1    
    
    a = 0
    b = 1
    for i in range(2, n+1):
       c = a + b
       a = b
       b = c        
    return b
        
if __name__=="__main__":
    print(fibo(5))


# m -2  rep -2 

def fibo(n):

    if n == 0 :
        return 0   
      
    a = 0
    b = 1

    for i in range(1, n+1):  # range 1 se start hai 
       c = a + b
       a = b
       b = c        
    return a     # return a  
        
if __name__=="__main__":
    print(fibo(5))




