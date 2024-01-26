














n = 28
binary = []
i = 0

while n:
    binary.append(n % 2)
    i += 1
    n //= 2

for ind in range(i - 1, -1, -1):
    print(binary[ind], end="")


print()
print()

n = 28
binary = [0] * 32
i = 0

while n > 0:
    binary[i] = n % 2
    i += 1
    n //= 2

for ind in range(i - 1, -1, -1):
    print(binary[ind], end="")


print()
print()

n = 28
binary = [0] * 32
i = 0

while n > 0:
    binary[i] = n % 2
    i += 1
    n //= 2

ans = binary[:i]
print(ans)


