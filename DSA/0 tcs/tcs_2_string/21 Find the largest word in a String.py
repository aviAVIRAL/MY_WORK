
# Find the largest word in a String
# Problem: Given a String, find the largest word in the string.

# Examples:

# Example 1:
# Input: string s=”Google Doc”
# Output: “Google”

# Explanation: Google is the largest word in the given string.

print()
# aapne aap kiya
# m1 

def f(s):
    
    arr = s.split()   
    max_len = -100

    for x in arr:
        if len(x) > max_len :
            max_len = len(x)
            ans = x
            
    return ans 

if __name__=="__main__":
    s = 'google doc aviralsharma'
    print(f( s))



