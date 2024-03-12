

print()
print()
print()

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)


print("...................")

numbers = [1, 2, 3, 4, 5]

index = 0

while index < len(numbers):
    num = numbers[index]
    if num % 2 == 0:
        index += 1
        continue
    
    print(num)
    
    index += 1


print("...................")