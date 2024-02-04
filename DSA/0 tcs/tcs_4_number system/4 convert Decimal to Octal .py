
# Convert Decimal to Octal

# Problem Statement: Given a decimal number, convert it into Octal Number.

# Examples:

# Example 1:
# Input:  17
# Output: 21
# Explanation: Octal Equivalent of 17 is 21



# m1
# build in function : 


s = 136
ans = oct(s)[2:]
print(ans)
# op 21


# m2  r1 

def f(n):

    temp =""
    arr = [0]*32
    i = 0
    while n != 0:
        arr[i] = n % 8
        i += 1
        n = n // 8
    
    for j in range(i - 1 , -1, -1):
        temp += str(arr[j])

    return temp

if __name__ == "__main__":
    print(f(136))

# m2  r2

   
def f(n):

    temp =[]
    arr = [0]*32
    i = 0

    while n :      # while n > 0 :  # while n != 0 : 
        arr[i] = n % 8
        i += 1
        n //= 8

    for j in range(i - 1 , -1, -1):
        temp.append(arr[j])

    ans =''.join( map(str,temp))


    return ans

if __name__ == "__main__":
    print(f(136))
















