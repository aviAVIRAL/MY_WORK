print()
print()

# m1 using % operator  

def f(n):
    if n % 2 == 0 :
        return True
    else : 
        return False
if __name__=="__main__":
    n =  4
    if f(n):
        print("even")
    else:
        print("odd")


# m2  using bitwise operator : &

def f(n):
    if n & 1 == 0:
        return True 
    else:
        return False

if __name__ == "__main__":
    n = 4
    if f(n) : 
        print( f"{n} is even" )
    else:
        print( f"{n} is odd" )








