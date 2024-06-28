# print N to 1 using recursion 

# output = 4, 3 , 2 ,1

# m-1

def f(i, n ):
    if i < n : 
        return 
    print(i , end = " ")
    f(i - 1 , 1 )

if __name__ =="__main__":
    i = int(input("enter the n : "))
    f(i , 1  )


# m-2

def f(n ):
    if n < 1 : 
        return 
    print(n , end = " ")
    f(n - 1 )

if __name__ =="__main__":
    n = int(input("enter the n : "))
    f(n  )
