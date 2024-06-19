def f(arr):
    n = len(arr)
    # edge case 
    if arr[0] != arr[1]: return arr[0]
    if arr[n-1] != arr[n-2]: return arr[n-1]
    
    for i in range(1, n-2):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
    return -1 


if __name__=="__main__": 
    arr = [1, 1, 2, 3, 3, 4, 4]
    print(f(arr))



if __name__=="__main__": 
    arr = [8, 1, 1, 3, 3, 4, 4]
    print(f(arr))



