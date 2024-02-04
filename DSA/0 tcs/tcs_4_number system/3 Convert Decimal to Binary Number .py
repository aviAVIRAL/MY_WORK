

# Convert Decimal to Binary Number
# Problem Statement: Convert decimal to binary number.

# Examples:

# Example 1:
# Input: N = 15
# Output: 1111
# Explanation: 15 in binary is represented as "1111".

# Example 2:
# Input: 18
# Output: 10010
# Explanation: 18 in binary is represented as "10010".






# m1

s = 18

ans = bin(s)[2:]

print(ans)

 

# m2 

n = 18

arr = [0] * 32

i = 0

while n :      # while n > 0 :  # while n != 0 : 
    arr[i] = n % 2
    i += 1
    n //= 2

for j in range(i - 1 , -1, -1):
    print(arr[j], end="")

# m2 return type representation 
    
def f(n):

    temp =""
    arr = [0]*32
    i = 0

    while n :      # while n > 0 :  # while n != 0 : 
        arr[i] = n % 2
        i += 1
        n //= 2

    for j in range(i - 1 , -1, -1):
        temp += str(arr[j])

    return temp

if __name__ == "__main__":
    print(f(18))

#  m2  "".join type representation
   
def f(n):

    temp =[]
    arr = [0]*32
    i = 0

    while n :      # while n > 0 :  # while n != 0 : 
        arr[i] = n % 2
        i += 1
        n //= 2

    for j in range(i - 1 , -1, -1):
        temp.append(arr[j])

    ans =''.join( map(str,temp))


    return ans

if __name__ == "__main__":
    print(f(18))

# .............
    
# m2 ki representation hai b hai see just see 

n = 18
arr = [0] * 32
i = 0

while n :      # while n > 0 :  # while n != 0 : 
    arr[i] = n % 2
    i += 1
    n //= 2


ans = arr[:i]

sol = ans[::-1]

print(sol)

fianl_sol = ''.join(map(str,sol))

print(fianl_sol) 
    


