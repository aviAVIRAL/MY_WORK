

print()
print()

def f (arr):
    inc = 1
    dec = 1

    n = len(arr)
    i = 1

    while(i < n):
        if arr[i] > arr[i - 1]  :
            inc += 1 
            i += 1

        elif arr[i] < arr[i-1] :
            dec += 1
            i += 1
        elif arr[i] == arr[i - 1] :
            inc += 1
            dec += 1 
            i += 1
    print(inc)
    print(dec)
    if inc == n or dec == n :
        return True 
    else:
        return False

arr = [6,5,4,4]
print(f(arr))



print()
print()

def f (arr):
    inc = 1
    dec = 1

    n = len(arr)
    i = 1

    while(i < n):
        if arr[i] >= arr[i - 1]  :
            inc += 1 
            i += 1

        elif arr[i] <= arr[i-1] :
            dec += 1
            i += 1
        # elif arr[i] == arr[i - 1] :
        #     inc += 1
        #     dec += 1 
        #     i += 1
    print(inc)
    print(dec)
    if inc == n or dec == n :
        return True 
    else:
        return False

arr = [6,5,4,4]
print(f(arr))


# arr = [6,2,4,4]
# print(f(arr))

       

# arr = [1,2,3,4]
# print(f(arr))


def f (arr):
    inc = 1
    dec = 1

    n = len(arr)
    i = 1

    while(i < n):
        if  arr[i] <= arr[i-1] :
            dec += 1
            i += 1
        elif arr[i] >= arr[i - 1]  :
            inc += 1 
            i += 1

        
        # elif arr[i] == arr[i - 1] :
        #     inc += 1
        #     dec += 1 
        #     i += 1
    print(inc)
    print(dec)
    if inc == n or dec == n :
        return True 
    else:
        return False

arr = [6,5,4,4]
print(f(arr))
