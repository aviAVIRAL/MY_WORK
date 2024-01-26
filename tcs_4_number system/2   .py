


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
