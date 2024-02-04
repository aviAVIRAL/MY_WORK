# Example 1:
# Input: string str = "take12% *&u ^$#forward"
# Output: takeuforward
# Explanation:
# Characters 1,2,%,*,&,^,$,# along with whitespaces are 
# removed but the order of remaining alphabets is preserved.

# Example 2:
# Input: String str = "1.Python & 2.Java"
# Output: PythonJava
# Explanation: 
# Characters 1.&2. along with whitespaces are removed 
# but the order of remaining alphabets is preserved.


# r 1


def f(s): 
    str = ""
    
    for x in s: 
        if  'a'<= x <= 'z' or  'A'<= x <= 'Z'  :
            str = str + x

    return str 

if __name__=="__main__":
    s =  "take12% *&u ^$#forwaWWWWrd"
    print(f(s))


# r 2 
    

def f(s): 
    str = ""
    
    for x in s: 
        if  'a'<= x <= 'z' :
            str = str + x
        elif 'A'<= x <= 'Z' :
            str = str + x

    return str 

if __name__=="__main__":
    s =  "take12% *&u ^$#forwaWWWWrd"
    print(f(s))





# # .....................
#     just see or ignore it def solve(s):
    
def solve(s):
    ans = ""
    for char in s:
        ascii_value = ord(char)  # ASCII value

        if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):  # if alphabets
            ans += char
    return ans

if __name__ == "__main__":
    # Input string
    my_str = "take12% *&u ^$#forward"

    print("Resultant string:")
    print(solve(my_str))






