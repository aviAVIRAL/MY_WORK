# xample 1:
# Input: Str = “take u forward”
# Output: tk  frwrd
# Explanation: All vowels are removed from the given String.

# Example 2:
# Input: Str = “I am very happy today”
# Output:  m vry happy tdy
# Explanation: All vowels are removed from the given String.





# r 1 

def f( s): 
    vowel = "aeiouAEIOU"
    str = ""

    for x in s: 
        if x not in vowel:
            str = str + x 
        #   str += x 
    return str 

if __name__=="__main__":
    s = "take u forward"
    print(f(s))


# output    tk  frwrd


# r 2 
    
def f( s): 
    
    str = ""

    for x in s: 
        if x not in ['a','e','i','o','u']:
            str = str + x 
        #   str += x 
    return str 

if __name__=="__main__":
    s = "take u forward"
    print(f(s))


# output    tk  frwrd
    
# ..................................

# r 3 
    

# while loop  

def f (s):

    n = len(s)

    vowel = "aeiou"
    str  = ""

    i = 0
    
    while ( i < n ):
        if s[i] not in vowel :
            str = str + s[i]
            i += 1  
        else: 
            i += 1

    return str 

if __name__=="__main__":
    s = "take u forward"
    print(f(s))
