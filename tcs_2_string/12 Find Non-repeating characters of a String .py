# Find Non-repeating characters of a String

# Examples:

# Example 1:
# Input: string = “google”
# Output: l,e

# Explanation: Non repeating characters are l,e.

# Example 2:
# Input: string = “yahoo”
# Output: y,a,h
# Explanation: Non repeating characters are y,a,h



#   m1  r1


def f(st):
    n = len(st)
    result = []
    freq = [0] * n


    for i in range(n):
        for j in range(n):
            if st[i] == st[j]:
                freq[i] += 1

    
    for i in range(n):
        if freq[i] == 1 and st[i] != ' ':
            result.append(st[i])

    return result

if __name__ == "__main__":
    st = "Takaeuforward"
    l = len(st)
    

    result = f(st)
    
    print(result)

# output as list form => ['T', 'k', 'e', 'u', 'f', 'o', 'w', 'd']

print( )
print( )

# 1m  r 2 
    

def f(st):
    n = len(st)
    # result = [] 
    string = ""
    freq = [0] * n
     

    for i in range(n):
        for j in range(n):
            if st[i] == st[j]:
                freq[i] += 1
    

    for i in range(n):
        if freq[i] == 1 and st[i] != ' ':
            string += st[i]  

    return string 
if __name__ == "__main__":
    st = "Takaeuforward"
    l = len(st)
    

    result = f(st)
    
    print(result)

# output as string form => Tkeufowd

print()

# ....................................

# m 2   #  mapping 
def f ( s): 

    n = len(s)
    mp = { }

    for x in s : 
        if x not in mp : 
            mp[x] = 1
        else : 
            mp[x] += 1

    return mp


if __name__=="__main__":
    s = "takeuforward"
    ans = f(s)

    for y in ans: 
        if ans[y] == 1 :
            print(y , end = " ")

# output => t k e u f o w d

print()
# also rep 
def f ( s): 

    n = len(s)
    mp = { }

    for x in s : 
        if x not in mp : 
            mp[x] = 1
        else : 
            mp[x] += 1

    for y in mp: 
        if mp[y] == 1 :
            print(y , end = " ")


if __name__=="__main__":
    s = "takeUForward"
    f(s)

    

# output => t k e u f o w d

print()

# ........................

# m3  r 1.0   impo 
    

def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for i in range(n):
        if s [i] == ' ':
            continue
        else:
            freq[ord(s [i]) - ord('a')] += 1

    # Printing Non-Repeating Characters
    for i in range(n):
        if freq[ord(s [i]) - ord('a')] == 1 and s [i] != ' ':
            print(s [i], end=" ")

if __name__ == "__main__":
    s  = "take u forward"   
    f(s) 
    
print()


# m3  r 1.1   impo 
    

def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for i in range(n):
        if s [i] == ' ':
            continue
        else:
            freq[ord(s [i])] += 1

    # Printing Non-Repeating Characters
    for i in range(n):
        if freq[ord(s [i])] == 1 and s [i] != ' ':
            print(s [i], end=" ")

if __name__ == "__main__":
    s  = "take u forward"   
    f(s) 
    
print()



# m3  r 2.0 
    
def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for x in s :
        if x == ' ':
            continue
        else:
            freq[ord(x) - ord('a')] += 1

    # Printing Non-Repeating Characters
    for x in s :
        if freq[ord(x) - ord('a')] == 1 and x != ' ':
            print(x, end=" ")

if __name__ == "__main__":
    s  = "take u forward"   
    f(s) 


   
print()



# m3  r 2.1 
    
def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for x in s :
        if x == ' ':
            continue
        else:
            freq[ord(x) ] += 1

    # Printing Non-Repeating Characters
    for x in s :
        if freq[ord(x) ] == 1 and x != ' ':
            print(x, end=" ")

if __name__ == "__main__":
    s  = "take u forward"   
    f(s) 











































