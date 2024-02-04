# Input:
# tiger     -> input string A
# ti          -> input string B
# Output:
# ger       -> Output string C


# r1 
def f ( s1 , s2):
    s = ""
    for x in s1: 
        if x not in s2:
            s += x
    return s 
if __name__=="__main__":
    s1 = 'tiger'
    s2 =  'ti'
    print(f (s1 , s2))

# r2 
def f ( s1 , s2):
    s = ""

    for x in s1: 
        if x in s2:
            continue  
        else: 
            s += x
    return s 
if __name__=="__main__":
    s1 = 'tiger'
    s2 =  'ti'
    print(f (s1 , s2))