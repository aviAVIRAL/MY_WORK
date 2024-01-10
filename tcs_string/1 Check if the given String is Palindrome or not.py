# Example 1:
# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

# Example 2:
# Input: Str = “TAKE U FORWARD”
# Output: Not Palindrome
# Explanation: String when reversed is not the same as string.


# m1 r1  

def f(s):
    n = len(s)
    i = 0
    j = n - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1 
            j -= 1

    return True

if __name__ == "__main__":
    s = "  ! ABCDCBA , _ .. "
    ans = f(s)

    if ans == True:
        print("Palindrome")
    else:
        print("Not Palindrome")



# m1 r 2
        

def f ( s):
    n = len(s)
    i = 0 
    j = n - 1 
    
    a = s.lower( )

    # print(s)
    # print(a)

    while ( i < j ):
        if not a[i].isalnum():
            i+=1
        elif not a[j].isalnum():
            j-=1
        elif a[i] != a[j] :
            return False
        else :
            i+=1 
            j-=1 
        
    return True

if __name__=="__main__": 

    s = " _ . !  A A v i 2 2 i v a a  } "
    ans = f(s)

    if ans == True :
        print ( " palendriom ")
    else : 
        print ( "not palendrom ")

# output " palendriom "


if __name__=="__main__": 

    s = " _ . !  A A v i 2 2 i v a z  } "
    ans = f(s)

    if ans == True :
        print ( " palendriom ")
    else : 
        print ( "not palendrom ")

# output " not  palendriom "






# ...................................
# simple only some test case will pass : - 
        
def f(s):
    
    for i in range(n // 2):   # for loop 
        if s[i] != s[n - i - 1]:
            return False
    return True


if __name__ == "__main__":
    s = " ! MADAM ! "  
    n = len(s)
    print(f(s))

if __name__ == "__main__":
    s = "XSDCZfMADAM"
    n = len(s)  
    print(f(s))