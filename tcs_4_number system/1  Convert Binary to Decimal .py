# Convert Binary to Decimal
# Problem Statement: Convert a binary number to a decimal number.

# Examples:

# Example 1:
# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”.


# m1 build in funcion   ;-  int(s, 2)

s = "1011"

ans = int(s, 2)

print(ans)


# m2 logic

s = "1011"
n = len(s)
base = 1
ans = 0

for i in range(n -1, -1, -1):
    if s[i] == '1':
        ans += base

    base *= 2

print(ans)


# m3 logic

s = "1011"

s = s[::-1]  # reverse 

ans = 0

for i in range(len(s)):
    if s[i] == '1':
        ans += 2 ** i  

print(ans)




