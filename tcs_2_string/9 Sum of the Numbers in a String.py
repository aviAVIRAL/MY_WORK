
# Sum of the Numbers in a String

# Examples:

# Example 1:
# Input: string = “123xyz”
# Output:   123

# Example 2:
# Input: string = “2xyz23”
# Output: 25  :----    2 + 23 = 25 



# ..............

def f( s ):

    n = len(s)
    
    str = ""
    sum = 0

    for i in range(n):
        
        if '0' <= s[i] <= '9':
            str += s[i]
        
        else:
            sum += int(str)
            str = ""

    return sum + int(str)

if __name__ == "__main__":
    s = "1a30z67"
    print(f (s))

# ,,,,,,,,,,,,,,,,,,,,,,,,
    

# # 
#  if char.isdigit():
    
print( )

def f( s ):

    n = len(s)
    
    str = ""
    sum = 0

    for i in range(n):

        if s[i].isdigit()  :
            str += s[i]
        
        else:
            sum += int(str)
            str = ""

    return sum + int(str)

if __name__ == "__main__":
    s = "1a30z67"
    print(f (s))

# ....................................



print( )

def f( s ):

    # n = len(s)
    
    str = ""
    sum = 0

    for X in s :

        if  X.isdigit()  :
            str += X
        
        else:
            sum += int(str)
            str = ""

    return sum + int(str)

if __name__ == "__main__":
    s = "1a30z67"
    print(f (s))



# .......................................................


