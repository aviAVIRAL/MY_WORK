

# concept  each element ki frequency find kr ne ta tarika  




# differences representations  and type   




print()
print()

# string 
    
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


print()
print()

# string 


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
    s  = "111233455677899"   
    f(s) 


print()
print()


# list 
    
def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for x in s :
        if x == ' ':
            continue
        else:
            freq[x] += 1

    # Printing Non-Repeating Characters
    for x in s :
        if freq[x] == 1 and x != ' ':
            print(x, end=" ")

if __name__ == "__main__":
    s  = [ 1, 1, 2 ,3,3,4,5,5,6,7,7,8,9,9  , 100]   
    f(s) 


print()
# list 
    
def f( s ):
    n = len(s )
    freq = [0] * 200   # 200 imp

    # Counting Frequencies
    for x in s :
        if x == ' ':
            continue
        else:
            freq[ord(x)] += 1

    # Printing Non-Repeating Characters
    for x in s :
        if freq[ord(x)] == 1 and x != ' ':
            print(x, end=" ")

if __name__ == "__main__":
    s  = [ '1', '1', '2' ,'3','3','4','5','5','6','7','7','8','9','9' ]   
    f(s) 

# ,'100'  notnont found 



