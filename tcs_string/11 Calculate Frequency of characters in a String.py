# Calculate Frequency of characters in a String

# Examples:

# Example 1:
# Input:   takeuforward
# Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 

    #   chhote se bada   { increasing oder .'.  sort kiya }

# Explanation: Count of every character of string is printed.

# Example 2:
# Input: articles
# Output: a1 c1 e1 i1 l1 r1 s1 t1 
# Explanation: Count of every character of string is printed.




print( )


def f(s):
    s = sorted(s)
    chr = s[0]
    count = 1

    for X in s[1:]:
        if X == chr:
            count += 1
        else:
            print(f"{chr}{count}", end=" ")
            count = 1
            chr = X

    print(f"{chr}{count}", end=" ")  # in acse of for the last element 

if __name__ == "__main__":
    s = "takeuforward"
    f(s)

# o/p ; a2 d1 e1 f1 k1 o1 r2 t1 u1 w1

# ...........................
    
# approach by me using mapping 
print( )    
print( )    

def f(s):
    s = sorted(s)
    mp = { }

    for x in s:
        if x not in mp:
            mp[x] = 1            
        else:
            mp[x] += 1
    
    return mp
    
if __name__ == "__main__":
    s = "takeuforward"
    ans = f(s)

    for y in ans :
        print( f"{y}{ans[y]}"  , end =" ")
    print()

# o/p:  a2 d1 e1 f1 k1 o1 r2 t1 u1 w1   : no space b/t variable [we can do space or any thing by own ]

if __name__ == "__main__":
    s = "takeuforward"
    ans = f(s)

    for y in ans :
        print(  y , ans[y] , end =" ")
    print()

# o/p:  a 2 d 1 e 1 f 1 k 1 o 1 r 2 t 1 u 1 w 1   : automaticaly space between vaeriables 
















