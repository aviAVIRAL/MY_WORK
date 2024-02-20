

def f(arr, n):
    pos = []
    neg = []

    for x in arr: 
        if x > 0: 
            pos.append(x)
        else: 
            neg.append(x)
    
    j = 0 
    for i in range(0, n, 2):
        arr[i] = pos[j]
        j += 1

    k = 0 
    for i in range(1, n, 2):
        arr[i] = neg[k]
        k += 1
    
    return arr 

if __name__=="__main__":
    arr = [1,2,-4,-5]
    k = f(arr,len(arr))

    for x in k:
        print(x, end = " ")
    print()




