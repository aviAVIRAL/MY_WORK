def f(arr):
        n = len(arr)

        j = - 1
        for i in range(0, n):
            if arr[i] == 0:
                j = i 
                break 
              
        # i = j + 1
        # while i < n :
        #     if arr[i] != 0 :
        #         arr[i] , arr[j] = arr[j] , arr[i]
        #         i +=1 
        #         j += 1
            
        #     i +=1 
        
        i = j + 1
        while i < n:
            if arr[i] != 0:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
                j += 1
            i += 1

        return arr 


if __name__=="__main__":
        arr = [ 1,2,0,3,4,0,5,0,6,7,8]
        print(f(arr))

print("done n dusted ")

def f(arr,n):

    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range( j+1 , n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    
    return arr

arr = [ 1,2,0,3,4,0,5,0,6,7,8]
ans = f(arr,11) 
print(ans)



print( " ye to sahee hai ")

def f(arr, n):
    
    j = -1
    i = 0

    while i < n:
        if arr[i] == 0:
            j = i
            break
        i += 1

    i = j + 1
    while i < n:
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        i += 1

    return arr

arr = [ 1,2,0,3,4,0,5,0,6,7,8]
ans = f(arr, 11)  # Output: [1, 2, 4, 5, 0, 0, 0, 0]
print(ans)

def f(arr, n):
    j = -1
    i = 0

    while i < n:
        if arr[i] == 0:
            j = i
            break
        i += 1

    i = j + 1
    while i < n:
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        i += 1

    return arr

arr = [1, 2, 0, 3, 4, 0, 5, 0, 6, 7, 8]
ans = f(arr, 11)
print(ans)

def f(arr, n):
    j = -1
    i = 0

    while i < n:
        if arr[i] == 0:
            j = i
            break
        i += 1

    i = j + 1
    while i < n:
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        i += 1

    return arr

arr = [1, 2, 0, 3, 4, 0, 5, 0, 6, 7, 8]
ans = f(arr, 11)
print(ans)



def f(arr, n):
    j = -1
    i = 0

    while i < n:
        if arr[i] == 0:
            j = i
            break
        i += 1

    i = j + 1
    while i < n:
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        else:
            i += 1

    return arr

if __name__=="__main__":
     arr = [1, 2, 0, 3, 0, 4, 0, 0, 0, 6, 7, 9]
     n  = len(arr)
     ans = f(arr, n)
     print(ans)

