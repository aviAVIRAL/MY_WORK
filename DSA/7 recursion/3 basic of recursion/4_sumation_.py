# summation 

# sumation of 3 is 3+2+1 = 6

# m-1

def f(i, sum):
    if i < 1:
        print(sum)
        return
    f(i - 1, sum + i)

if __name__ == "__main__":
    i = int(input("Enter i: "))
    f(i, 0)



# m -2 { break into sub prob }

def func(n):
    # Base Condition.
    if n == 0:
        return 0

    # Problem broken down into 2 parts and then combined.
    return n + func(n - 1)

if __name__ == "__main__":
    # Here, let’s take the value of n to be 3.
    n = 3
    print(func(n))


#  m-3 most easy way
def s(n):
    sum = 0
    for i in range(1, n+1): # Include n in the range
        sum +=i
    print(sum)

s(3)