print("snvd")

def f(arr):

    arr.sort()
    print(arr)
    lng = 1 
    i = 0
    j = i + 1 
    n = len(arr)
    while (i < n-1):
        x = arr[i]
        cnt = 1
        if arr[i] == arr[j]:
            j += 1
            i += 1
        elif arr[j] == x+1:
            x +=1 
            cnt += 1
            j += 1
            i += 1




        lng = max(lng, cnt)
    return lng

if __name__=="__main__":
    arr = [100, 9,1,2,3,200, 1, 2, 3, 4]
    print(f(arr))

    




