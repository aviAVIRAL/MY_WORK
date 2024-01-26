# Express given number as Sum of Two Prime Numbersv

# more deeply explain on notes 







# r 1 

def fun(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def f(n):
    return fun(n) and fun(n - 2)

if __name__ == "__main__":
    n = 13
  
    if f(n):
        print("Yes")
    else:
        print("No")

    

# standard representation 
        
class SumOf2Prime:

    def is_prime(self, n):
        if n <= 1:
            return False

        for i in range(2, n ):
            if n % i == 0:
                return False

        return True

    def prime(self, n):
        return self.is_prime(n) and self.is_prime(n - 2)

if __name__ == "__main__":
    n = 13
    s1 = SumOf2Prime()
    if s1.prime(n):
        print("Yes")
    else:
        print("No")


# represenration 
        
def fun(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def f(n):
    if fun(n) and fun(n - 2):
        return True
    else:
        return False

if __name__ == "__main__":
    n = 13

    if f(n):
        print("Yes it can express ..........")
    else:
        print("No")












