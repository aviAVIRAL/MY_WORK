









# representation hai b hai see just see 

n = 28

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