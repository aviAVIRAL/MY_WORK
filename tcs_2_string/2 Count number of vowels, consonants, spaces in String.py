# r1 

def f(s): 
    s = s.lower()
    n = len(s)

    vowel = 0 
    consonant = 0 
    whiteSpace = 0 

    for i in range(n): 
        
        if s[i] in [ 'a', 'e', 'i', 'o', 'u']:
            vowel += 1
        
        elif 'a' <= s[i] <= 'z':
            consonant += 1
        
        elif s[i] == " ":
            whiteSpace += 1

    return vowel, consonant, whiteSpace

if __name__=="__main__":
    s = "Take u forward is Awesome"
    print(f(s)) 


# out put  
    
# (10, 11, 4) 

print( )
print( )



def f(s): 
    s = s.lower()
    n = len(s)

    vowel = 0 
    consonant = 0 
    whiteSpace = 0 

    string = "aeiou"

    
    for i in range(n): 
        
        if s[i] in string :
            vowel += 1
        
        elif 'a' <= s[i] <= 'z':
            consonant += 1
        
        elif s[i] == " ":
            whiteSpace += 1

    return vowel, consonant, whiteSpace

if __name__=="__main__":
    s = "Take u forward is Awesome"
    ans = print(f(s)) 

    
# out put  
    
# (10, 11, 4) 

# ........................................
print( )

def count_characters(s):
    vowels = 0
    consonants = 0
    whitespaces = 0

    # Converting the given string to lowercase
    s = s.lower()

    for char in s:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        elif 'a' <= char <= 'z':
            consonants += 1
        elif char == ' ':
            whitespaces += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("White Spaces:", whitespaces)

if __name__ == "__main__":
    my_str = "Take u forward is Awesome"
    count_characters(my_str)


# output 

# Vowels: 10
# Consonants: 11
# White Spaces: 4


print( )
print( )
# for i in range(length):
#     if str[i] in ['a', 'e', 'i', 'o', 'u']:
#         vowels += 1

def count_characters(s):
    vowels = 0
    consonants = 0
    whitespaces = 0

    # Converting the given string to lowercase
    s = s.lower()
    n = len(s)

    for i in range(n) :
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        elif 'a' <= s[i] <= 'z':
            consonants += 1
        elif s[i] == ' ':
            whitespaces += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("White Spaces:", whitespaces)

if __name__ == "__main__":
    my_str = "Take u forward is Awesome"
    count_characters(my_str)



print()
print()


def count_characters(s):
    vowels = 0
    consonants = 0
    whitespaces = 0

    # Converting the given string to lowercase
    s = s.lower()
    n = len(s)
    
    string = "aeiou"

    for i in range(n) :
        if s[i] in string :
            vowels += 1
        elif 'a' <= s[i] <= 'z':
            consonants += 1
        elif s[i] == ' ':
            whitespaces += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("White Spaces:", whitespaces)

if __name__ == "__main__":
    my_str = "Take u forward is Awesome"
    count_characters(my_str)



print()
print()



# ..................

# dekha trick  

def count_characters(s):
    # vowels = 0
    consonants = 0
    whitespaces = 0

    # Converting the given string to lowercase
    s = s.lower()

    for char in s:
        # if char in ['a', 'e', 'i', 'o', 'u']:
        #     vowels += 1
        if 'a' <= char <= 'z':
            consonants += 1
        elif char == ' ':
            whitespaces += 1

    # print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("White Spaces:", whitespaces)

if __name__ == "__main__":
    my_str = "Take u forward is Awesome"
    count_characters(my_str)


# output 
# Consonants: 21
# White Spaces: 4

# ............................................................