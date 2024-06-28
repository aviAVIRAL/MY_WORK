


def f(arr, brr , i, result): # wrong op wrong code 
    if i  == len(arr):
        result.append(brr[:])
        return
    brr.append(arr[i])
    f(arr, brr , i  + 1, result)
    brr.pop()  
    f(arr, brr , i  + 1, result)
# Example usage
arr = [1, 2, 3]
f(arr, [], 0, [])


print(result)
