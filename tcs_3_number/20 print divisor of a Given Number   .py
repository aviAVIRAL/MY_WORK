# Factors of a Given Number

# factors jo koi us ko divide kr ne mein succes . uske sare factors hai 


# Example 1:
# Input: n = 6
# Output: 1,2,3,6
# Explanation: 6 is divisible by 1,2,3,6

# Example 2:
# Input: n = 9
# Output: 1,3,9
# Explanation: 9 is divisible by 1,3,9



n = 6

for i in range( 1, n+1):
    if n % i == 0 :
        print( i ,end= " ")


print()


def divisor(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

if __name__ == "__main__":
    n = 60
    print("Factors of", n, "are:", end=" ")
    divisor(n)

