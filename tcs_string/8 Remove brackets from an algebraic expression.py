# Example 1:
# Input: “a+((b-c)+d)”
# Output: “a+b-c+d”
# Explanation: Removed all the brackets in the algebric expression.

# Example 2:
# Input: “(((a-b))+c)”
# Output: “a-b+c”
# Explanation: Removed all the brackets in the algebric expression.












print( )

# m1
# r1
def solve(s):
    str = ""
    ToBeRemoved = "()"

    for x in s:
        if x not in ToBeRemoved : 
            str += x
    
    return str

if __name__ == "__main__":
    input1 = "a+((b-c)+d)"
    
    print("Original String:", input1)
    print("After removing brackets:", solve(input1))

    print( )

# r2
def solve(s):
    str = ""
   
    for x in s:
        if x not in [ '(' , ')'] : 
            str += x
    return str

if __name__ == "__main__":
    input1 = "a+((b-c)+d)"
    
    print("Original String:", input1)
    print("After removing brackets:", solve(input1))

    print( )



# m 2 

def f(s):
    str = ""

    for X in s:
        if  X != '('   and   X != ')':
            str += X

    return str

if __name__ == "__main__":
    s = "a+((b-c)+d)"
    print( f ( s))
    
# output is  a+b-c+d










