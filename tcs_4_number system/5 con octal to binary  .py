

# Convert Octal to Binary
# Problem Statement: Given an Octal Number, convert it into Binary Number.

# Examples:

# Example 1:
# Input: 345
# Output: 1111000
# Explanation: Binary equivalent of given Octal expressionis 011100101





s = "170"

# Convert octal to decimal
x  = int(s, 8)

# Convert decimal to binary
ans = bin( x )[2:]

print(ans)
