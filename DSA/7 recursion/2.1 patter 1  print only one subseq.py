
def f(arr, brr , i, s, sum):
    if i  == len(arr):
        if s == sum :
            print(brr )
            return True 
        else: 
            return False 

 
    brr.append(arr[i])
    s += arr[i]
    if (f(arr, brr , i  + 1,  s, sum)):
        return True 
    

    brr.pop()
    s -= arr[i]
    if (f(arr, brr , i  + 1,  s, sum)):
        return True 

    return False

# main()

arr = [1, 2, 1]
f(arr, [], 0 , 0 , 2)    
# oop [1 ,1]


# .................
arr = [1,2,1]
print(f(arr, [], 0 , 0 , 2)    )

# to op is   [1, 1]
        #     True
