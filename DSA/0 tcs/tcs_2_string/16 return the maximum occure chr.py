


# Maximum occurring character in a string
# Maximum occurring character in a string

# Problem Statement: Given a string, return the character that occurs the maximum number of times in the string. If the maximum occurrence of two or more characters is the same, return any one of them. 

# Examples:

# Example 1:
# Input: str = “takeuforward”
# Output: a
# Explanation: The character 'a' and 'r’ have the same  maximum occurrence i.e 2. Hence we can print any one of them

# Example 2:
# Input: str = “apple”
# Output: p
# Explanation: The character 'p' have the maximum occurrence i.e 2.




def f(s):
    
    Max = 0
    freq = [0] * 256
    
    for x in s:
        freq[ord(x)] += 1

        if freq[ord(x)] > Max  and x != " " :  # to avoid white space as answer
            Max = freq[ord(x)]
            ans = x

    return ans

if __name__ == "__main__":
    s="            aaviiiiii "
    print(f(s))

