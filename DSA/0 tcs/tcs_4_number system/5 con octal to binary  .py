

# Convert Octal to Binary
# Problem Statement: Given an Octal Number, convert it into Binary Number.

# Examples:

# Example 1:
# Input: 345
# Output: 11100101
# Explanation: Binary equivalent of given Octal expressionis 011100101





s = "345"

# Convert octal to decimal
x  = int(s, 8)

# Convert decimal to binary
ans = bin( x )[2:]

print(ans)    #   op 11100101


# ............representation..........
#  Convert Octal to Binary

x = 345
# O -> D
decimal = int(str(x), 8)
# D -> b 
binary = bin(decimal)[2:]

print(binary)





