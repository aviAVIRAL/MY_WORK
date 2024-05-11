# Capitalize first and last character of each word of a string

# Examples:

# Example 1:
# Input: String str = "take u forward is awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: We get the result after capitalizing the first and last character of each word of a string

# Example 2:
# Input: String str = "Take u Forward is Awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: Characters T, F, A are initially in uppercase , so they remain as they are in the result.



# r1 

def f(s):
    temp = []

    for x in s.split():
        n = len(x)

        if n > 1:
            x = x[0].upper() + x[1:n-1] + x[n-1].upper()
        else:
            x = x.upper()

        temp.append(x)

    return ' '.join(temp)

if __name__ == "__main__":
    s = "take u forward is awesome"
    print(f(s))


print( )

# r2


def f (s): 
    
    arr = s.split()
    temp = []
    
    # n = len(x)
    
    for x in arr : 
        n = len(x)
    
        if n > 1 :
            x = x[0].upper() + x[1:n-1] + x[n-1].upper()
        else:
            x = x.upper()

        temp.append(x)     

    return ' '.join(temp)   # ' spacing '.join(temp)


if __name__ == "__main__":
    s =  "take u forward is awesome"
    print( f ( s))
 
# output TakE U ForwarD IS AwesomE 
    





