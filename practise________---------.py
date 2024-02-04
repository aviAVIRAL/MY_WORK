


def DecimaltoOctal(decimal):
    octal = 0
    i = 0
    while decimal != 0:
        rem = decimal % 8
        octal += rem * 10 ** i
        i += 1
        decimal = decimal // 8
    return octal

if __name__ == "__main__":
    decimal = 136
    print(f"The Octal conversion of the given decimal number is {DecimaltoOctal(decimal)}")



print()
print()



n = 136
arr = [0]*32
i = 0
while decimal != 0:
    arr[i] = decimal % 8
    i += 1
    decimal = decimal // 8
for j in range(i - 1 , -1, -1):
    print(arr[j], end="")



print()
print()



# represent : imp 

def DecimaltoOctal(decimal):

    temp =""
    arr = [0]*32
    i = 0
    while decimal != 0:
        arr[i] = decimal % 8
        i += 1
        decimal = decimal // 8
    
    for j in range(i - 1 , -1, -1):
        temp += str(arr[j])

    return temp

if __name__ == "__main__":
    print(DecimaltoOctal(136))




