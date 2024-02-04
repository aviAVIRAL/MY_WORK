# check string is palendrom or not :

# palendrom :-   same even after reverse / mirror immage 


def f(i, s):
    
    if i >= n // 2:
        return True
    
    if s[i] != s[n - i - 1]:
        return False
    
    return f(i + 1, s)


if __name__ == "__main__":
    s = " M A D A M "      #or    " 1 1 2 1 1 "
    n = len(s)
    print(f(0, s))

# output : True
 
if __name__ == "__main__":
    s = " l A X F B H D A M "  
    n = len(s)
    print(f(0, s))

# output : False 
    
# .................................

# simple methoud logic  without recursion 

# m1 r1
def f(s):

    i = 0
    while i <= n//2 :
        if s[i] != s[n - i - 1]:
            return False
        i +=1 
    return True  # caerfull  
        

# m1 r2
def f(s):
   
    i = 0
    while i <= n // 2:
        if s[i] != s[n - i - 1]:
            return False
        else:         # else  
            i += 1 
    return True

# m2 r1

def f(s):
    
    for i in range(n // 2):   # for loop 
        if s[i] != s[n - i - 1]:
            return False
    return True


if __name__ == "__main__":
    s = "MADAM"  
    n = len(s)
    print(f(s))

if __name__ == "__main__":
    s = "XSDCZfMADAM"
    n = len(s)  
    print(f(s))