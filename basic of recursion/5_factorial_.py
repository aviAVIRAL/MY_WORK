# factorial 

# factorial of 3 is 3*2*1 = 6

#  m-1 reprentation - 2  explicit return Best practices Standard Practices

def Funct(i, fac):
    if i < 1:
        return fac
    return Funct(i - 1, fac * i)

if __name__ == "__main__":
    
    print(Funct(4, 1))   
    
    # or 

    # res = fun(4,1)
    # print(res)


# m-1 reprentation - 1 

def f(i, fac):
    if i < 1:
        print(fac)
        return
    f(i - 1, fac * i)

if __name__ == "__main__":
    i = int(input("Enter i: "))
    f(i, 1)



# m -2 { break into sub prob }

def func(n):
    
    # Base Condition.
    if n == 1:
        return 1

    # Problem broken down into 2 parts and then combined.
    return n * func(n - 1)

if __name__ == "__main__":
    # Here, let’s take the value of n to be 3.
    n = 4
    print(func(n))


#  m-3 most easy way
def function_factorial_(n):
    fac = 1
    for i in range(1, n+1): # Include n in the range
        fac *= i
    print(fac)

function_factorial_(4)