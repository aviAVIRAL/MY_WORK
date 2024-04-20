
    # tc = 0(n)^2  sc = 0(n)

def f(arr, k):
    n = len(arr)  # size of the array.
    mp = {}
    sum = 0
    Maxi = 0
    for i in range(n):
        sum += arr[i]
        if sum == k:
            Maxi = max(Maxi, i + 1)
        rem = sum - k
        if rem in mp:
            length = i - mp[rem]
            Maxi = max(Maxi, length)
        if sum not in mp:
            mp[sum] = i
    return Maxi

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    length = f(arr, k)
    print(f"{length}")


if __name__=="__main__":
    arr= [ -1, 1, 1]
    k = 1 
    print(f(arr, k))     



if __name__ == "__main__":
    arr = [2, 0, 0, 3]
    k = 3
    length = f(arr, k)
    print(f"{length}")





