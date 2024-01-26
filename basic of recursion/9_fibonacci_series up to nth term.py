# fibbonacci serires 
# 0 1 1 2 5 8 13....

# input : 5    
# output : 0 0 1 1 2 5


def fibo(n):

    a = 0
    b = 1

    for i in range(n+1): 
       print(a , end = " ") 
       c = a + b
       a = b
       b = c        
    
if __name__=="__main__":
   fibo(5)


