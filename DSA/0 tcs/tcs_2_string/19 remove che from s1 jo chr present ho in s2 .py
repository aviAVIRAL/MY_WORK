# Remove Characters from first String present in the Second String
# Problem Statement: Given two strings, write a program to remove characters from the first string which are present in the second string.

# Examples:

# Example 1:
# Input: String str1 = “abcdef”
#        String str2 = “cefz”
# Output: abd
# Explanation: The common characters in both strings are c, e, f.
# So after removing these characters from string 1 we get string resulting string as abd.


# Example 2:
# Input: String str1 = “xyzpw”
#        String str2 = “lmno”
# Output: xyzpw
# Explanation: As there is no common character in both the strings, string 1 remains unchanged


# m1 

def f(s1 , s2):
    temp = []

    for x in s1:
        if x not in s2:
            temp.append(x)

    return ' '.join(temp)

if __name__=="__main__":

    s1 = 'abcdef'
    s2 = 'cefz'
    print(f(s1 , s2))


# m2  mapping
    
def f(s1 , s2):
    
    str = ''
    mp = { }
    
    for x in s2:
        if x not in mp:
            mp[x] = 1
    
    for y in s1:
        if y not in mp:
            str += y
    
    return str

if __name__=="__main__":

    s1 = 'abcdef'
    s2 = 'cefz'
    print(f(s1 , s2))

    




