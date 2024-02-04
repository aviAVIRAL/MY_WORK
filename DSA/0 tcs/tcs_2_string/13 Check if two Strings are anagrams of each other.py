


# Check if two Strings are anagrams of each other

#  anagrams :- a word or phrase that is made by arranging the letters of another word or phrase in a different/same order and length must be equal bhai 
#  abc -  abc  ,bca ,cba ,bac  etc 


# Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

# Examples:

# Example 1:
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

# Example 2:
# Input: RULES, LESRT 
# Output: false
# Explanation: Since the count of U and T  is not equal in both strings.



# m1 

def f(str1 , str2 ):

    if len(str1) != len(str2) :  # impo 
        return False

    for x in str1 : 
        if x not in str2  :
            return False 
               
    return True
        

if __name__ == "__main__":
    str1 = "cat"
    str2 = "atc"
    
    print(f(str1 , str2)) 
    

if __name__ == "__main__":
    str1 = "cat"
    str2 = "aKc"
    
    print(f(str1 , str2)) 
    
    
if __name__ == "__main__":
    str1 = "catccccc"
    str2 = "aKc"
    
    print(f(str1 , str2)) 
    


print()

# m 2.0

def f(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    freq = [0] * 26
    
    # Counting frequencies for str1
    for X in str1:
        freq[ord(X) - ord('A')] += 1
    
    # Decreasing frequencies for str2
    for X in str2:
        freq[ord(X) - ord('A')] -= 1
    
    # Checking if all frequencies are zero
    for count in freq:
        if count != 0:
            return False
    
    return True

if __name__ == "__main__":
    str1 = "INTEGER"
    str2 = "TEGERNI"
    
    print( f ( str1 , str2 ) )



print()

# m 2.1

def f(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    freq = [0] * 26
    
    # Counting frequencies for str1
    for X in str1:
        freq[ord(X)] += 1
    
    # Decreasing frequencies for str2
    for X in str2:
        freq[ord(X)] -= 1
    
    # Checking if all frequencies are zero
    for count in freq:
        if count != 0:
            return False
    
    return True

if __name__ == "__main__":
    str1 = "INTEGER"
    str2 = "TEGERNI"
    
    print( f ( str1 , str2 ) )















