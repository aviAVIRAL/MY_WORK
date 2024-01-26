


# concept

# list into string 

# 1

# arr = [ 'a' , 'b', 'c ']
# ans = ''.join(arr)
# print(ans)

# output is   abc

# 2  

# fruits = ['apple', 'banana', 'orange']
# ans = ', '.join(fruits)
# print(ans)

# Output: 'apple, banana, orange'

# 3

# word = 'hello'
# ans = '-'.join(word)
# print(ans)

# Output: 'h-e-l-l-o'

# ,,,,,,,,,,,,,,,,,,,,,,,,

# concept

# string into list  

# s = "abcd"

# ans = list(s)

# print(ans)

# # .........................
# Example 1:
# Input: str = “Take you forward” 
# Output: Takeyouforward
# Explanation: After removing all the whitespaces Takeyouforward is the result

# Example 2:
# Input: str = “How are you doing”
# Output: Howareyoudoing
# Explanation: After removing all the whitespaces Howareyoudoing is the result
# # .........................


# m1 r1 

# for loop  each element wala 

def f(s): 
    arr = []
    
    for x in s: 
        if x != " ":
            arr.append(x)

    str =  ''.join(arr)

    return str 

if __name__=="__main__":
    s =  "Take you forward"
    print(f(s))


# m1 r 2

# for loop range wala 

def f(s): 
    arr = []
    n = len(s)

    for i in range(n): 
        if s[i] != " ":
            arr.append(s[i])

    str =  ''.join(arr)

    return str 

if __name__=="__main__":
    s =  "Take you forward"
    print(f(s))


# m 2 

def f(s): 
    
    arr = list(s)      # first convert string into list 
    temp = [ ]
    
    for x in arr: 
        if x != " ":
            temp.append(x)

    str =  ''.join(temp)

    return str 

if __name__=="__main__":
    s =  "Take you forward"
    print(f(s))




# .......................


# m 4 
    

# simple methoud  
    
def f( s): 
    whiteSpace = " "
    str = ""

    for x in s: 
        if x not in whiteSpace:
                str += x
    return str 

if __name__=="__main__":
    s = "Take you forward"
    print(f(s))
