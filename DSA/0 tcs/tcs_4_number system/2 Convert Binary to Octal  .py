# Convert Binary to Octal
# Problem Statement: Convert a binary number to an octal number

# Examples:

# Example 1:.
# Input: N = 1100110
# Output: 146
# Explanation: 1100110 when converted to octal number is “146”.

# Example 2:
# Input: 11111
# Output: 37
# Explanation: 11111 when converted to octal number is “37”.



# **octal number, every bit should be between 0 to 7.


# m 2

s = "1100110"
n = len(s)

if n % 3 == 1:
    s = "00" + s
elif n % 3 == 2:
    s = "0" + s

n = len(s)
ans = ""

for i in range(0, n, 3):
    temp = int(s[i]) * 4 + int(s[i + 1]) * 2 + int(s[i + 2]) * 1
    ans += str(temp)

print(ans)

 
# m 1 

s = "1100110"
n = len(s)

if n % 3 == 1:
    s = "00" + s
elif n % 3 == 2:
    s = "0" + s
                                                                                                                                                     
n = len(s)
ans = ""

for i in range(0, n, 3):

    temp = int(s[i:i+3], 2)
    ans += str(temp)

print(ans)
