

def f(arr, i):
    if i >= n/2:
        return arr
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    f(arr, i+1 )

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    n = len(arr)
    f(arr, 0)
    print(arr)
    



